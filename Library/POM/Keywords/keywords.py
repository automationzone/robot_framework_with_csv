from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger

# Functions for Data
##############################################

def get_variable(variable):
    return BuiltIn().get_variable_value("${"+str(variable)+"}")

def data(variable):
    test_case = get_variable("TEST_NAME")
    return get_variable(test_case+"."+str(variable))

def set_test_variable(variable, value):
    BuiltIn().set_test_variable("${"+str(variable)+"}", value)

def set_suite_variable(variable, value):
    BuiltIn().set_suite_variable("${"+str(variable)+"}", value)

#  Function for logging
##############################################

def log_msg(str_text=""):
    logger.info(str_text)
    logger.console(str_text)

def log_debug(str_text=""):
    logger.debug(str_text)

def log_console(str_text=""):
    logger.console(str_text)

def fail_test_case(str_text=""):
    BuiltIn().fail(str_text)

# Functions for Selenium
##############################################

def get_selenium_instance():
    builtin = BuiltIn()
    return builtin.get_library_instance("SeleniumLibrary")

def get_driver():
    return get_selenium_instance().driver

def get_screenshot():
    get_selenium_instance().capture_page_screenshot()
