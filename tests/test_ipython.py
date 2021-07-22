import sys
from PyQt5 import QtWidgets as QW

from sequanix.widgets import QIPythonWidget

app = QW.QApplication(sys.argv)


def test_ipy():
    ipyConsole = QIPythonWidget(customBanner="Welcome to the embedded ipython console\n")
    ipyConsole.printText("The variable 'foo' andion.")
    ipyConsole.execute("from sequana import *")
    ipyConsole.execute("import sequana")
    ipyConsole.execute("")

    ipyConsole.pushVariables({"a": 1})

    ipyConsole.clearTerminal()
    ipyConsole.executeCommand("a=1")
