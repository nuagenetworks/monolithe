from setuptools import setup

setup(
    name='vsdk',
    version='{{apiversion}}-{{revisionnumber}}',
    url='http://www.nuagenetworks.net/',
    author='Christophe Serafin, Aravind Ganesan',
    author_email='christophe.serafin@alcatel-lucent.com, aravind.ganesan@alcatel-lucent.com',
    packages=['vsdk', 'vsdk.autogenerates', 'vsdk.fetchers'],
    description='VSD Python SDK for API',
    long_description=open('README.md').read(),
    install_requires=[line for line in open('requirements.txt')],
)
