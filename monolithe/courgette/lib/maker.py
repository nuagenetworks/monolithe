# -*- coding: utf-8 -*-

import re

from unittest2 import TestSuite

from monolithe.lib import SDKLoader

from .helper import TestHelper
from .testcase import CourgetteTestCase



class _TestMaker(object):
    """ Make tests

    """

    IGNORED_ATTRIBUTES = ['id', 'parent_id', 'parent_type', 'creation_date', 'owner', 'last_updated_date', 'last_updated_by', 'external_id']

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

    def make_tests(self, sdkobject, testcase):
        """ Make all tests that should be run for the given object in the specified testcase

            Args:
                sdkobject: the sdk object
                testcase: the test case

            Returns:
                It returns a dictionary of all tests to run

        """
        tests = dict()
        attributes = sdkobject.get_attributes()

        for attribute in attributes:

            if attribute.local_name in self.IGNORED_ATTRIBUTES:
                continue

            for function_name, conditions in self._attributes_registry.iteritems():
                if self.does_attribute_meet_condition(attribute, conditions):
                    (test_name, test_func) = self._create_test(testcase=testcase, sdkobject=sdkobject, function_name=function_name, attribute=attribute)
                    tests[test_name] = test_func

        for function_name, infos in self._object_registry.iteritems():
            (test_name, test_func) = self._create_test(testcase=testcase, sdkobject=sdkobject, function_name=function_name)
            tests[test_name] = test_func

        return tests

    def _create_test(self, testcase, function_name, sdkobject, attribute=None):
        """ Create a test method for the sdkoject

            Args:
                testcase: the testcase to that should manage the method
                function_name: the name of the method in the testcase
                sdkobject: the object that should be tested
                attribute: the attribute information if necessary

            Returns:
                It returns a tuple (name, method) that represents the test method

        """
        func = getattr(testcase, function_name)
        object_name = sdkobject.rest_name

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



##### CREATE TESTS
class CreateTestMaker(_TestMaker):
    """ TestCase for create objects

    """
    def __init__(self, parent, sdkobject, user):
        """ Initializes a test case for creating objects

        """
        super(CreateTestMaker, self).__init__()
        self.parent = parent
        self.sdkobject = sdkobject
        self.user = user

        # Object tests
        self.register_test('_test_create_object_with_all_valid_attributes_should_succeed')
        self.register_test('_test_create_object_without_authentication_should_fail')

        # Attribute tests
        self.register_test_for_attribute('_test_create_object_with_required_attribute_as_none_should_fail', is_required=True)
        self.register_test_for_attribute('_test_create_object_with_attribute_not_in_allowed_choices_list_should_fail', has_choices=True)
        self.register_test_for_attribute('_test_create_object_with_attribute_as_none_should_succeed', is_required=False)

    def suite(self):
        """ Inject generated tests

        """
        CreateTestCase.parent = self.parent
        CreateTestCase.sdkobject = self.sdkobject
        CreateTestCase.user = self.user

        tests = self.make_tests(sdkobject=self.sdkobject, testcase=CreateTestCase)
        for test_name, test_func in tests.iteritems():
            setattr(CreateTestCase, test_name, test_func)

        return TestSuite(map(CreateTestCase, tests))


