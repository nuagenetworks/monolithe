from setuptools import setup
from os import walk


def get_data_files_from_root(root_dir):
    data_files = []
    for (root, dirs, files) in walk(root_dir):
        if files:
            files = ['%s/%s' % (root, f) for f in files]
            data_files.append((root, files))
    return data_files


def get_data_files():
    files = ['README.md', 'vsdkgenerator.py', 'vsdkdocgenerator.py',
             'testgenerator.py', 'docgenerator.py']
    files = files + get_data_files_from_root('data')
    files = files + get_data_files_from_root('vsdgenerators/templates/')
    return files

github_repo = 'http://github.mv.usa.alcatel.com/corentih/vsdk-vanilla'
deps = ['jinja2', 'colorama', 'gitpython', 'argparse', 'requests', 'bambou',
        'sphinx==1.2.3', 'sphinx_rtd_theme', 'sphinxcontrib-napoleon',
        'Contextual==0.7a1.dev-r2695']

setup(
    name='vsdgenerators',
    packages=['vsdgenerators', 'vsdgenerators.lib'],
    data_files=get_data_files(),
    version='0.2',
    description='VSD generator',
    author='Christophe Serafin',
    author_email='Christophe.Serafin@nuagenetworks.net',
    url=github_repo,
    classifiers=[],
    install_requires=deps,
    entry_points={
        'console_scripts': ['vsdk-generator = vsdkgenerator:main',
                            'test-generator = testgenerator:main',
                            'vsdkdoc-generator = vsdkdocgenerator:main']
    },
    download_url='%s/tarball/0.2' % github_repo
)
