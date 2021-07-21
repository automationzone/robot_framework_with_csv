from FW_upgrades import runner
run = runner()

run.start_suite("TestSuite", testcases=["testcase01"])