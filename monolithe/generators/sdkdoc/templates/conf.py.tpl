# -*- coding: utf-8 -*-
import sys
import os
import sphinx_rtd_theme

extensions = [ 'sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']
add_module_names = False
source_suffix = '.rst'
master_doc = 'index'
project = '{{ sdk_name }}'
copyright = '{{ copyright }}'
version = ''
release = ''
exclude_patterns = ['_build', '../sdk/autogenerates']
pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = '32doc'
html_logo = 'logo.png'
autodoc_member_order = "groupwise"
autodoc_default_flags = []


napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
