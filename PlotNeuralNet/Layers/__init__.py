"""
Layers module.

This module contains LaTeX style and initialization files for different neural network layers used in PlotNeuralNet.
"""

import glob
import os

baseDir = os.path.dirname(__file__)

# List all .sty and .tex files
layer_files = glob.glob(os.path.join(baseDir, "*.*"))
layer_files = [os.path.basename(f) for f in layer_files]  # Only file names

# Example: Export file paths for programmatic access
ballStyPath = os.path.join(baseDir, "Ball.sty")
boxStyPath = os.path.join(baseDir, "Box.sty")
rightBandedBoxStyPath = os.path.join(baseDir, "RightBandedBox.sty")
initTexPath = os.path.join(baseDir, "init.tex")


__all__ = ["Ball", "Box", "RightBandedBox", "initialize_layers", "layer_files"]
