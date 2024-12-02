import glob
import os

baseDir = os.path.dirname(__file__)

# List all files in pyexamples
pyexampleFiles = glob.glob(os.path.join(baseDir, "*.*"))
pyexampleFiles = [os.path.basename(f) for f in pyexampleFiles]  # Only file names

from .testSimple import *

# Import specific Python files
from .unet import *
