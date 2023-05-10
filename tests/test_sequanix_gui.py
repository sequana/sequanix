import os
import time
from argparse import Namespace

import pytest
from mock import patch
from easydev import TempFile
from PyQt5 import QtWidgets as QW
from sequana_pipetools import Module, SequanaConfig

from sequanix.sequanix import SequanixGUI, Options

from . import test_dir


skiptravis = pytest.mark.skipif("TRAVIS_PYTHON_VERSION" in os.environ, reason="On travis")


@pytest.fixture
def module():
    return Module("pipeline:fastqc")


def test_settings(qtbot):
    widget = SequanixGUI(ipython=False)
    qtbot.addWidget(widget)
    widget.read_settings()

    # widget.menuHelp()
    widget.close()


def test_standalone_generic(qtbot, tmpdir, module):
    # Standalone for generic case given a wkdir and snakefile (no config)
    args = Namespace(wkdir=str(tmpdir), snakefile=module.snakefile)
    widget = SequanixGUI(ipython=False, user_options=args)
    qtbot.addWidget(widget)
    assert widget.mode == "generic"


def test_standalone_generic_with_config(qtbot, tmpdir):
    # Standalone for generic case given a wkdir and snakefile

    args = Namespace(
        wkdir=str(tmpdir),
        snakefile=f"{test_dir}/resources/test_generic.smk",
        configfile=f"{test_dir}/resources/test_generic.yml",
    )
    widget = SequanixGUI(ipython=False, user_options=args)
    qtbot.addWidget(widget)
    assert widget.mode == "generic"
    assert widget.generic_factory.is_runnable() == True
    widget.save_project()

    # read back
    yaml = SequanaConfig(str(tmpdir) + "/test_generic.yml").config
    assert yaml["test"]["mylist"] == [1, 2, 3]


def test_standalone_generic_with_config(qtbot, tmpdir, module):
    # Standalone for generic case given a wkdir and snakefile
    args = Namespace(wkdir=str(tmpdir), snakefile=module.snakefile, configfile=module.config)
    widget = SequanixGUI(ipython=False, user_options=args)
    qtbot.addWidget(widget)
    assert widget.mode == "generic"
    assert widget.generic_factory.is_runnable()
    widget.save_project()
    widget.unlock_snakemake()
    with TempFile() as fh:
        widget.report_issues(fh.name)

    widget.click_run()


def test_standalone_generic_with_noconfig_2(qtbot, tmpdir):
    """mimics:

        sequanix -s path_to_snakefile

    followed by selection of a working directory in the GUI + forceall + run
    """
    # From the command line argument
    snakefile = f"{test_dir}/resources/test_generic_noconfig.smk"
    args = Namespace(snakefile=snakefile)
    widget = SequanixGUI(ipython=False, user_options=args)
    qtbot.addWidget(widget)
    assert widget.mode == "generic"
    assert not widget.generic_factory.is_runnable()
    assert not widget.ui.run_btn.isEnabled()

    widget.generic_factory._directory_browser.set_filenames(str(tmpdir))
    widget.force = True
    widget.save_project()

    # check that it worked:
    widget.snakemake_dialog.ui.snakemake_options_general_forceall_value.setChecked(True)
    widget.click_run()
    time.sleep(2)
    widget.click_stop()
    time.sleep(4)
    widget.show_dag()
    time.sleep(4)
    widget.diag.close()

    # in the GUI, we see when it stops. Here, we need to wait a few seconds
    time.sleep(5)
    # data = open(wkdir.name + os.sep + "count.txt").read().split()


