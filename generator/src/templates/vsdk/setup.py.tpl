from setuptools import setup

setup(
    name='vsdk',
    version='{{apiversion}}-{{revisionnumber}}',
    url='http://www.nuagenetworks.net/',
    author='NuageNetworks',
    author_email='christophe.serafin@nuagenetworks.net',
    packages=['vsdk', 'vsdk.autogenerates', 'vsdk.fetchers'],
    description='VSD Python SDK for API',
    long_description=open('README.md').read(),
    install_requires=[line for line in open('requirements.txt')],
)
