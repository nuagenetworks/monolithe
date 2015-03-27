from setuptools import setup

setup(
    name='vspk',
    packages=['vspk'],
    include_package_data=True,
    version='0.1',
    description='VSPK',
    long_description=open('README.md').read(),
    author='Antoine Mercadal',
    author_email='antoine@nuagenetworks.net',
    classifiers=[],
    install_requires=[line for line in open('requirements.txt')],
)
