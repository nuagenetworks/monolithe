# -*- coding: utf-8 -*-

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
        self.monolithe_config = monolithe_config
        self._sdk_class_prefix = self.monolithe_config.get_option("sdk_class_prefix", "sdk")
        self.session_class_name = "%s%sSession" % (self._sdk_class_prefix, self.monolithe_config.get_option("product_accronym"))

        SDKLoader.init(version)
        sdk = SDKLoader.get_sdk_package(sdk_identifier=sdk_identifier, sdk_class_prefix=self._sdk_class_prefix)
        TestHelper.use_sdk(sdk, self.session_class_name)

        session = getattr(sdk, self.session_class_name)(api_url=url, username=username, password=password, enterprise=enterprise)
        session.start()

        self.user = session.user
        self.resource_name = model.resource_name

        python_attributes = {SDKUtils.get_python_name(name): value for name, value in default_values.iteritems()}
        self.sdkobject = SDKLoader.get_instance_from_model(model, self._sdk_class_prefix, **python_attributes)

        self.parent = None

        if parent_resource and parent_id:
            try:
                self.parent = SDKLoader.get_instance(parent_resource, id=parent_id)
                self.parent.fetch()
            except:
                raise AttributeError("Could not find parent %s with ID=%s" % (parent_resource, parent_id))

        SDKLoader.update_fetchers_for_object(self.parent, self.sdkobject, self._sdk_class_prefix, model)

        self.is_create_allowed = False
        self.is_delete_allowed = False
        self.is_get_allowed = False
        self.is_get_all_allowed = False
        self.is_update_allowed = False

        for api in model.parent_apis:
            for operation in api.operations:
                method = operation.method

                if method == "POST":
                    self.is_create_allowed = True
                elif method == "GET":
                    self.is_get_all_allowed = True

        for api in model.self_apis:
            for operation in api.operations:
                method = operation.method

                if method == "PUT":
                    self.is_update_allowed = True
                elif method == "DELETE":
                    self.is_delete_allowed = True
                elif method == "GET":
                    self.is_get_allowed = True

    def suite(self):
        """ Returns a TestSuite that can be run

            TestSuite is computed according to what is defined in the model

        """
        all_suites = TestSuite()

        if self.is_create_allowed:
            maker = CreateTestMaker(self.parent, self.sdkobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self.is_update_allowed:
            maker = UpdateTestMaker(self.parent, self.sdkobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self.is_delete_allowed:
            maker = DeleteTestMaker(self.parent, self.sdkobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self.is_get_allowed:
            maker = GetTestMaker(self.parent, self.sdkobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self.is_get_all_allowed:
            maker = GetAllTestMaker(self.parent, self.sdkobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        return all_suites

    def run(self):
        """ Runs all tests on the specified SDK

        """
        suite = self.suite()
        results = CourgetteTestRunner().run(suite)

        return results
