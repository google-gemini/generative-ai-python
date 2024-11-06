project = 'Google Generative AI - Python'
copyright = '2024, Google LLC'
author = 'Google LLC'

extensions = [
    'sphinx.ext.coverage',
    'myst_parser',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    ]

myst_url_schemes = ["http", "https", "mailto"]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "tasklist",
    "substitution"
]

source_suffix = {'.md': 'markdown',}
master_doc = 'index'  # Changed in version 2.0: Default is 'index' (previously 'contents').

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
# html_static_path = ['_static']


import re

# def set_relative_links(app, docname, source):
#     # Pattern to match the GitHub links
#     pattern = r'https://github\.com/vi-shruti/generative-ai-python/blob/main/docs/api/google/generativeai/(.+?)\.md(#.+)?'
    
#     def replace_link(match):
#         file_name = match.group(1)
#         anchor = match.group(2) or ''
        
#         # If it's the GenerativeModel file, we don't need the file name in the link
#         if file_name == 'GenerativeModel':
#             return f'{anchor}'
#         else:
#             return f'/api/google/generativeai/{file_name}{anchor}'

#     # Replace the links
#     source[0] = re.sub(pattern, replace_link, source[0])


def set_relative_links(app, docname, source):
    source[0] = source[0].replace(
        '../google/generativeai/GenerativeModel.md',
        ''
    )

    source[0] = source[0].replace(
        '../google/generativeai/',
        '/api/google/generativeai/'
    )


def setup(app):
    app.connect('source-read', set_relative_links)
