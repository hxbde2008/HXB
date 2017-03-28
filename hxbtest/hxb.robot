*** Settings ***
Documentation    Suite description
Library           test.py

*** Test Cases ***
测试
    [Tags]    DEBUG
    测试一下

*** Keywords ***
测试一下
    log  ${a}