class CreateTestCase(CourgetteTestCase):

    def __init__(self, methodName='runTest'):
        """ Initialize

        """
        CourgetteTestCase.__init__(self, methodName)
        self.pristine_sdkobject = SDKLoader.get_instance_copy(self.sdkobject)

    def setUp(self):
        """ Setting up create test

        """
        self.last_connection = None
        self.sdkobject = SDKLoader.get_instance_copy(self.pristine_sdkobject)

    def tearDown(self):
        """ Clean up environment

        """
        if self.sdkobject and self.sdkobject.id:
            self.sdkobject.delete()
            self.sdkobject.id = None

    # Objects tests
    def _test_create_object_without_authentication_should_fail(self):
        """ Create an object without authentication """

        TestHelper.set_api_key(None)
        (obj, connection) = self.parent.create_child(self.sdkobject)
        self.last_connection = connection
        TestHelper.set_api_key(self.user.api_key)

        self.assertConnectionStatus(connection, 401)

    def _test_create_object_with_all_valid_attributes_should_succeed(self):
        """ Create an object with all its valid attributes should always succeed with 201 response

        """
        (obj, connection) = self.parent.create_child(self.sdkobject)
        self.last_connection = connection

        self.assertConnectionStatus(connection, 201)
        self.assertEquals(obj.to_dict(), self.sdkobject.to_dict())

    # Attributes tests
    def _test_create_object_with_required_attribute_as_none_should_fail(self, attribute):
        """ Create an object with a required attribute as None """

        setattr(self.sdkobject, attribute.local_name, None)
        (obj, connection) = self.parent.create_child(self.sdkobject)
        self.last_connection = connection

        self.assertConnectionStatus(connection, 409)
        self.assertErrorEqual(connection.response.errors, title=u'Invalid input', description=u'This value is mandatory.', remote_name=attribute.remote_name)

    def _test_create_object_with_attribute_as_none_should_succeed(self, attribute):
        """ Create an objet with an attribute as none """

        setattr(self.sdkobject, attribute.local_name, None)
        (obj, connection) = self.parent.create_child(self.sdkobject)
        self.last_connection = connection

        self.assertConnectionStatus(connection, 201)
        # self.assertIsNone(getattr(obj, attribute.local_name), '%s should be none but was %s instead' % (attribute.local_name, getattr(obj, attribute.local_name)))

    def _test_create_object_with_attribute_not_in_allowed_choices_list_should_fail(self, attribute):
        """ Create an object with a wrong choice attribute """

        setattr(self.sdkobject, attribute.local_name, u'A random value')
        (obj, connection) = self.parent.create_child(self.sdkobject)
        self.last_connection = connection

        self.assertConnectionStatus(connection, 409)
        self.assertErrorEqual(connection.response.errors, title=u'Invalid input', description=u'Invalid input', remote_name=attribute.remote_name)



##### UPDATE TESTS
class UpdateTestMaker(_TestMaker):
    """ TestCase for updating objects

    """
    def __init__(self, parent, sdkobject, user):
        """ Initializes a test case for updating objects

        """
        super(UpdateTestMaker, self).__init__()
        self.parent = parent
        self.sdkobject = sdkobject
        self.user = user

        # Object tests
        self.register_test('_test_update_object_with_same_attributes_should_fail')
        self.register_test('_test_update_object_without_authentication_should_fail')

        # Attribute tests
        self.register_test_for_attribute('_test_update_object_with_attribute_not_in_allowed_choices_list_should_fail', has_choices=True)
        self.register_test_for_attribute('_test_update_object_with_required_attribute_as_none_should_fail', is_required=True)
        self.register_test_for_attribute('_test_update_object_with_attribute_as_none_should_succeed', is_required=False)
        # self.register_test_for_attribute('_test_update_object_with_attribute_with_choices_as_none_should_fail', has_choices=True)

    def suite(self):
        """ Inject generated tests

        """
        UpdateTestCase.parent = self.parent
        UpdateTestCase.sdkobject = self.sdkobject
        UpdateTestCase.user = self.user

        tests = self.make_tests(sdkobject=self.sdkobject, testcase=UpdateTestCase)
        for test_name, test_func in tests.iteritems():
            setattr(UpdateTestCase, test_name, test_func)

        return TestSuite(map(UpdateTestCase, tests))


