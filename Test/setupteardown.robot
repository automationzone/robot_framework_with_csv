*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
OpenBrowser
    SeleniumLibrary.Open Browser    https://www.google.com    chrome    executable_path=F:\\Python\\RobotFrameworkDataDriven\\driver\\chromedriver.exe

CloseAll
    SeleniumLibrary.Close Browser
