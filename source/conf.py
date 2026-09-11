# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "demoutrei's utilities"
copyright = '2026, demoutrei'
author = 'demoutrei'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "jupyter_sphinx",
  "shibuya",
  "sphinx_contributors",
  "sphinx_design",
  "sphinx_tabs.tabs",
  "sphinx_thebe"
]

jupyter_sphinx_thebelab_config = {
  "requestKernel": True,
  "binderOptions": {
    "repo": "binder-examples/requirements"
  }
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_context = {
  "source_type": "github",
  "source_user": "demoutrei",
  "source_repo": "utils",
  "source_version": "main",
  "source_docs_path": "/source/"
}
html_favicon = "_static/demoutrei.png"
html_theme = 'shibuya'
html_theme_options = {
  "accent_color": "green",
  "color_mode": "dark",
  "globaltoc_expand_depth": 1,
  "toctree_collapse": True,
  "toctree_maxdepth": 5,
  "show_ai_links": False,
  "og_image_url": "https://cdn.discordapp.com/embed/avatars/2.png",
  "discussion_url": "https://github.com/demoutrei/utils/discussions"
}
html_static_path = ['_static']
html_css_files = [ "custom.css" ]
html_js_files = [
  "timestampConverter.js"
]
html_title = "demoutrei's utilities"