class UpdateTestCase(CourgetteTestCase):

    def __init__(self, methodName='runTest'):
        """ Initialize

        """
        CourgetteTestCase.__init__(self, methodName)
        self.pristine_sdkobject = SDKLoader.get_instance_copy(self.sdkobject)

    def setUp(self):
        """ Setting up create test

        """
        self.last_connection = None
        self.sdkobject = SDKLoader.get_instance_copy(self.pristine_sdkobject)

        self.parent.create_child(self.sdkobject)

    def tearDown(self):
        """ Clean up environment

        """
        self.sdkobject.delete()

    # Objects tests
    def _test_update_object_without_authentication_should_fail(self):
        """ Update an object without authentication """

        TestHelper.set_api_key(None)
        (obj, connection) = self.sdkobject.save()
        self.last_connection = connection
        TestHelper.set_api_key(self.user.api_key)

        self.assertConnectionStatus(connection, 401)

    def _test_update_object_with_same_attributes_should_fail(self):
        """ Update an object with same attributes should always fail with 409 error

        """
        (obj, connection) = self.sdkobject.save()
        self.last_connection = connection

        self.assertConnectionStatus(connection, 409)
        self.assertErrorEqual(connection.response.errors, title=u'No changes to modify the entity', description=u'There are no attribute changes to modify the entity.')

    # Attributes tests
    def _test_update_object_with_required_attribute_as_none_should_fail(self, attribute):
        """ Update an object with a required attribute as None """

        setattr(self.sdkobject, attribute.local_name, None)
        (obj, connection) = self.sdkobject.save()
        self.last_connection = connection

        self.assertConnectionStatus(connection, 409)
        self.assertErrorEqual(connection.response.errors, title=u'Invalid input', description=u'This value is mandatory.', remote_name=attribute.remote_name)

    def _test_update_object_with_attribute_with_choices_as_none_should_fail(self, attribute):
        """ Update an objet with an attribute with choices as none should fail """

        setattr(self.sdkobject, attribute.local_name, None)
        (obj, connection) = self.sdkobject.save()
        self.last_connection = connection

        self.assertConnectionStatus(connection, 409)
        # self.assertIsNone(getattr(obj, attribute.local_name), '%s should be none but was %s instead' % (attribute.local_name, getattr(obj, attribute.local_name)))

    def _test_update_object_with_attribute_not_in_allowed_choices_list_should_fail(self, attribute):
        """ Update an object with a wrong choice attribute """

        setattr(self.sdkobject, attribute.local_name, u'A random value')
        (obj, connection) = self.sdkobject.save()
        self.last_connection = connection

        self.assertConnectionStatus(connection, 409)
        self.assertErrorEqual(connection.response.errors, title=u'Invalid input', description=u'Invalid input', remote_name=attribute.remote_name)

    def _test_update_object_with_attribute_as_none_should_succeed(self, attribute):
        """ Update an objet with an attribute as none """

        setattr(self.sdkobject, attribute.local_name, None)
        (obj, connection) = self.sdkobject.save()
        self.last_connection = connection

        self.assertConnectionStatus(connection, 200)
        self.assertIsNone(getattr(obj, attribute.local_name), '%s should be none but was %s instead' % (attribute.local_name, getattr(obj, attribute.local_name)))




##### DELETE TESTS
class DeleteTestMaker(_TestMaker):
    """ TestCase for create objects

    """
    def __init__(self, parent, sdkobject, user):
        """ Initializes a test case for creating objects

        """
        super(DeleteTestMaker, self).__init__()
        self.parent = parent
        self.sdkobject = sdkobject
        self.user = user

        # Object tests
        self.register_test('_test_delete_object_without_authentication_should_fail')
        self.register_test('_test_delete_object_with_valid_id_should_succeed')
        self.register_test('_test_delete_object_with_wrong_id_should_succeed')

        # No Attribute tests

    def suite(self):
        """ Inject generated tests

        """
        DeleteTestCase.parent = self.parent
        DeleteTestCase.sdkobject = self.sdkobject
        DeleteTestCase.user = self.user

        tests = self.make_tests(sdkobject=self.sdkobject, testcase=DeleteTestCase)
        for test_name, test_func in tests.iteritems():
            setattr(DeleteTestCase, test_name, test_func)

        return TestSuite(map(DeleteTestCase, tests))


