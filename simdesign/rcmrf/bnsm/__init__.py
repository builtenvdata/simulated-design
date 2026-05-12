"""
Building Nonlinear Structural Model (BNSM) package.

This package provides predefined nonlinear structural modelling
configurations for building systems. The main entry point is the
:class:`BNSM` factory, which dynamically instantiates a specific
modelling strategy (e.g., CP01, DP03) based on the selected model type.

Example
-------
>>> from bnsm import BNSM
>>> model = BNSM(model="CP03", ...)
"""

from .factory import BNSM

__all__ = ["BNSM"]
