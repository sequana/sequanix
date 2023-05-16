from PySide6 import QtWidgets as QW


class About(QW.QMessageBox):
    """A resizable QMessageBox for the About dialog"""

    def __init__(self, *args, **kwargs):
        super(About, self).__init__(*args, **kwargs)
        self.setSizeGripEnabled(True)
        self.setIcon(QW.QMessageBox.Information)
        self.setWindowTitle("Sequana")
        self.setStandardButtons(QW.QMessageBox.Ok)

    def event(self, e):
        result = super(About, self).event(e)

        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(500)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Expanding)

        return result
