from setuptools import setup
import os

packages = ['vspk', 'vspk.vsdk']
vsdks_path = "./vspk/vsdk"

for item in os.listdir(vsdks_path):
    if os.path.isfile("%s/%s" % (vsdks_path, item)):
        continue

    packages.append("vspk.vsdk.%s" % item)
    packages.append("vspk.vsdk.%s.fetchers" % item)
    packages.append("vspk.vsdk.%s.autogenerates" % item)

setup(
    name='vspk',
    packages=packages,
    include_package_data=True,
    version='0.1',
    description='VSPK',
    long_description=open('README.md').read(),
    author='Antoine Mercadal',
    author_email='antoine@nuagenetworks.net',
    classifiers=[],
    install_requires=[line for line in open('requirements.txt')],
)
