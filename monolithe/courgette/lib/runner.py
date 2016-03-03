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
import logging
from unittest2 import TestSuite

from .sdkloader import SDKLoader
from .maker import GetTestMaker, CreateTestMaker, UpdateTestMaker, DeleteTestMaker, GetAllTestMaker
from .helper import TestHelper
from .testcase import CourgetteTestRunner


class CourgetteTestsRunner(object):
    """ Runner for SDK Objects tests
    """

    def __init__(self, url, username, password, enterprise, version, specification, sdk_identifier, monolithe_config, default_values, parent_resource=None, parent_id=None):
        """ Initializes the CourgetteTestsRunner.

            Args:
                url (string): the server url
                username (string): the username to connect with
                password (string): the password for the username
                enterprise (string): the enterprise
                version (float): the server api version (eg 3.2)
                specification (Specification): the specification representation of the object to test
                parent_resource: the parent_resource if necessary
                parent_id: the parent id if necessary
                sdk: the full name of the SDK to load to run the test suite
                default_values: all default values to have a valid version of the specification

        """
        session_class_name = "%s%sSession" % (monolithe_config.get_option("class_prefix", "transformer"), monolithe_config.get_option("product_accronym"))
        sdk_loader = SDKLoader(version=version, sdk_identifier=sdk_identifier)
        sdk_loader.sdk_utils.set_log_level(logging.DEBUG)

        self._helper = TestHelper(sdk_module=sdk_loader.sdk,
                                  sdk_session_class_name=session_class_name,
                                  api_url=url, api_username=username,
                                  api_password=password,
                                  api_enterprise=enterprise)

        self._sdk_object = sdk_loader.get_instance_from_rest_name(specification.rest_name)
        self._sdk_object.from_dict(default_values)
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

        # as we get one single spec, we can't know the parent info...
        self._create_allowed = True
        self._get_all_allowed = True

        # for api in specification.parent_apis:
        #     self._create_allowed = api.allows_create
        #     self._get_all_allowed = api.allows_get

        self._update_allowed = specification.allows_update
        self._delete_allowed = specification.allows_delete
        self._get_allowed = specification.allows_get

    def suite(self):
        """ Returns a TestSuite that can be run
            TestSuite is computed according to what is defined in the specification
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
