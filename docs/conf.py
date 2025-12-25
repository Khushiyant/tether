import os
import sys
# Ensure Sphinx can find the source code
sys.path.insert(0, os.path.abspath('../src'))

project = 'Tether'
copyright = '2025, Khushiyant'
author = 'Khushiyant'
release = '0.0.1'

extensions = [
    'sphinx.ext.autodoc',      # Core library for html generation from docstrings
    'sphinx.ext.autosummary',  # Create neat summary tables
    'sphinx.ext.napoleon',     # Support for NumPy/Google style docstrings
    'sphinx.ext.viewcode',     # Add links to highlighted source code
    'myst_parser',             # Support for Markdown files
    'sphinx_autodoc_typehints' # Show type hints in docs
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Use the Read the Docs theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Napoleon settings to handle your current docstring style
napoleon_google_docstring = False
napoleon_numpy_docstring = True