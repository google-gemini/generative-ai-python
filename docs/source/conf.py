import os
import sys

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath('../..'))  # Adjust this path as necessary

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'google-generativeai'
copyright = '2024, Google LLC'
author = 'Google LLC'
release = "0.2.2"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

# templates_path = ['_templates']
# exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    # '.txt': 'restructuredtext',
    '.md': 'markdown',
}