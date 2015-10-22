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

from monolithe.lib import SDKUtils


class SpecificationAPI(object):
    """ Describe an object API

    """
    def __init__(self, remote_specification_name, specification=None, data=None):
        """
        """
        self.specification = remote_specification_name

        self.allows_get    = False
        self.allows_create = False
        self.allows_update = False
        self.allows_delete = False
        self.deprecated    = False
        self.relationship  = "child"

        if data:
            self.from_dict(data)

    def from_dict(self, data):
        """

        """
        self.allows_get    = data["get"] if "get" in data else False
        self.allows_create = data["create"] if "create" in data else False
        self.allows_update = data["update"] if "update" in data else False
        self.allows_delete = data["delete"] if "delete" in data else False
        self.deprecated    = data["deprecated"] if "deprecated" in data else False
        self.relationship  = data["relationship"] if "relationship" in data else "child"

    def to_dict(self):
        """
        """

        data = {}

        if self.allows_get:
            data["get"] = self.allows_get

        if self.allows_create:
            data["create"] = self.allows_create

        if self.allows_update:
            data["update"] = self.allows_update

        if self.allows_delete:
            data["delete"] = self.allows_delete

        if self.deprecated:
            data["deprecated"] = self.deprecated

        if self.relationship:
            data["relationship"] = self.relationship

        return data
