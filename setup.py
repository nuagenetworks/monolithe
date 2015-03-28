from setuptools import setup

deps = ['jinja2', 'colorama', 'gitpython', 'argparse', 'requests', 'bambou',
        'sphinx==1.2.3', 'sphinx_rtd_theme', 'sphinxcontrib-napoleon']

setup(
    name='monolithe',
    packages=['generators', 'generators.lib'],
    include_package_data=True,
    version='0.0.1',
    description='Monolithe is the generator of all documentation and SDK for Nuage Network VSP',
    author='Christophe Serafin',
    author_email='christophe.serafin@nuagenetworks.net',
    url="https://github.com/nuagenetworks/monolithe",
    classifiers=[],
    install_requires=deps,
    entry_points={
        'console_scripts': [
            'vsdk-generator = generators.vsdkgenerator:main',
            'vspkdoc-generator = generators.vspkdocgenerator:main',
            'vspk-generator = generators.vspkgenerator:main',
            'apidoc-generator = generators.apidocgenerator:main']
    }
)
