"""
pyexamples module.

This module contains example scripts for PlotNeuralNet, including U-Net and simple test cases.
"""

import glob
import os

baseDir = os.path.dirname(__file__)

# List all files in pyexamples
pyexampleFiles = glob.glob(os.path.join(baseDir, "*.*"))
pyexampleFiles = [os.path.basename(f) for f in pyexampleFiles]  # Only file names

from .test_simple import *

# Import specific Python files
from .unet import *

__all__ = ["test_simple", "unet"]
