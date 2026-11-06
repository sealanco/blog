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

# Set this to your actual GitHub Pages URL (including the repository subpath)
html_baseurl = "https://sealanco.github.io/blog/"

html_theme_options = {
#    "logo_name": True,  # Uses your exact html_title instead of default branding logic
}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.mathjax',
    # "sphinx_copybutton",
    "matplotlib.sphinxext.plot_directive",
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

pygments_style = "default"  # or "sphinx", "friendly", "monokai"

plot_pre_code = """
import matplotlib.pyplot as plt
plt.style.use('dark_background')
"""

plot_rcparams = {
    "figure.facecolor": "none",
    "axes.facecolor": "none",
}
