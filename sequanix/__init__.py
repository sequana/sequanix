
import pkg_resources

try:
    version = pkg_resources.require("sequanix")[0].version
except:
    version = ">=0.2"


from .sequanix import SequanixGUI, main
