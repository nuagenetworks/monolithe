from distutils.core import setup

setup(
    name='vsdk_api',
    version='V3_0_1',
    author='Christophe Serafin, Aravind Ganesan',
    author_email='christophe.serafin@alcatel-lucent.com, aravind.ganesan@alcatel-lucent.com',
    packages=['vsdk_V3_0', 'vsdk_V3_0.autogenerates', 'vsdk_V3_0.fetchers'],
    description='VSD Python SDK for API V3_0',
    long_description=open('README.md').read(),
    install_requires=[line for line in open('requirements.txt')],
)

