# -*- coding: utf-8 -*-

from unittest2 import TestSuite

from monolithe.lib import SDKLoader
from monolithe.lib import SDKUtils

from .maker import GetTestMaker, CreateTestMaker, UpdateTestMaker, DeleteTestMaker, GetAllTestMaker
from .helper import TestHelper
from .testcase import CourgetteCourgetteTestsRunner




class CourgetteTestsRunner(object):
    """ Runner for VSD Objects tests

    """

    def __init__(self, vsdurl, username, password, enterprise, version, model, parent_resource=None, parent_id=None, sdk_identifier=None, **default_values):
        """ Initializes the CourgetteTestsRunner.

            Args:
                vsdurl (string): the vsd url
                username (string): the username to connect with
                password (string): the password for the username
                enterprise (string): the enterprise
                version (float): the vsd api version (eg 3.2)
                model (Model): the model representation of the object to test
                parent_resource: the parent_resource if necessary
                parent_id: the parent id if necessary
                sdk: the full name of the SDK to load to run the test suite
                default_values: all default values to have a valid version of the model

        """
        SDKLoader.init(version)
        sdk = SDKLoader.get_sdk_package(sdk_identifier=sdk_identifier)
        TestHelper.use_sdk(sdk)

        session = sdk.NUVSDSession(api_url=vsdurl, username=username, password=password, enterprise=enterprise)
        session.start()

        self.user = session.user
        self.resource_name = model.resource_name

        python_attributes = {SDKUtils.get_python_name(name): value for name, value in default_values.iteritems()}
        self.vsdobject = SDKLoader.get_instance_from_model(model, **python_attributes)

        self.parent = None

        if parent_resource and parent_id:
            try:
                self.parent = SDKLoader.get_instance(parent_resource, id=parent_id)
                self.parent.fetch()
            except:
                raise AttributeError('Could not find parent %s with ID=%s' % (parent_resource, parent_id))

        SDKLoader.update_fetchers_for_object(self.parent, self.vsdobject, model)

        self.is_create_allowed = False
        self.is_delete_allowed = False
        self.is_get_allowed = False
        self.is_get_all_allowed = False
        self.is_update_allowed = False

        for api in model.parent_apis:
            for operation in api.operations:
                method = operation.method

                if method == 'POST':
                    self.is_create_allowed = True
                elif method == 'GET':
                    self.is_get_all_allowed = True

        for api in model.self_apis:
            for operation in api.operations:
                method = operation.method

                if method == 'PUT':
                    self.is_update_allowed = True
                elif method == 'DELETE':
                    self.is_delete_allowed = True
                elif method == 'GET':
                    self.is_get_allowed = True

    def suite(self):
        """ Returns a TestSuite that can be run

            TestSuite is computed according to what is defined in the model

        """
        all_suites = TestSuite()

        if self.is_create_allowed:
            maker = CreateTestMaker(self.parent, self.vsdobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self.is_update_allowed:
            maker = UpdateTestMaker(self.parent, self.vsdobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self.is_delete_allowed:
            maker = DeleteTestMaker(self.parent, self.vsdobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self.is_get_allowed:
            maker = GetTestMaker(self.parent, self.vsdobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        if self.is_get_all_allowed:
            maker = GetAllTestMaker(self.parent, self.vsdobject, self.user)
            suite = maker.suite()
            all_suites.addTests(suite)

        return all_suites

    def run(self):
        """ Runs all tests on the specified VSD

        """
        suite = self.suite()
        results = CourgetteCourgetteTestsRunner().run(suite)

        return results
