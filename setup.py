from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

ext_modules = [
    Pybind11Extension(
        "mymodule",
        ["bindings.cpp"],
        extra_compile_args=['-std=c++11'],
        library_dirs=['.'],
        libraries=['main'],
    ),
]

setup(
    name="mymodule",
    ext_modules=ext_modules,
)