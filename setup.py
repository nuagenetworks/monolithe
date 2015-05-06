from setuptools import setup

setup(
    name='monolithe',
    packages=['monolithe', 'monolithe.lib', 'monolithe.specsvalidator'],
    include_package_data=True,
    version='0.0.1',
    description='Monolithe is the generator of all documentation and SDK for Nuage Network VSP',
    author='Christophe Serafin',
    author_email='christophe.serafin@nuagenetworks.net',
    url="https://github.com/nuagenetworks/monolithe",
    classifiers=[],
    install_requires=[line for line in open('requirements.txt')],
    entry_points={
        'console_scripts': [
            'vsdk-generator = monolithe.vsdkgenerator:main',
            'vspkdoc-generator = monolithe.vspkdocgenerator:main',
            'vspk-generator = monolithe.vspkgenerator:main',
            'apidoc-generator = monolithe.apidocgenerator:main',
            'spec-validator = monolithe.specvalidator:main',
            'spec-generator = monolithe.specgenerator:main']
    }
)
