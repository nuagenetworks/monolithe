# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from builtins import object


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

    # properties

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

    # report management

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

        self._total = self._total + report.testsRun
        self._failures = self._failures + len(report.failures)
        self._errors = self._errors + len(report.errors)
        self._success = self._total - self._failures - self._errors
