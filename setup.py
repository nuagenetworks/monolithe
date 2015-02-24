from setuptools import setup

github_repo = 'http://github.mv.usa.alcatel.com/corentih/vsdk-vanilla'
deps = ['jinja2', 'colorama', 'gitpython', 'argparse', 'requests', 'bambou',
        'sphinx==1.2.3', 'sphinx_rtd_theme', 'sphinxcontrib-napoleon',
        'Contextual==0.7a1.dev-r2695']

setup(
    name='vsdgenerators',
    packages=['vsdgenerators', 'vsdgenerators.lib'],
    include_package_data=True,
    version='0.2',
    description='VSD generator',
    author='Christophe Serafin',
    author_email='Christophe.Serafin@nuagenetworks.net',
    url=github_repo,
    classifiers=[],
    install_requires=deps,
    entry_points={
        'console_scripts': [
            'vsdk-generator = vsdgenerators.vsdkgenerator:main',
            'vsdkdoc-generator = vsdgenerators.vsdkdocgenerator:main',
            'apidoc-generator = vsdgenerators.apidocgenerator:main',
            'test-generator = vsdgenerators.testgenerator:main']
    },
    download_url='%s/tarball/0.2' % github_repo
)
