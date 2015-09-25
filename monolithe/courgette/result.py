# -*- coding: utf-8 -*-

class CourgetteResult(object):

    def __init__(self):
        """
            Initializes the CourgetteResult
        """
        self._failures = 0
        self._errors = 0
        self._success = 0
        self._total = 0
        self._reports = {}


    ## properties

    @property
    def reports(self):
        return self._reports

    @property
    def failures(self):
        return self._failures

    @property
    def errors(self):
        return self._errors

    @property
    def success(self):
        return self._success

    @property
    def total(self):
        return self._total


    ## report management

    def add_report(self, specification_name, report):
        """
            Adds a given report with the given specification_name as key
            to the reports list and computes the number of success, failures
            and errors

            Args:
                specification_name: string representing the specification (with ".spec")
                report: The
        """
        self._reports[specification_name] = report

        self._total    = self._total + report.testsRun
        self._failures = self._failures + len(report.failures)
        self._errors   = self._errors + len(report.errors)
        self._success  = self._total - self._failures - self._errors
