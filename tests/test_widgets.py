import sys

import pytest
from PySide6 import QtWidgets as QW
from PySide6.QtGui import qBlue

from sequanix.widgets import (
    About,
    Browser,
    CriticalMessage,
    PreferencesDialog,
    SnakemakeDialog,
    WarningMessage,
)


def test_preference(qtbot, mocker):
    widget = PreferencesDialog()
    qtbot.addWidget(widget)

    widget.read_settings()  ##### do not write settings in the test or with a mock

    widget.get_settings()
    widget.accept()
    widget.reject()


def test_snakemakedialog(qtbot):
    form = SnakemakeDialog()
    qtbot.addWidget(form)

    form.get_snakemake_local_options()
    form.get_snakemake_general_options()
    form.get_snakemake_cluster_options()

    form.accept()

    form.reject()
    form.get_settings()


def test_warning(qtbot):
    w = WarningMessage("test")
    w.show()
    qtbot.addWidget(w)


def test_critical(qtbot):
    w = CriticalMessage("test", details="test")
    w.show()
    qtbot.addWidget(w)


def test_browser(qtbot):
    window = Browser(url="https://sequana.readthedocs.io")
    window.show()
    window.close()


def test_directory_dialog(qtbot):
    widget = About()
    widget.show()
    qtbot.addWidget(widget)
