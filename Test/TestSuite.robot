*** Settings ***
Library    SeleniumLibrary
Test Setup    OpenBrowser
Test Teardown    CloseAll
Resource    setupteardown.robot
Variables  ../Library/POM/Keywords/csv_read.py    data.csv
Library    ../Library/suite_functions.py


*** Test Cases ***
testcase01
    log   testcase001
    log   ${${TEST_NAME}.parameter1}
    suite_functions.perform_a_actions

testcase02
    log   testcase002

testcase03
    log   testcase003



