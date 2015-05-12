# -*- coding: utf-8 -*-

import re

from .printer import Printer
from .factory import VSDKFactory
from unittest import TestCase, TestSuite, TextTestRunner

from bambou.config import BambouConfig

HTTP_METHOD_POST = 'POST'
HTTP_METHOD_GET = 'GET'
HTTP_METHOD_DELETE = 'DELETE'
HTTP_METHOD_UPDATE = 'UPDATE'


class TestMaker(object):
    """ Make tests

    """
    def __init__(self):
        """ Initializes a TestMaker

        """
        self._object_registry = dict()
        self._attributes_registry = dict()

    def register_test(self, function_name, **conditions):
        """ Register test for all attributes

        """
        if function_name not in self._object_registry:
            self._object_registry[function_name] = conditions

    def register_test_for_attribute(self, function_name, **conditions):
        """ Register an attribute test for all given conditions

        """
        if function_name not in self._attributes_registry:
            self._attributes_registry[function_name] = conditions

    def does_attribute_meet_condition(self, attribute, conditions):
        """ Check if the attribute meet all the given conditions

            Args:
                attribute: the attribute information
                conditions: a dictionary of condition to match

            Returns:
                True if the attribute match all conditions. False otherwise
        """
        if conditions is None or len(conditions) == 0:
            return True

        for attribute_name, attribute_value in conditions.iteritems():
            value = getattr(attribute, attribute_name, False)
            if value != attribute_value and bool(value) != attribute_value:
                return False

        return True

    def make_tests(self, vsdobject, testcase):
        """ Make all tests that should be run for the given object in the specified testcase

            Args:
                vsdobject: the vsd object
                testcase: the test case

            Returns:
                It returns a dictionary of all tests to run

        """
        tests = dict()
        attributes = vsdobject.get_attributes()

        for attribute in attributes:
            for function_name, conditions in self._attributes_registry.iteritems():
                if self.does_attribute_meet_condition(attribute, conditions):
                    (test_name, test_func) = self._create_test(testcase=testcase, vsdobject=vsdobject, function_name=function_name, attribute=attribute)
                    tests[test_name] = test_func

        for function_name, infos in self._object_registry.iteritems():
            (test_name, test_func) = self._create_test(testcase=testcase, vsdobject=vsdobject, function_name=function_name)
            tests[test_name] = test_func

        Printer.log("------ ALL TESTS:\n%s" % tests.keys())
        return tests

    def _create_test(self, testcase, function_name, vsdobject, attribute=None):
        """ Create a test method for the vsdoject

            Args:
                testcase: the testcase to that should manage the method
                function_name: the name of the method in the testcase
                vsdobject: the object that should be tested
                attribute: the attribute information if necessary

            Returns:
                It returns a tuple (name, method) that represents the test method

        """
        func = getattr(testcase, function_name)
        object_name = vsdobject.rest_name

        # Name that will be displayed
        test_name = ''
        rep = dict()
        rep["object"] = object_name

        if attribute:
            rep["attribute"] = attribute.local_name

        rep = dict((re.escape(k), v) for k, v in rep.iteritems())
        pattern = re.compile("|".join(rep.keys()))

        if function_name.startswith('_'):
            function_name = function_name[1:]

        test_name = pattern.sub(lambda m: rep[re.escape(m.group(0))], function_name)

        # Prepare and add test method to test suite
        test_func = None

        if attribute:
            test_func = lambda self, attribute=attribute: func(self, attribute)
        else:
            test_func = lambda self: func(self)

        test_func.__name__ = str(test_name)

        return (test_name, test_func)


class CreateTestMaker(TestMaker):
    """ TestCase for create objects

    """
    def __init__(self, parent, vsdobject):
        """ Initializes a test case for creating objects

        """
        super(CreateTestMaker, self).__init__()
        self.parent = parent
        self.vsdobject = vsdobject

        # Object tests
        self.register_test('_test_create_object_in_parent_with_all_valid_attributes_should_succeed')
        self.register_test('_test_create_object_with_dummy_test')

        # Attribute tests
        # self.register_test_for_attribute('test_create_object_in_parent_with_all_valid_attributes_should_succeed')

    def test_suite(self):
        """ Inject generated tests

        """
        CreateTestCase.parent = self.parent
        CreateTestCase.vsdobject = self.vsdobject

        tests = self.make_tests(vsdobject=self.vsdobject, testcase=CreateTestCase)
        for test_name, test_func in tests.iteritems():
            setattr(CreateTestCase, test_name, test_func)

        return TestSuite(map(CreateTestCase, tests))


