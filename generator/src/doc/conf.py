# -*- coding: utf-8 -*-
import sys
import os
import sphinx_rtd_theme

extensions = [ 'sphinx.ext.autodoc', 'sphinx.ext.viewcode']
add_module_names = False
source_suffix = '.rst'
master_doc = 'index'
project = u'VSDK'
copyright = u'2015, Nuage Networks'
version = ''
release = ''
exclude_patterns = ['_build', '../vsdk/autogenerates']
pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# html_theme = "nature"
# html_static_path = ['_static']
htmlhelp_basename = '32doc'

autodoc_member_order = "groupwise"
autodoc_default_flags = ['members', 'inherited-members']
