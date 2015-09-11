# -*- coding: utf-8 -*-

import sys
import time

from copy import deepcopy

from collections import OrderedDict
from unittest2 import TestCase, TestResult

from bambou.config import BambouConfig
from bambou.exceptions import BambouHTTPError

from monolithe.courgette.lib.helpers import TestHelper
from monolithe.lib import Printer


class _MonolitheTestResult(TestResult):
    """ A TestResult

    """
    def __init__(self):
        """ Initialized a new result

        """
        TestResult.__init__(self)
        self.tests = OrderedDict()

    def getDescription(self, test):
        """ Get test description

        """
        return str(test).split(' ')[0]  # Removing (package.name)

    def addSuccess(self, test):
        """ Add success to the result

        """
        TestResult.addSuccess(self, test)
        self.tests[self.getDescription(test)] = {'status': 'SUCCESS'}

        Printer.success('OK')

    def addError(self, test, err, connection=None):
        """ Add error to the result

        """
        TestResult.addError(self, test, err)
        self.tests[self.getDescription(test)] = {'status': 'ERROR', 'stacktrace': err, 'connection': connection}

        Printer.warn('ERROR')
        Printer.warn(err[1])
        TestHelper.trace(connection)


    def addFailure(self, test, err, connection):
        """ Add failure to the result

        """
        TestResult.addFailure(self, test, err)
        self.tests[self.getDescription(test)] = {'status': 'FAILURE', 'stacktrace': err, 'connection': connection}

        Printer.warn('Failure')
        Printer.warn(err[1])
        TestHelper.trace(connection)

    def __repr__(self):
        """ Representation

        """
        return "<%s testsRun=%i errors=%i failures=%i>" % \
               (str(self.__class__), self.testsRun, len(self.errors), len(self.failures))


class _MonolitheTestRunner(object):
    """

    """
    def __init__(self):
        """ Initialized """
        pass

    def _makeResult(self):
        """ Return a TestResult implementation

        """
        return _MonolitheTestResult()

    def run(self, test):
        """ Run the given test case or test suite.

        """
        result = self._makeResult()
        startTime = time.time()
        test(result)
        stopTime = time.time()
        timeTaken = stopTime - startTime

        run = result.testsRun
        Printer.log("Ran %d test%s in %.3fs" %
                            (run, run != 1 and "s" or "", timeTaken))

        if not result.wasSuccessful():
            Printer.warn("FAILED (failures=%i, errors=%i)" % (len(result.failures), len(result.errors)))
        else:
            Printer.success("OK")
        return result


class MonolitheTestCase(TestCase):

    _last_connection = None  # Last connection to present errors
    parent = None  # Parent VSD object
    vsdobject = None  # Current VSD object
    user = None  # Current RESTUser

    @property
    def last_connection(self):
        """ Returns last connection """
        return self._last_connection

    @last_connection.setter
    def last_connection(self, connection):
        """ set last_connection """
        self._last_connection = deepcopy(connection)

    # Very Dark Side of unittest... Maybe we should upgrade to unittest2 to do that.
    # Will see that later !
    # CS 05-13-2015
    def run(self, result=None):
        if result is None: result = self.defaultTestResult()
        result.startTest(self)
        testMethod = getattr(self, self._testMethodName)

        try:
            try:
                self.setUp()
                BambouConfig.set_should_raise_bambou_http_error(False)
            except KeyboardInterrupt:
                raise
            except BambouHTTPError as error:
                result.addError(self, [None, u'Test setUp has failed', None], error.connection)
                return
            except:
                result.addError(self, sys.exc_info())
                return
            ok = False
            try:
                Printer.log('%s...' % self._testMethodName)

                testMethod()
                BambouConfig.set_should_raise_bambou_http_error(True)
                ok = True
            except self.failureException:
                result.addFailure(self, sys.exc_info(), self.last_connection)
            except KeyboardInterrupt:
                raise
            except:
                result.addError(self, sys.exc_info(), self.last_connection)
            try:
                self.tearDown()
            except KeyboardInterrupt:
                raise
            except BambouHTTPError as error:
                result.addError(self, [None, u'Test tearDown has failed', None], error.connection)
                return
            except:
                result.addError(self, sys.exc_info())
                ok = False
            if ok: result.addSuccess(self)
        finally:
            result.stopTest(self)

    def assertErrorEqual(self, errors, title, description, remote_name=u'', index=0):
        """ Check if errors received matches

        """
        self.assertEquals(errors[index]['descriptions'][0]['title'], title, 'Expected error title "%s" != "%s"' % (title, errors[index]['descriptions'][0]['title']))
        self.assertEquals(errors[index]['descriptions'][0]['description'], description, 'Expected error description "%s" != "%s"' % (description, errors[index]['descriptions'][0]['description']))
        self.assertEquals(errors[index]['property'], remote_name, 'Expected error property "%s" != "%s"' % (remote_name, errors[index]['property']))

    def assertConnectionStatus(self, connection, expected_status):
        """ Check if the connection has expected status

        """
        message = self._connection_failure_message(connection, expected_status)
        self.assertEquals(connection.response.status_code, expected_status, message)

    # Messages

    def _connection_failure_message(cls, connection, expected_status):
        """ Returns a message that explains the connection status failure """

        return 'Expected status code %s != %s\n' % (expected_status, connection.response.status_code)