class DeleteTestCase(CourgetteTestCase):

    def __init__(self, methodName='runTest'):
        """ Initialize

        """
        CourgetteTestCase.__init__(self, methodName)
        self.pristine_sdkobject = SDKLoader.get_instance_copy(self.sdkobject)

    def setUp(self):
        """ Setting up create test

        """
        self.last_connection = None
        self.sdkobject = SDKLoader.get_instance_copy(self.pristine_sdkobject)

        self.parent.create_child(self.sdkobject)

    def tearDown(self):
        """ Clean up environment

        """
        if self.sdkobject.id is not None:
            self.sdkobject.delete()

    # Objects tests
    def _test_delete_object_without_authentication_should_fail(self):
        """ Delete an object without authentication """

        TestHelper.set_api_key(None)
        (obj, connection) = self.sdkobject.delete()
        self.last_connection = connection

        TestHelper.set_api_key(self.user.api_key)

        self.assertConnectionStatus(connection, 401)

    def _test_delete_object_with_valid_id_should_succeed(self):
        """ Delete an object with its id should always succeed with 204 response

        """
        (obj, connection) = self.sdkobject.delete()
        self.last_connection = connection

        self.assertConnectionStatus(connection, 204)
        self.assertEquals(obj.to_dict(), self.sdkobject.to_dict())

    def _test_delete_object_with_wrong_id_should_succeed(self):
        """ Delete an object with a wrong id should fail with 404 error

        """
        default_id = self.sdkobject.id
        invalid_id = u'Unknown ID'
        self.sdkobject.id = invalid_id
        (obj, connection) = self.sdkobject.delete()
        self.last_connection = connection

        self.sdkobject.id = default_id

        self.assertConnectionStatus(connection, 404)
        self.assertErrorEqual(connection.response.errors, title=u'%s not found' % self.sdkobject.rest_name, description=u'Cannot find %s with ID %s' % (self.sdkobject.rest_name, invalid_id))

    # No Attributes tests



##### GET TESTS
class GetTestMaker(_TestMaker):
    """ TestCase for create objects

    """
    def __init__(self, parent, sdkobject, user):
        """ Initializes a test case for creating objects

        """
        super(GetTestMaker, self).__init__()
        self.parent = parent
        self.sdkobject = sdkobject
        self.user = user

        # Object tests
        self.register_test('_test_get_object_without_authentication_should_fail')
        self.register_test('_test_get_object_with_valid_id_should_succeed')
        self.register_test('_test_get_object_with_wrong_id_should_succeed')

        # No Attribute tests

    def suite(self):
        """ Inject generated tests

        """
        GetTestCase.parent = self.parent
        GetTestCase.sdkobject = self.sdkobject
        GetTestCase.user = self.user

        tests = self.make_tests(sdkobject=self.sdkobject, testcase=GetTestCase)
        for test_name, test_func in tests.iteritems():
            setattr(GetTestCase, test_name, test_func)

        return TestSuite(map(GetTestCase, tests))


