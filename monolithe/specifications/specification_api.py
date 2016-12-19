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

from __future__ import unicode_literals
from builtins import object


class SpecificationAPI(object):
    """ Describe an object API

    """
    def __init__(self, specification=None, data=None):
        """
        """
        self.specification = specification

        self.rest_name = ""
        self.allows_get = False
        self.allows_create = False
        self.allows_update = False
        self.allows_delete = False
        self.allows_bulk_create = False
        self.allows_bulk_update = False
        self.allows_bulk_delete = False
        self.deprecated = False
        self.relationship = "child"

        if data:
            self.from_dict(data)

    def from_dict(self, data):
        """

        """
        # mandatory
        self.rest_name = data["rest_name"]

        self.allows_get = data["get"] if "get" in data else False
        self.allows_create = data["create"] if "create" in data else False
        self.allows_update = data["update"] if "update" in data else False
        self.allows_delete = data["delete"] if "delete" in data else False
        self.allows_bulk_create = data["bulk_create"] if "bulk_create" in data else False
        self.allows_bulk_update = data["bulk_update"] if "bulk_update" in data else False
        self.allows_bulk_delete = data["bulk_delete"] if "bulk_delete" in data else False
        self.deprecated = data["deprecated"] if "deprecated" in data else False
        self.relationship = data["relationship"] if "relationship" in data else "child"

    def to_dict(self):
        """
        """

        data = {}

        data["rest_name"] = self.rest_name
        data["get"] = self.allows_get
        data["create"] = self.allows_create
        data["update"] = self.allows_update
        data["delete"] = self.allows_delete
        data["bulk_create"] = self.allows_bulk_create
        data["bulk_update"] = self.allows_bulk_update
        data["bulk_delete"] = self.allows_bulk_delete
        data["deprecated"] = self.deprecated
        data["relationship"] = self.relationship

        return data
