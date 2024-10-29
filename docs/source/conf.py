import os
import sys
import sphinx_external_toc

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

extensions = ["sphinx_external_toc"]
external_toc_path = "docs/api/google/generativeai/_toc.yaml"  # Path to your YAML file
external_toc_exclude_missing = False  # Optional; set to True to exclude missing files

    # pip install furo
    # html_theme = 'furo'
# templates_path = ['_templates']

# conda install myst-parser # "myst_parser"
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