# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
# '../..' means: go up one level from 'source' to 'docs', then up another level to 'AI_GUARD' (the project root)
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AI_GUARD'
copyright = '2025, Wiame'
author = 'Wiame'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',      # Core Sphinx extension to pull documentation from docstrings.
    'sphinx.ext.napoleon',     # Enables Sphinx to understand Google and NumPy style docstrings.
                               # (Highly recommended if you use these styles!)
    'sphinx.ext.viewcode',     # Adds links from your API docs to the highlighted source code.
    'sphinx.ext.intersphinx',  # Allows linking to other projects' documentation (e.g., Python, NumPy).
    'myst_parser',             # Enables you to write documentation in Markdown (.md) files.
    'sphinx_autodoc_typehints',# Renders Python type hints nicely in the API documentation.
                               # (Install this if you haven't: pip install sphinx-autodoc-typehints)
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    # 'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    # 'matplotlib': ('https://matplotlib.org/stable/', None),
    # Add other projects you commonly refer to
}