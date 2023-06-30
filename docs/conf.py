# Configuration file for Read the Docs

# -- Project information -----------------------------------------------------

project = 'BELIV-SIM'
version = 'latest'
release = 'latest'
author = 'Vishal Nadig'
master_doc = 'index'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = 'MyDocumentationProject'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}

latex_documents = [
    (master_doc, 'MyDocumentationProject.tex', 'My Documentation Project',
     'Your Name', 'manual'),
]

# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'mydocumentationproject', 'My Documentation Project',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc, 'MyDocumentationProject', 'My Documentation Project',
     author, 'MyDocumentationProject', 'One line description of project.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------

# Add any custom configuration options for extensions here.

# -- Intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
}
