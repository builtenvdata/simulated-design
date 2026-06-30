# Configuration file for the Sphinx documentation builder.

import inspect
import os
import sys

from sphinx.ext.autodoc import INSTANCEATTR, SLOTSATTR

# Add project root to PYTHONPATH so `import simdesign` works
sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------

project = "SimDesign"
author = "Volkan Ozsarac"
copyright = "2026, Volkan Ozsarac"
release = "1.0.0-beta"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
]

todo_include_todos = False

# Napoleon settings (NumPy style docstrings)
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_ivar = False
napoleon_custom_sections = [
    ("Abbreviations for rebars", "notes_style"),
    ("Assumptions", "notes_style"),
    ("TODO", "notes_style"),
]

# Show type hints in description instead of signature
autodoc_typehints = "description"
autodoc_typehints_format = "short"   # nicer type display

# Order members as they appear in source
autodoc_member_order = "bysource"

# Include undocumented members if needed
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}

# Paths that contain templates
templates_path = ["_templates"]

# Ignore build artifacts
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Hide Pydantic-inherited members from autoclass :members: ----------------

_PYDANTIC_SKIP = {
    # Pydantic v2 BaseModel
    "model_config", "model_fields", "model_computed_fields", "model_extra",
    "model_fields_set", "model_construct", "model_copy", "model_dump",
    "model_dump_json", "model_json_schema", "model_parametrized_name",
    "model_post_init", "model_rebuild", "model_validate",
    "model_validate_json", "model_validate_strings",
    # Pydantic v1 compatibility
    "construct", "copy", "dict", "from_orm", "json", "parse_file",
    "parse_obj", "parse_raw", "schema", "schema_json",
    "update_forward_refs", "validate", "Config",
}


def _is_data_attribute(obj):
    """True if ``obj`` is a data/class attribute rather than a routine,
    class, or property.

    Note: in ``autodoc-skip-member`` the ``what`` argument is the *parent's*
    type (e.g. ``"class"``), not the member's type, so it cannot be used to
    detect attributes. We inspect the member object instead.
    """
    if obj is INSTANCEATTR or obj is SLOTSATTR:
        # Annotation-only attribute (e.g. ``rot_angle: float``) with no value.
        return True
    if inspect.isroutine(obj) or inspect.isclass(obj) or isinstance(obj, property):
        return False
    return True


def _skip_pydantic_members(app, what, name, obj, skip, options):
    # Skip declared/data attributes; they're already documented in the
    # class docstring's "Attributes" section (rendered by Napoleon).
    if not name.startswith("__") and _is_data_attribute(obj):
        return True
    if name in _PYDANTIC_SKIP:
        return True
    if name.startswith("__pydantic_") or name.startswith("_pydantic_"):
        return True
    if name in {"__private_attributes__", "__class_vars__", "__signature__",
                "__pretty__", "__rich_repr__", "__repr_args__",
                "__repr_name__", "__repr_str__"}:
        return True
    return skip


def setup(app):
    app.connect("autodoc-skip-member", _skip_pydantic_members)

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}

html_static_path = ["_static"]