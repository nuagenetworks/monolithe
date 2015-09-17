# -*- coding: utf-8 -*-
#
# {{copyright}}
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

from setuptools import setup
import os

packages = ['{{sdk_name}}']
resources = []
sdk_api_version_path = "./{{sdk_name}}"

for version_folder in os.listdir(sdk_api_version_path):
    if os.path.isfile("%s/%s" % (sdk_api_version_path, version_folder)):
        continue

    packages.append("{{sdk_name}}.%s" % version_folder)
    packages.append("{{sdk_name}}.%s.fetchers" % version_folder)
    packages.append("{{sdk_name}}.%s.autogenerates" % version_folder)

    resources.append(('{{sdk_name}}/%s/resources' % version_folder, ['{{sdk_name}}/%s/resources/attrs_defaults.ini' % version_folder]))

sdk_name_upper = "{{sdk_name}}_VERSION".upper()

setup(
    name='{{sdk_name}}',
    version=os.environ[sdk_name_upper] if sdk_name_upper in os.environ else {{sdk_version}},
    url='{{sdk_url}}',
    author='{{sdk_author}}',
    author_email='{{sdk_email}}',
    packages=packages,
    description='{{sdk_description}}',
    long_description=open('README.md').read(),
    install_requires=[line for line in open('requirements.txt')],
    license='{{sdk_license_name}}',
    include_package_data=True,
    data_files=resources
)
