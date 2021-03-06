*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported Selenium2Library.
Library           Selenium2Library

*** Variables ***
${BROWSER}        chrome
${DELAY}          0
${VALID SERACH}     饿了么
${Search URL}      http://www.baidu.com

*** Test Cases ***
Valid Search
    Open Browser To Search Page
    Input Searchword  饿了么
    Submit Credentials
    wait until page contains  饿了么网上订餐

*** Keywords ***
Open Browser To Search Page
    Open Browser    ${Search URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Input Searchword
    [Arguments]    ${Searchword}
    input text  id=kw  ${searchword}

Submit Credentials
    Click Button    id=su



