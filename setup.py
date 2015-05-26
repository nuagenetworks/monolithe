from setuptools import setup, find_packages

setup(
    name='monolithe',
    packages=find_packages(exclude=['*tests*']),
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
            'generate-vspk = monolithe.generators.vspk.cli:main',
            'generate-specifications = monolithe.generators.specifications.cli:main',
            'generate-apidoc = monolithe.generators.apidoc.cli:main',
            'generate-vspkdoc = monolithe.generators.vspkdoc.cli:main',
            'validate-specifications = monolithe.validators.specifications.cli:main']
    }
)