class GetTestCase(CourgetteTestCase):

    def __init__(self, methodName='runTest'):
        """ Initialize

        """
        CourgetteTestCase.__init__(self, methodName)
        self.pristine_sdkobject = SDKLoader.get_instance_copy(self.sdkobject)

    def setUp(self):
        """ Setting up get test

        """
        self.last_connection = None
        self.sdkobject = SDKLoader.get_instance_copy(self.pristine_sdkobject)

        self.parent.create_child(self.sdkobject)

    def tearDown(self):
        """ Clean up environment

        """
        self.sdkobject.delete()

    # Objects tests
    def _test_get_object_without_authentication_should_fail(self):
        """ Get an object without authentication """

        TestHelper.set_api_key(None)
        (obj, connection) = self.sdkobject.fetch()
        self.last_connection = connection

        TestHelper.set_api_key(self.user.api_key)

        self.assertConnectionStatus(connection, 401)

    def _test_get_object_with_valid_id_should_succeed(self):
        """ Get an object with its id should always succeed with 204 response

        """
        (obj, connection) = self.sdkobject.fetch()
        self.last_connection = connection

        self.assertConnectionStatus(connection, 200)
        self.assertEquals(obj.to_dict(), self.sdkobject.to_dict())

    def _test_get_object_with_wrong_id_should_succeed(self):
        """ Get an object with a wrong id should fail with 404 error

        """
        default_id = self.sdkobject.id
        invalid_id = u'Unknown ID'
        self.sdkobject.id = invalid_id
        (obj, connection) = self.sdkobject.fetch()
        self.last_connection = connection

        self.sdkobject.id = default_id

        self.assertConnectionStatus(connection, 404)
        self.assertErrorEqual(connection.response.errors, title=u'%s not found' % self.sdkobject.rest_name, description=u'Cannot find %s with ID %s' % (self.sdkobject.rest_name, invalid_id))

    # No Attributes tests





##### GETALL TESTS
class GetAllTestMaker(_TestMaker):
    """ TestCase for create objects

    """
    def __init__(self, parent, sdkobject, user):
        """ Initializes a test case for creating objects

        """
        super(GetAllTestMaker, self).__init__()
        self.parent = parent
        self.sdkobject = sdkobject
        self.user = user

        # Object tests
        self.register_test('_test_get_all_objects_without_authentication_should_fail')
        self.register_test('_test_get_all_objects_without_content_should_success')
        self.register_test('_test_get_all_objects_with_content_should_success')

        # No Attribute tests

    def suite(self):
        """ Inject generated tests

        """
        GetAllTestCase.parent = self.parent
        GetAllTestCase.sdkobject = self.sdkobject
        GetAllTestCase.user = self.user

        tests = self.make_tests(sdkobject=self.sdkobject, testcase=GetAllTestCase)
        for test_name, test_func in tests.iteritems():
            setattr(GetAllTestCase, test_name, test_func)

        return TestSuite(map(GetAllTestCase, tests))


class GetAllTestCase(CourgetteTestCase):

    def __init__(self, methodName='runTest'):
        """ Initialize

        """
        CourgetteTestCase.__init__(self, methodName)
        self.pristine_sdkobject = SDKLoader.get_instance_copy(self.sdkobject)

    def setUp(self):
        """ Setting up get test

        """
        self.last_connection = None
        self.sdkobject = SDKLoader.get_instance_copy(self.pristine_sdkobject)

    def tearDown(self):
        """ Clean up environment

        """
        pass

    # Objects tests
    def _test_get_all_objects_without_authentication_should_fail(self):
        """ Get all object without authentication """

        TestHelper.set_api_key(None)
        fetcher = SDKLoader.get_fetcher_instance(self.parent, self.sdkobject)
        (fetcher, parent, children) = fetcher.fetch()
        connection = fetcher.current_connection

        self.last_connection = connection

        TestHelper.set_api_key(self.user.api_key)

        self.assertConnectionStatus(connection, 401)

    def _test_get_all_objects_without_content_should_success(self):
        """ Get all object without content should succeed with 200 response

        """
        fetcher = SDKLoader.get_fetcher_instance(self.parent, self.sdkobject)
        (fetcher, parent, children) = fetcher.fetch()
        connection = fetcher.current_connection
        self.last_connection = connection

        self.assertConnectionStatus(connection, 200)

    def _test_get_all_objects_with_content_should_success(self):
        """ Get all object with content should succeed with 200 response

        """
        self.parent.create_child(self.sdkobject)

        fetcher = SDKLoader.get_fetcher_instance(self.parent, self.sdkobject)
        (fetcher, parent, children) = fetcher.fetch()
        connection = fetcher.current_connection

        self.last_connection = connection
        self.sdkobject.delete()

        self.assertConnectionStatus(connection, 200)

    # Attributes tests
    # Filter, Order, Page etc.
