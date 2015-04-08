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
    version='0.0.1',
    author='Antoine Mercadal',
    author_email='antoine@nuagenetworks.net',
    packages=packages,
    description='Nuage Networks VSP Software Development Kit',
    long_description=open('README.md').read(),
    install_requires=[line for line in open('requirements.txt')],
    license='TODO',
    url='https://github.com/nuagenetworks',
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: Other/Proprietary License",
        "Environment :: Console",
        "Intended Audience :: Developers"
    ]
)
