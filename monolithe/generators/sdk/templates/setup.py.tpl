# -*- coding: utf-8 -*-
{{ header }}

from setuptools import setup
import os

packages = ['{{ sdk_name }}', '{{ sdk_name }}.cli']
resources = []
sdk_api_version_path = "./{{ sdk_name }}"

for version_folder in os.listdir(sdk_api_version_path):

    if os.path.isfile("%s/%s" % (sdk_api_version_path, version_folder)):
        continue

    if version_folder == "cli":
        continue

    packages.append("{{ sdk_name }}.%s" % version_folder)
    packages.append("{{ sdk_name }}.%s.fetchers" % version_folder)

    resources.append(('{{ sdk_name }}/%s/resources' % version_folder, ['{{ sdk_name }}/%s/resources/attrs_defaults.ini' % version_folder]))

sdk_name_upper = "{{ sdk_name }}_VERSION".upper()

setup(
    name='{{ sdk_name }}',
    version=os.environ[sdk_name_upper] if sdk_name_upper in os.environ else "{{ sdk_version }}",
    url='{{ sdk_url }}',
    author='{{ sdk_author }}',
    author_email='{{ sdk_email }}',
    packages=packages,
    description='{{ sdk_description }}',
    long_description=open('README.md').read(),
    install_requires=[line for line in open('requirements.txt')],
    license='{{ sdk_license_name }}',
    include_package_data=True,
    data_files=resources,
    entry_points={
        'console_scripts': [
            '{{ sdk_cli_name }} = {{ sdk_name }}.cli.cli:main']
    }
)
