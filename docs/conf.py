# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information



project = 'Motorola MC6800 Exhibitions'
copyright = '2026, Andrew Shapton'
author = 'Andrew Shapton'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.autosectionlabel',
        'sphinx_collapse',
        'sphinx_design',
        'linuxdoc.rstFlatTable',
        'sphinx.ext.intersphinx',]
#        

intersphinx_mapping = {
    "mc6800collection": ("https://alshapton.github.io/MC6800Catalogue/", None),
}

# We recommend adding the following config value.
# Sphinx defaults to automatically resolve *unresolved* labels using all your Intersphinx mappings.
# This behavior has unintended side-effects, namely that documentations local references can
# suddenly resolve to an external location.
# See also:
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]


autosectionlabel_prefix_document = True
templates_path = ['_templates']
exclude_patterns = []
root_prefix = '/Users/andrew/MyProjects/Motorola-6800/MC6800Exhibitions'
source_suffix = ['.rst']




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
    'https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Round',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css'
]
