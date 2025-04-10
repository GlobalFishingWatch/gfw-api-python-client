# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

SRC_DIR = "../../src/gfwapiclient"


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Global Fishing Watch API Client"
copyright = "2025, Global Fishing Watch"
author = "Global Fishing Watch"
release = "0.1.0"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # first-party extensions
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    # third-party extensions
    "myst_parser",
    # "myst_nb",
    "autodoc2",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
]


# -- Options for autodoc output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

# Define the order in which automodule and autoclass members are listed
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_member_order
autodoc_member_order = "bysource"


# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html

# This config value contains the locations and names of other projects that
# should be linked to in this documentation.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}


# -- Options for myst-parser -------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "fieldlist",
    "deflist",
    "dollarmath",
    "html_image",
]
myst_heading_anchors = 3


# -- Options for autodoc2 -------------------------------------------------
# https://sphinx-autodoc2.readthedocs.io/en/latest/config.html
autodoc2_packages = [
    {
        "path": SRC_DIR,
        "exclude_dirs": [
            "__pycache__",
        ],
    },
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_theme_options = {"sidebar_hide_name": True}

html_title = f"{project} documentation v{release}"
html_short_title = f"{project} v{release}"

html_static_path = ["_static"]
html_logo = "_static/logo-primary.png"
html_favicon = "_static/favicon.ico"
