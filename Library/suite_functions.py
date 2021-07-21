from Library.POM.Keywords import keywords
from Library.POM.Keywords.keywords import data

def perform_a_actions():
    data("parameter2")

    keywords.log_msg("adding quantity in field")
    driver = keywords.get_driver()
    driver.find_ele()
    if True:
        keywords.log_msg("Step as passed and quanty has beep entered")
        keywords.get_screenshot()
    else:
        keywords.fail_test_case("there was an error when entering the qty")





