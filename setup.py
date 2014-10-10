from distutils.core import setup

setup(
    name='pymodel',
    version='0.0.1',
    author='Christophe Serafin',
    author_email='christophe.serafin@alcatel-lucent.com',
    packages=['pymodel', 'pymodel.autogenerates', 'pymodel.fetchers'],
    description='VSD Python SDK',
    long_description=open('README.md').read(),
    install_requires=[line for line in open('requirements.txt')],
)