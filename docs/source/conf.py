import os
import sys

from setup import release_status

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
release = release_status

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',               # For Markdown support
]

# templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_static_path = ['_static']
