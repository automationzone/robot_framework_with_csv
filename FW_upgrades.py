from robot import run
import os
import csv


class runner:
    def __init__(self, report_path="Reports//"):
        self.report_path = report_path

    def start_suite(self, suite, testcases=None, tag="", loglevel="DEBUG:INFO"):
        suite_path = "Test/" + suite + ".robot"
        if testcases is None:
            testcases = []
        run(suite_path, test=testcases, outputdir=self.report_path, tag=tag, loglevel=loglevel)


