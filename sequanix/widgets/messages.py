from PyQt5 import QtWidgets as QW


class WarningMessage(QW.QMessageBox):
    def __init__(self, msg, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Warning message")
        self.setIcon(QW.QMessageBox.Warning)
        self.setText(msg)


class CriticalMessage(QW.QMessageBox):
    def __init__(self, msg, details="", parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Error message")
        self.setIcon(QW.QMessageBox.Critical)

        # Force a minimum width ! Cannot use setFixedWidth. This is a trick
        # found on
        # http://www.qtcentre.org/threads/22298-QMessageBox-Controlling-the-width
        layout = self.layout()
        spacer = QW.QSpacerItem(600, 0)
        layout.addItem(spacer, layout.rowCount(), 0, 1, layout.columnCount())

        msg = '<b style="color:red">' + msg + "</b><br><br>"
        try:
            details = str(details).replace("\\n", "<br>")
        except:
            pass
        self.setText(msg + details)
