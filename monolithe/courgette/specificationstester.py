# -*- coding: utf-8 -*-
import json

from .courgette import Courgette

class SpecificationsTester (object):
    """ This class allows to run unit tests on a VSD server based on some specifications """

    def __init__(self, specifications_repository_manager):
        """ Initialize the SpecificationsTester

        """
        self._specifications_repository_manager = specifications_repository_manager


    def run_tests(self, specification_version, test_data, vsd_server_url, vsd_api_version, vsd_user, vsd_password, vsd_organization):
        """ Run auto test suite

        """
        total_failures = 0
        total_errors   = 0
        total_tests    = 0
        total_success  = 0
        total_score    = 0
        reports        = []

        for specification_file, data in test_data.iteritems():

            if "ignore" in data:
                continue

            report = {}

            report["specification"] = specification_file

            try:
                info                  = {}
                info["parentObject"]  = {"resourceName": data["parent_resource"], "id": data["parent_id"]}
                info["spec"]          = self._specifications_repository_manager.get_specification_data(specification_version=specification_version, specification_file=specification_file)
                info["defaultValues"] = json.loads(data["default_values"])

                courgette = Courgette(vsdurl=vsd_server_url, username=vsd_user, password=vsd_password, enterprise=vsd_organization, apiversion=vsd_api_version, data=info, swagger_path=None)
                result = courgette.run()

                report["tests_results"] = result

                total_failures = total_failures + len(result.failures)
                total_errors   = total_errors + len(result.errors)
                total_tests    = total_tests + result.testsRun

            except Exception as error:
                total_errors = total_errors + 1
                total_tests  = total_tests + 1
                report["processing_error"] = error

            reports.append(report)

        total_success = total_tests - total_failures - total_errors
        total_score = int((float(total_success) / float(total_tests)) * 100)
        return {"summary": {"errors": total_errors, "failures": total_failures, "sucesses": total_success, "total": total_tests, "score": total_score}, "reports" : reports}

