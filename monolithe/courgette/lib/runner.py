# -*- coding: utf-8 -*-

import logging

from unittest2 import TestSuite

from monolithe.lib import SDKLoader
from monolithe.lib import SDKUtils

from .maker import GetTestMaker, CreateTestMaker, UpdateTestMaker, DeleteTestMaker, GetAllTestMaker
from .helper import TestHelper
from .testcase import CourgetteTestRunner




class CourgetteTestsRunner(object):
    """ Runner for SDK Objects tests

    """

    def __init__(self, url, username, password, enterprise, version, model, sdk_identifier, monolithe_config, parent_resource=None, parent_id=None, **default_values):
        """ Initializes the CourgetteTestsRunner.

            Args:
                url (string): the server url
                username (string): the username to connect with
                password (string): the password for the username
                enterprise (string): the enterprise
                version (float): the server api version (eg 3.2)
                model (Model): the model representation of the object to test
                parent_resource: the parent_resource if necessary
                parent_id: the parent id if necessary
                sdk: the full name of the SDK to load to run the test suite
                default_values: all default values to have a valid version of the model

        """
        session_class_name = "%s%sSession" % (monolithe_config.get_option("sdk_class_prefix", "sdk"), monolithe_config.get_option("product_accronym"))
        sdk_loader = SDKLoader(version=version, sdk_identifier=sdk_identifier)
        sdk_loader.sdk_utils.set_log_level(logging.DEBUG)

        self._helper = TestHelper(  sdk_module=sdk_loader.sdk,
                                    sdk_session_class_name=session_class_name,
                                    api_url=url, api_username=username,
                                    api_password=password,
                                    api_enterprise=enterprise)

        self._sdk_object = sdk_loader.get_instance_from_rest_name(model.remote_name)

        self._sdk_object.from_dict({SDKUtils.get_python_name(name): value for name, value in default_values.iteritems()})
        self._sdk_parent_object = None


        if parent_resource and parent_id:
            try:
                self._sdk_parent_object = sdk_loader.get_instance_from_rest_name(parent_resource)
                self._sdk_parent_object.id = parent_id
                self._sdk_parent_object.fetch()
            except:
                raise AttributeError("Could not find parent %s with ID=%s" % (parent_resource, parent_id))
        else:
            self._sdk_parent_object = self._helper.root_object

        self._create_allowed = False
        self._delete_allowed = False
        self._get_allowed = False
        self._get_all_allowed = False
        self._update_allowed = False

        for api in model.parent_apis:
            for operation in api.operations:
                if operation.method == "POST":
                    self._create_allowed = True
                if operation.method == "GET":
                    self._get_all_allowed = True

        for api in model.self_apis:
            for operation in api.operations:
                if operation.method == "PUT":
                    self._update_allowed = True
                if operation.method == "DELETE":
                    self._delete_allowed = True
                if operation.method == "GET":
                    self._get_allowed = True

    def suite(self):
        """ Returns a TestSuite that can be run

            TestSuite is computed according to what is defined in the model

        """
        all_suites = TestSuite()

        if self._create_allowed:
            maker = CreateTestMaker(self._sdk_parent_object, self._sdk_object, self._helper)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self._update_allowed:
            maker = UpdateTestMaker(self._sdk_parent_object, self._sdk_object, self._helper)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self._delete_allowed:
            maker = DeleteTestMaker(self._sdk_parent_object, self._sdk_object, self._helper)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self._get_allowed:
            maker = GetTestMaker(self._sdk_parent_object, self._sdk_object, self._helper)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self._get_all_allowed:
            maker = GetAllTestMaker(self._sdk_parent_object, self._sdk_object, self._helper)
            suite = maker.suite()
            all_suites.addTests(suite)

        return all_suites

    def run(self):
        """ Runs all tests on the specified SDK

        """
        suite = self.suite()
        results = CourgetteTestRunner().run(suite)

        return results
