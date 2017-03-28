#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from testrail_client import TestRailClient
from robot.api import TestData
from robot.errors import DataError
from robot.writer.datafilewriter import DataFileWriter


def getTagsValue(tags):
    """
    Get value from robot framework's tags for TestRail.
    """
    attributes = dict()
    matchers = ['testRailId', 'defects', 'references']
    for matcher in matchers:
        if tags is not None:
            for tag in tags:
                match = re.match(matcher, tag)
                if match:
                    split_tag = tag.split('=')
                    tag_value = split_tag[1]
                    attributes[matcher] = tag_value
                    break
                else:
                    attributes[matcher] = None
    return attributes

ROBOT_HEAD = '*** Test Case ***'
ROBOT_TEMPLATE = """

{test_name}
    {precondition}
    {case_information}
    [Tags]  testRailId={case_id}   Developing
    Fail    待自动化用例
"""


class ArtificialCaseManager(TestRailClient):

    def __init__(self, host, user, password, project_id,
                 file_path, section_name, file_format='robot'):
        """
        :param host: test rail host
        :param user: user name
        :param password: password
        :param project_id: int, test rail project id
        :param file_path: path of test case files or directory
        :param section_name: str, section name like 'robot_data_distribution'
        :param file_format: default to be .robot
        """
        super(ArtificialCaseManager, self).__init__(host, user, password)
        self.file = list()
        self.project_id = project_id
        self.section_name = section_name
        # to loop through the test suites
        try:
            if os.path.isdir(file_path):
                for files in os.walk(file_path):
                    for robot_file in filter(lambda x: x.endswith('.robot'), files[2]):
                        if robot_file != 'case-back.robot':
                            self.file.append(
                                TestData(source=os.path.abspath(os.path.join(files[0],
                                                                             robot_file))
                                         )
                            )
            else:
                self.file.append(TestData(source=file_path))
        except DataError as e:
            # robot file may have no test cases in it
            error_str = (
                '[ \033[1;33mWARNING\033[0m ] Cannot find test cases',
                '            ' + e.message
            )
            print '\n'.join(error_str)

        self.writer = DataFileWriter(format=file_format)

    def get_section_id(self):
        """
        get section id from test rail
        :return: int, section id
        """
        return filter(lambda x: x['name'] == self.section_name,
                      self.section.for_suite(self.project_id))[0]['id']

    def get_cases(self, section_id=''):
        """
        get newly added test cases from test rail
        :param section_id: int, section id on test rail
        :return: dict, cases
        """
        # type_id = 16 is corresponding to 'newly' type
        return filter(lambda x: x['type_id'] == 16,
                      self.case.for_project(self.project_id, section_id=section_id)
                      )

    def update_artificial_cases(self):
        robot_ids = set()
        section_id = self.get_section_id()
        if section_id is None:
            return
        for suite in self.file:
            for test in suite.testcase_table.tests:
                test_rail_id = getTagsValue(test.tags.value).get('testRailId')
                if test_rail_id is not None:
                    robot_ids.update([int(test_rail_id)])
        test_cases = dict()
        test_rail_ids = set()
        for case in self.get_cases(section_id):
            test_rail_ids.add(case['id'])

            test_cases[case['id']] = case

        artificial_case_ids = test_rail_ids - robot_ids

        robot_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                  'test_suites/case-back.robot')
        if_exist = os.path.exists(robot_file)
        with open(robot_file, 'a') as f:
            if not if_exist:
                f.write(ROBOT_HEAD)
            for case_id in artificial_case_ids:
                steps = ''
                custom_preconds = '# precondition: {}'\
                    .format(test_cases[case_id]['custom_preconds'])
                for step in test_cases[case_id]['custom_steps']:
                    steps += '# content: {content}, expected: {expected}\n'.format(**step)
                f.write(
                    ROBOT_TEMPLATE.format(test_name=test_cases[case_id]['title'],
                                          case_information=steps,
                                          case_id=case_id,
                                          precondition=custom_preconds)
                )


def gen_artificial_cases():
    section_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    if section_path.split('/')[-1] == "workspace":
        project_name = section_path.split('/')[-2]
    else:
        project_name = section_path.split('/')[-1]
    # in jenkins there is a work space in path like '/var/lib/jenkins/jobs/robot_data_distribution/workspace'
    manager = ArtificialCaseManager('testrail.ele.me', 'weiguo.yu@ele.me', 'Eisoo_com123',
                                    53, os.path.join(section_path, 'test_suites'), project_name)
    manager.update_artificial_cases()


if __name__ == '__main__':
    gen_artificial_cases()
