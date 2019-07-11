# -*- coding: utf-8 -*-
{{ header }}

from setuptools import setup
import os

packages = ['{{ name }}', '{{ name }}.cli']
resources = []
api_version_path = "./{{ name }}"

for version_folder in os.listdir(api_version_path):

    if os.path.isfile("%s/%s" % (api_version_path, version_folder)):
        continue

    if version_folder == "cli":
        continue

    packages.append("{{ name }}.%s" % version_folder)
    packages.append("{{ name }}.%s.fetchers" % version_folder)

    if os.path.exists('{{ name }}/%s/resources' % version_folder):
        resources.append(('{{ name }}/%s/resources' % version_folder, ['{{ name }}/%s/resources/attrs_defaults.ini' % version_folder]))

setup(
    name='{{ name }}',
    version="{{ version }}",
    url='{{ url }}',
    author='{{ author }}',
    author_email='{{ email }}',
    packages=packages,
    description='{{ description }}',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='{{ license_name }}',
    include_package_data=True,
    install_requires=[line for line in open('requirements.txt')],
    data_files=resources,
    entry_points={
        'console_scripts': [
            '{{ cli_name }} = {{ name }}.cli.cli:main']
    }
)
