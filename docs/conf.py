import re

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
master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
# html_static_path = ['_static']


def set_relative_links(app, docname, source):
    source[0] = source[0].replace(
        '../google/generativeai/',
        '/api/google/generativeai/'
    )

    # if '#' in source[0]:
    #     print("\n\nComing from set_relative_links: ")
    #     print(source[0])
    #     print("==========================================\n\n")        

def setup(app):
    app.connect('source-read', set_relative_links)



# def set_relative_links(app, pagename, templatename, context, doctree):
#     if 'body' in context:
#         # Perform the substitution in the HTML body
#         context['body'] = re.sub(
#             r'(\.\./google/generativeai/[^"]+)\.md(#\w+)?',
#             r'/api/google/generativeai/\1.html\2',
#             context['body']
#         )

# def setup(app):
#     app.connect('html-page-context', set_relative_links)
