"""Sequana GUI. Can also be used for any snakemake pipeline"""
from PyQt5 import QtCore
from PyQt5 import QtWidgets as QW

from sequanix.ui import Ui_Preferences


class PreferencesDialog(QW.QDialog):
    """FIXME May not be required anymore"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Preferences()
        self.ui.setupUi(self)
        self._application = "sequana_gui"
        self._section = "preferences_dialog"
        self.read_settings()

    def accept(self):
        self.write_settings()
        super().accept()

    def reject(self):
        self.read_settings()
        super().reject()

    def read_settings(self):
        settings = QtCore.QSettings(self._application, self._section)
        for key in settings.allKeys():
            value = settings.value(key)
            try:
                # This is required to skip the tab_position key/value
                this = getattr(self.ui, key)
            except:
                continue
            if isinstance(this, QW.QLineEdit):
                this.setText(value)
            elif isinstance(this, QW.QSpinBox):
                this.setValue(int(value))
            elif isinstance(this, QW.QComboBox):
                index = this.findText(value)
                this.setCurrentIndex(index)
            elif isinstance(this, QW.QCheckBox):
                if value in ["false"]:
                    this.setChecked(False)
                else:
                    this.setChecked(True)
            else:
                print("could not handle : %s" % this)
        # The last tab position
        self._tab_pos = settings.value("tab_position", 0, type=int)
        self.ui.tabs.setCurrentIndex(self._tab_pos)

    def write_settings(self):
        settings = QtCore.QSettings(self._application, self._section)
        items = self.get_settings()
        for k, v in self.get_settings().items():
            settings.setValue(k, v)

    def _get_widget_names(self, prefix="preferences_options"):
        names = [this for this in dir(self.ui) if this.startswith(prefix)]
        names = [this for this in names if this.endswith("_value")]
        return names

    def get_settings(self):
        # get all items to save in settings
        items = {}
        names = self._get_widget_names()
        for name in names:
            widget = getattr(self.ui, name)
            if isinstance(widget, QW.QLineEdit):
                value = widget.text()
            elif isinstance(widget, QW.QSpinBox):
                value = widget.value()
            elif isinstance(widget, QW.QCheckBox):
                value = widget.isChecked()
            elif isinstance(widget, QW.QComboBox):
                value = widget.currentText()
            else:
                raise NotImplementedError("for developers")
            items[name] = value
        items["tab_position"] = self.ui.tabs.currentIndex()
        return items
