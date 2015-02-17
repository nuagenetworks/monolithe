# -*- coding: utf-8 -*-
import sys
import os

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'
project = u'vsdk'
copyright = u'2015, Nuage Networks'
version = ''
release = ''
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'nature'
html_static_path = ['_static']
htmlhelp_basename = '32doc'
man_pages = [
    ('index', '32', u'3.2 Documentation',
     [u'Author'], 1)
]
