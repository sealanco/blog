# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Maths for Python'
copyright = '2026, Sérgio A. A. Coutinho'
author = 'Sérgio A. A. Coutinho'

# Set the exact HTML title without the "documentation" suffix
html_title = "Maths for Python"
html_short_title = "Maths for Python"

html_theme_options = {
#    "logo_name": True,  # Uses your exact html_title instead of default branding logic
}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',             # Replaces both myst_parser and plot_directive
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = [
    "_build",
    "_website",  # Added based on your output path
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "**/jupyter_execute",  # Catches nested execution directories
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']

myst_enable_extensions = [
    "colon_fence",  # Enables ::: directive blocks
    "deflist",      # Enables definition lists
]

# Enable dollar sign math parsing in Markdown
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

# Tell Sphinx to parse .md files using myst-nb
#source_suffix = {
#    '.rst': 'restructuredtext',
#    '.md': 'myst-nb',
#}

# Optional: suppress execution warnings if desired
nb_execution_mode = "force"

