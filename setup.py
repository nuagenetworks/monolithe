from setuptools import setup

deps = ['jinja2', 'colorama', 'gitpython', 'argparse', 'requests', 'bambou',
        'sphinx==1.2.3', 'sphinx_rtd_theme', 'sphinxcontrib-napoleon']

setup(
    name='monolithe',
    packages=['vsdgenerators', 'vsdgenerators.lib'],
    include_package_data=True,
    version='0.2',
    description='VSD generator',
    author='Christophe Serafin',
    author_email='christophe.serafin@nuagenetworks.net',
    url="https://github.com/nuagenetworks/monolithe",
    classifiers=[],
    install_requires=deps,
    entry_points={
        'console_scripts': [
            'vsdk-generator = vsdgenerators.vsdkgenerator:main',
            'vsdkdoc-generator = vsdgenerators.vsdkdocgenerator:main',
            'vspk-generator = vsdgenerators.vspkgenerator:main'
            'apidoc-generator = vsdgenerators.apidocgenerator:main']
    }
)
