__version__ = "0.1.1"


import os
import sys

from pathlib import Path
# Make generated protobuf files to work.
sys.path.append(os.path.join(Path(__file__).parent, "pb"))

from .wrapper import CLUE
