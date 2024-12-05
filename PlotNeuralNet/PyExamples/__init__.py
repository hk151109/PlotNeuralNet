"""
pyexamples module.

This module contains example scripts for PlotNeuralNet, including U-Net and simple test cases.
"""

import glob
import os

baseDir = os.path.dirname(__file__)

# List all files in pyexamples
pyExampleFiles = glob.glob(os.path.join(baseDir, "*.*"))
pyExampleFiles = [os.path.basename(f) for f in pyExampleFiles]  # Only file names

from .TestSimple import Main as TestSimpleMain
from .UNet import Main as UnetMain

__all__ = [
    "TestSimpleMain",
    "UnetMain",
]
