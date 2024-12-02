"""
pyexamples module.

This module contains example scripts for PlotNeuralNet, including U-Net and simple test cases.
"""

import glob
import os

baseDir = os.path.dirname(__file__)

# List all files in pyexamples
py_example_files = glob.glob(os.path.join(baseDir, "*.*"))
py_example_files = [os.path.basename(f) for f in py_example_files]  # Only file names


from .test_simple import main as test_simple_main
from .unet import main as unet_main

__all__ = [
    "test_simple_main",
    "unet_main",
]
