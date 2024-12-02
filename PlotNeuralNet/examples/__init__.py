import glob
import os

baseDir = os.path.dirname(__file__)

# List all files in the examples directory, including subdirectories
exampleFiles = glob.glob(os.path.join(baseDir, "**/*.*"), recursive=True)
exampleFiles = [os.path.relpath(f, baseDir) for f in exampleFiles]  # Relative paths
