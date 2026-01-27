# pylint: disable=missing-docstring
"""
Setup script for lie_learn.

Build dependencies (numpy, cython) are specified in pyproject.toml
and will be installed automatically by PEP 517 compliant build tools.
"""
import os
import sys

# Make sure numpy and cython are available (they're in build-system.requires)
import numpy as np
from Cython.Build import cythonize
from setuptools import setup, Extension

# Get numpy include path
numpy_include = np.get_include()

# Define the Cython extensions explicitly
extensions = [
    Extension(
        "lie_learn.groups.SO3",
        ["lie_learn/groups/SO3.pyx"],
        include_dirs=[numpy_include],
    ),
    Extension(
        "lie_learn.representations.SO3.irrep_bases",
        ["lie_learn/representations/SO3/irrep_bases.pyx"],
        include_dirs=[numpy_include],
    ),
    Extension(
        "lie_learn.representations.SO3.pinchon_hoggan.pinchon_hoggan",
        ["lie_learn/representations/SO3/pinchon_hoggan/pinchon_hoggan.pyx"],
        include_dirs=[numpy_include],
    ),
    Extension(
        "lie_learn.spaces.spherical_quadrature",
        ["lie_learn/spaces/spherical_quadrature.pyx"],
        include_dirs=[numpy_include],
    ),
]

# Cythonize with Python 3 language level
ext_modules = cythonize(
    extensions,
    language_level="3",
    compiler_directives={
        "boundscheck": False,
        "wraparound": False,
        "cdivision": True,
    },
)

setup(
    ext_modules=ext_modules,
)
