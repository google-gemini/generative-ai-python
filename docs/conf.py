import re
from docutils import nodes

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

# def set_relative_links(app, docname, source):
#     source[0] = source[0].replace(
#         '../google/generativeai/',
#         '/api/google/generativeai/'
#     )


# def setup(app):
#     app.connect('source-read', set_relative_links)



def markdown_link_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    match = re.match(r'(.*?)\s*<(.+?)>', text)
    if match:
        label, target = match.groups()
    else:
        label = text
        target = text

    # Convert .md to .html and add the prefix
    target = target.replace('.md#', '.html#')
    target = f'/generative-ai-python{target}' if not target.startswith('/generative-ai-python') else target

    url = target
    node = nodes.reference(rawtext, label, refuri=url, **options)
    return [node], []

def setup(app):
    app.add_role('mdlink', markdown_link_role)
