# Configuration file for the Sphinx documentation builder.

import os
import sys

# Make repo root importable so `import simdesign` works
sys.path.insert(0, os.path.abspath("../.."))


project = 'SimDesign'
copyright = '2026, Volkan Ozsarac'
author = 'Volkan Ozsarac'
release = '0.5.0'
master_doc = "index"

project = "SimDesign"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # supports Google/Numpy style docstrings
]

autosummary_generate = False
exclude_patterns = ["_autosummary/**", "modules/**"]

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}