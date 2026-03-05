from importlib.metadata import PackageNotFoundError, version as _version

try:
    version = _version("sequanix")
except PackageNotFoundError:
    version = ">=0.2"


from .sequanix import SequanixGUI, main
