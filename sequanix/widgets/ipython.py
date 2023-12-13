# Import the console machinery from ipython
from IPython.lib import guisupport
from qtconsole.inprocess import QtInProcessKernelManager
from qtconsole.rich_jupyter_widget import RichJupyterWidget


# http://stackoverflow.com/questions/11513132/embedding-ipython-qt-console-in-a-pyqt-application
class QIPythonWidget(RichJupyterWidget):
    """Convenience class for a live IPython console widget. We can
    replace the standard banner using the customBanner argument"""

    def __init__(self, customBanner=None, *args, **kwargs):
        if customBanner != None:
            self.banner = customBanner
        super(RichJupyterWidget, self).__init__(*args, **kwargs)
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()
        kernel_manager.kernel.gui = "qt4"
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            guisupport.get_app_qt4().exit()

        self.exit_requested.connect(stop)

        self.setStyleSheet("* { selection-background-color: #5964FF; }")

    def pushVariables(self, variableDict):
        """Given a dictionary containing name / value pairs, push those
        variables to the IPython console widget"""
        self.kernel_manager.kernel.shell.push(variableDict)

    def clearTerminal(self):
        """Clears the terminal"""
        self._control.clear()

    def printText(self, text):
        """Prints some plain text to the console"""
        self._append_plain_text(text)

    def executeCommand(self, command):
        """Execute a command in the frame of the console widget"""
        self._execute(command, False)