class CreateTestCase(TestCase):

    parent = None
    vsdobject = None

    def setUp(self):
        """ Setting up create test

        """
        pass

    def tearDown(self):
        """ Clean up environment

        """
        if self.vsdobject and self.vsdobject.id:
            self.vsdobject.delete()

    def _test_create_object_in_parent_with_all_valid_attributes_should_succeed(self):
        """ Create an object with all its valid attributes should always succeed with 201 response

        """
        Printer.warn('Creating %s' % self.vsdobject.rest_name)
        Printer.json(self.vsdobject.to_dict())
        (obj, connection) = self.parent.create_child(self.vsdobject)

        Printer.warn(connection.response.errors)

        self.assertEquals(connection.response.status_code, 201)
        self.assertEquals(obj.to_dict(), self.vsdobject.to_dict())

    def _test_create_object_with_dummy_test(self):
        """ This is a dummy test

        """
        self.assertEquals(True, True)


class TestsRunner(object):
    """ Runner for VSD Objects tests

    """
    def __init__(self, vsdurl, username, password, enterprise, version, spec, parent_resource=None, parent_id=None, **attributes):
        """ Initializes the TestsRunner.

            Args:
                vsdurl (string): the vsd url
                username (string): the username to connect with
                password (string): the password for the username
                enterprise (string): the enterprise
                version (float): the vsd api version (eg 3.2)
                spec (dict): the JSON representation of the specification
                parent_resource: the parent_resource if necessary
                parent_id: the parent id if necessary
                attributes: all attributes to have a valid version of the spec

        """
        VSDKFactory.init(version)
        vsdk = VSDKFactory.get_vsdk_package(version)

        session = vsdk.NUVSDSession(api_url=vsdurl, username=username, password=password, enterprise=enterprise, version=version)
        session.start()

        self.spec = spec
        self.resource_name = spec['model']['resourceName']
        self.vsdobject = VSDKFactory.get_instance(self.resource_name, **attributes)
        self.parent = None

        if parent_resource and parent_id:
            try:
                self.parent = VSDKFactory.get_instance(parent_resource, id=parent_id)
                self.parent.fetch()
            except:
                Printer.raiseError('Could not find parent %s with ID=%s' % (parent_resource, parent_id))

        self.is_create_allowed = False
        self.is_delete_allowed = False
        self.is_get_allowed = False
        self.is_get_all_allowed = False
        self.is_update_allowed = False

        for path, api in self.spec['apis']['parents'].iteritems():
            for operation in api['operations']:
                method = operation['method']
                if method == HTTP_METHOD_POST:
                    self.is_create_allowed = True
                elif method == HTTP_METHOD_GET:
                    self.is_get_all_allowed = True

        # Self is not present here... :( Find another way !
        # for path, api in self.spec['apis']['self'].iteritems():
        #     for operation in api['operations']:
        #         method = operation['method']
        #         if method == HTTP_METHOD_GET:
        #             self.is_get_allowed = True
        #         elif method == HTTP_METHOD_UPDATE:
        #             self.is_update_allowed = True
        #         elif method == HTTP_METHOD_DELETE:
        #             self.is_delete_allowed = True
        #         elif method == HTTP_METHOD_POST:
        #             self.is_create_allowed = True

        Printer.log('---------------------------------')
        Printer.log('parent = %s' % self.parent)
        Printer.log('vsdobject = %s' % self.vsdobject)
        Printer.log('resource_name = %s' % self.resource_name)
        Printer.log('is_create_allowed = %s' % self.is_create_allowed)
        Printer.log('is_delete_allowed = %s' % self.is_delete_allowed)
        Printer.log('is_get_allowed = %s' % self.is_get_allowed)
        Printer.log('is_get_all_allowed = %s' % self.is_get_all_allowed)
        Printer.log('is_update_allowed = %s' % self.is_update_allowed)
        Printer.log('---------------------------------')

    def test_suite(self):
        """ Returns a TestSuite that can be run

            TestSuite is computed according to what is defined in the spec

        """
        suite = None
        if self.is_create_allowed:
            maker = CreateTestMaker(self.parent, self.vsdobject)
            suite = maker.test_suite()

        # Do the same of update and delete.. and combine suites

        return suite

    def run(self):
        """ Runs all tests on the specified VSD

        """
        BambouConfig.set_should_raise_bambou_http_error(False)

        import logging
        bambou_logger = logging.getLogger('bambou')
        bambou_logger.setLevel(logging.INFO)

        suite = self.test_suite()
        results = TextTestRunner().run(suite)

        BambouConfig.set_should_raise_bambou_http_error(True)
        return results
