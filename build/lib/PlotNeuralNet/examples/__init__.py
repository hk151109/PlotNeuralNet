"""
examples module.

This module aggregates all example scripts for generating neural network diagrams using PlotNeuralNet.
"""

import glob
import os

baseDir = os.path.dirname(__file__)

# List all files in the examples directory, including subdirectories
example_files = glob.glob(os.path.join(baseDir, "**/*.*"), recursive=True)
example_files = [os.path.relpath(f, baseDir) for f in example_files]  # Relative paths

__all__ = [
    "AlexNet",
    "HED",
    "LeNet",
    "SoftmaxLoss",
    "Unet",
    "UnetUshape",
    "VGG16",
    "fcn32",
    "fcn8",
]
