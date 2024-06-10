"""Demo package for course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-coursenf")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Noel Frey"
__email__ = "frey.noel1@gmail.com"

from . import algos