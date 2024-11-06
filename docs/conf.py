project = 'Google Generative AI - Python'
copyright = '2024, Google LLC'
author = 'Google LLC'

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'myst_parser',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    ]

# autosectionlabel_prefix_document = True

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
    "substitution",
    "linkify",
]
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-header-anchors
# Controls allowable header anchors in markdown files. Value allows header anchors for h1 - h6
myst_heading_anchors = 6

source_suffix = {'.md': 'markdown',}
master_doc = 'index' #'api/google/generativeai'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
# html_static_path = ['_static']


# def set_relative_links(app, docname, source):
#     source[0] = source[0].replace(
#         '../google/generativeai/',
#         '/api/google/generativeai/'
#     )

# def setup(app):
#     app.connect('source-read', set_relative_links)

import re

def set_relative_links(app, docname, source):
    def replace_link(match):
        path = match.group(1)
        anchor = match.group(2) or ''
        if path.endswith('.md'):
            path = path[:-3] + '.html'
        return f'/api/google/generativeai/{path}{anchor}'

    # Pattern for both Markdown links and HTML anchor links
    pattern = r'(?:href="|")(?:\.\.\/google\/generativeai\/)?([\w-]+\.md)(#[\w-]+)?"'
    
    # Replace the links
    source[0] = re.sub(pattern, lambda m: f'href="{replace_link(m)}"', source[0])

    source[0] = source[0].replace(
        '../google/generativeai/',
        '/api/google/generativeai/'
    )

def setup(app):
    app.connect('source-read', set_relative_links)