def test_open_report(qtbot, tmpdir, module):
    p = tmpdir.mkdir("sub").join("test.html")
    p.write("hello")

    args = Namespace(wkdir=str(p.dirpath()), snakefile=module.snakefile)

    # Open a valid HTML file
    widget = SequanixGUI(ipython=False, user_options=args)
    qtbot.addWidget(widget)
    widget.preferences_dialog.ui.preferences_options_general_htmlpage_value.setText("test.html")
    widget.open_report()
    assert widget.browser.isVisible()
    widget.close()

    # a wrong filename
    widget.preferences_dialog.ui.preferences_options_general_htmlpage_value.setText("dummy.html")
    widget.open_report()
    assert widget.browser.isVisible() is False

    # Now, we unset the working dir and this should just return without openning
    # any report
    widget.sequana_factory._directory_browser.set_empty_path()
    widget.generic_factory._directory_browser.set_empty_path()
    assert widget.working_dir is None
    widget.open_report()
    assert widget.browser.isVisible() is False

    # try using firefox
    widget = SequanixGUI(ipython=False, user_options=args)
    qtbot.addWidget(widget)
    widget.preferences_dialog.ui.preferences_options_general_htmlpage_value.setText("test.html")
    widget.preferences_dialog.ui.preferences_options_general_browser_value.setCurrentText("firefox")

    def simple_execute(cmd):
        pass

    @patch("easydev.execute", side_effects=simple_execute)
    def runthis(qtbot):
        widget.open_report()

    runthis()
    # There is no dialog browser but firefox should open a tab
    # assert widget.browser.isVisible()


def test_progress_bar(qtbot):
    widget = SequanixGUI(ipython=False)
    qtbot.addWidget(widget)
    widget.click_run()  # defines the regex
    widget.update_progress_bar("0 of 10 steps ")
    widget.update_progress_bar("10 of 10 steps ")
    widget.start_progress()
    widget.end_run()


def test_user_interface_sequana(qtbot):
    widget = SequanixGUI(ipython=False)
    qtbot.addWidget(widget)
    assert widget.form.count() == 0

    # simulate selection of quality control pipeline
    index = widget.sequana_factory._choice_button.findText("pipeline:fastqc")
    widget.sequana_factory._choice_button.setCurrentIndex(index)
    widget.ui.tabs_pipeline.setCurrentIndex(0)  # set sequana pipeline mode
    widget._update_sequana("pipeline:fastqc")

    # we should have the focus on the config file now
    assert widget.ui.tabs.currentIndex() == 2
    assert widget.form.count() == 6
    widget.clear_form()
    assert widget.form.count() == 0

    # select no pipeline
    widget._update_sequana("Select a Sequana pipeline")
    assert widget.form.count() == 0


def test_others(qtbot, mocker):
    widget = SequanixGUI(ipython=False)
    qtbot.addWidget(widget)
    # level and pipeline attribute
    widget.set_level()
    assert widget.sequana_factory.pipeline is None
    # The repr functions
    widget.sequana_factory.__repr__()
    widget.generic_factory.__repr__()

    import sequanix.widgets

    # menuQuit
    mocker.patch.object(sequanix.widgets.WarningMessage, "exec_", return_value=QW.QMessageBox.Yes)
    widget.menuQuit()

    # menu Help and About
    mocker.patch.object(sequanix.widgets.About, "exec_", return_value=QW.QMessageBox.Ok)
    widget.menuAbout()
    mocker.patch.object(sequanix.widgets.HelpDialog, "exec_", return_value=QW.QMessageBox.Ok)
    widget.menuHelp()


def test_generic_copy_nodir(qtbot):
    # _copy does not work if directory not set
    snakefile = f"{test_dir}/resources/test_generic_noconfig.rules"
    configfile = f"{test_dir}/resources/test_generic_config.yaml"
    args = Namespace(snakefile=snakefile, configfile=configfile)
    widget = SequanixGUI(ipython=False, user_options=args)
    qtbot.addWidget(widget)
    widget.generic_factory._copy_configfile()
    widget.generic_factory._copy_snakefile()


def test_options():
    user_options = Options()
    options = user_options.parse_args(["--pipeline", "fastqc"])


def test_only(qtbot):
    from easydev import execute

    execute("sequanix --no-splash --testing")


def test_import_config_from_menu(qtbot):
    widget = SequanixGUI(ipython=False)
    qtbot.addWidget(widget)
    assert widget.sequana_factory._imported_config is None
    # while an existing config file should
    # First, we simulate selection of quality control pipeline
    index = widget.sequana_factory._choice_button.findText("pipeline:fastqc")
    widget.sequana_factory._choice_button.setCurrentIndex(index)
    widget.ui.tabs_pipeline.setCurrentIndex(0)  # set sequana pipeline mode
    widget._update_sequana("pipeline:fastqc")

    qc = Module("pipeline:fastqc")
    widget.menuImportConfig(qc.config)
    assert widget.sequana_factory._imported_config is not None

    widget.close()
