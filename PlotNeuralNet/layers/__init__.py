"""
layers module.

This module contains LaTeX style and initialization files for different neural network layers used in PlotNeuralNet.
"""

import glob
import os

baseDir = os.path.dirname(__file__)

# List all .sty and .tex files
layerFiles = glob.glob(os.path.join(baseDir, "*.*"))
layerFiles = [os.path.basename(f) for f in layerFiles]  # Only file names

# Example: Export file paths for programmatic access
ballStyPath = os.path.join(baseDir, "Ball.sty")
boxStyPath = os.path.join(baseDir, "Box.sty")
rightBandedBoxStyPath = os.path.join(baseDir, "RightBandedBox.sty")
initTexPath = os.path.join(baseDir, "init.tex")
