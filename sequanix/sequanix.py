#  This file is part of Sequana software
#
#  Copyright (c) 2016 - Sequana Development Team
#
#  File author(s):
#      Thomas Cokelaer <thomas.cokelaer@pasteur.fr>
#      Dimitri Desvillechabrol <dimitri.desvillechabrol@pasteur.fr>,
#          <d.desvillechabrol@gmail.com>
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/sequana/sequana
#  documentation: http://sequana.readthedocs.io
#
##############################################################################
"""Sequana GUI. Can also be used for any snakemake pipeline"""
import sys
import os
import shutil
import re
import time
import psutil
import subprocess as sp
import argparse
import signal
import pkg_resources

from PySide6 import QtCore, QtGui
from PySide6 import QtWidgets as QW
from PySide6.QtCore import Qt, QTemporaryDir
from PySide6.QtCore import Slot as pyqtSlot

from sequana_pipetools import snaketools
from sequanix.utils import YamlDocParser, on_cluster, rest2html

from .ui import Ui_MainWindow
from .widgets import (
    Browser,
    QIPythonWidget,
    About,
    FileBrowser,
    SVGDialog,
    WarningMessage,
    CriticalMessage,
    PreferencesDialog,
    HelpDialog,
    SnakemakeDialog,
    Logger,
    QPlainTextEditLogger,
    Ruleform,
)

import easydev
import colorlog

logger = colorlog.getLogger(__name__)


def sigint_handler(*args):  # pragma: no cover
    """Handler for the SIGINT signal."""
    sys.stderr.write("\r")
    if (
        QW.QMessageBox.question(
            None, "", "Are you sure you want to quit?", QW.QMessageBox.Yes | QW.QMessageBox.No, QW.QMessageBox.No
        )
        == QW.QMessageBox.Yes
    ):
        QW.QApplication.quit()


class BaseFactory:
    """Tab on top are all based on this abstract class

    It should provide access to a snakefile and its config file as well
    as working directory.

    Currently, the :class:`SequanaFactory` and :class:`GenericFactory` are
    implemented.

    """

    def __init__(self, mode, run_button):
        super(BaseFactory, self).__init__()
        self.mode = mode
        self._run_button = run_button
        self.logger = Logger()

        # And finally the working directory
        self._directory_browser = FileBrowser(directory=True)
        self._directory_browser.clicked_connect(self._switch_off_run)

    def _switch_off_run(self):  # pragma: no cover
        self.logger.debug("Switching off run button")
        self._run_button.setEnabled(False)

    def _copy(self, source, target):
        try:
            shutil.copy(source, target)
        except Exception as err:
            self.logger.error(err)
            self.logger.warning("Cannot overwrite existing file. (Probably identical)")

    def copy(self, source, target, force):  # pragma: no cover
        if os.path.exists(target) and force is False:
            save_msg = WarningMessage("The file <i>{0}</i> already exists in the working directory".format(source))
            save_msg.setInformativeText("Do you want to overwrite it?")
            save_msg.setStandardButtons(QW.QMessageBox.Yes | QW.QMessageBox.Discard | QW.QMessageBox.Cancel)
            save_msg.setDefaultButton(QW.QMessageBox.Yes)
            # Yes == 16384
            # Save == 2048
            retval = save_msg.exec_()
            if retval in [16384, 2048]:
                self.logger.warning("Overwritting %s" % target)
                self._copy(source, target)
        else:
            self._copy(source, target)

    def _copy_snakefile(self, force=False):  # pragma: no cover
        if self.snakefile is None:
            self.logger.info("No pipeline selected yet")
            return  # nothing to be done

        if self.directory is None:
            self.logger.info("No working directory selected yet (copy snakefile)")
            return

        # source and target filenames
        target = self.directory + os.sep + os.path.basename(self.snakefile)

        if os.path.exists(target) and easydev.md5(target) == easydev.md5(self.snakefile):
            self.logger.info("Target and source (pipeline) are identical. Skipping copy.")
            # if target and source are identical, nothing to do
            return

        # if filename are identical but different, do we want to overwrite it ?
        if os.path.basename(self.snakefile) == target:
            self.logger.warning("%s exists already in %s" % (self.snakefile, self.directory))
            return

        self.logger.info("Copying snakefile in %s " % self.directory)
        self.copy(self.snakefile, target, force=force)

    def _copy_configfile(self):  # pragma: no cover
        if self.configfile is None:
            self.logger.info("No config selected yet")
            return  # nothing to be done

        if self._directory_browser.path_is_setup() is False:
            self.logger.info("No working directory selected yet (copy config)")
            return

        # FIXME
        # This does not check the formatting so when saved, it is different
        # from original even though parameters are the same...
        target = self.directory + os.sep + os.path.basename(self.configfile)
        if os.path.exists(target) and easydev.md5(target) == easydev.md5(self.configfile):
            self.logger.info("Target and source (pipeline) are identical. Skipping copy.")
            return

        self.logger.info("Copying config in %s " % self.directory)
        self.copy(self.configfile, self.directory)

    def _get_directory(self):
        filename = self._directory_browser.get_filenames()
        if len(filename):
            return filename
        else:
            return None

    directory = property(_get_directory)

    def __repr__(self):
        return "%s Factory" % self.mode


class SequanaFactory(BaseFactory):
    def __init__(self, run_button, combobox):
        super(SequanaFactory, self).__init__("sequana", run_button)
        self._imported_config = None
        self._choice_button = combobox

        # Some widgets to be used: a file browser for paired files
        fastq_filter = "Fastq file (*.fastq *.fastq.gz *.fq *.fq.gz)"
        self._sequana_paired_tab = FileBrowser(paired=True, file_filter=fastq_filter)

        # Set the file browser input_directory tab
        self._sequana_directory_tab = FileBrowser(directory=True)

        # triggers/connectors
        self._sequana_directory_tab.clicked_connect(self._switch_off_run)
        self._choice_button.activated.connect(self._switch_off_run)
        self._sequana_paired_tab.clicked_connect(self._switch_off_run)

    def _get_pipeline(self):
        index = self._choice_button.currentIndex()
        if index == 0:
            return None
        else:
            return self._choice_button.currentText()

    pipeline = property(_get_pipeline)

    def _get_snakefile(self):
        if self.pipeline:
            module = snaketools.Module(self.pipeline)
            return module.snakefile

    snakefile = property(_get_snakefile)

    def _get_configfile(self):
        if self.pipeline:
            module = snaketools.Module(self.pipeline)
            return module.config

    configfile = property(_get_configfile)

    def _get_clusterconfigfile(self):
        if self.pipeline:
            module = snaketools.Module(self.pipeline)
            return module.cluster_config

    clusterconfigfile = property(_get_clusterconfigfile)

    def _get_multiqcconfigfile(self):
        if self.pipeline:
            module = snaketools.Module(self.pipeline)
            return module.multiqc_config

    multiqcconfigfile = property(_get_multiqcconfigfile)

    def _get_schemafile(self):
        if self.pipeline:
            module = snaketools.Module(self.pipeline)
            return module.schema_config

    schemafile = property(_get_schemafile)

    def _get_config(self):
        if self._imported_config:
            cfg = snaketools.SequanaConfig(self._imported_config)
            return cfg
        if self.configfile:
            try:
                cfg = snaketools.SequanaConfig(self.configfile)
                return cfg
            except AssertionError:
                self.logger.warning("Warning: could not parse the config file")
                return

    config = property(_get_config)

    def __repr__(self):  # pragma: no cover
        in1 = self._sequana_directory_tab.get_filenames()
        in2 = self._sequana_paired_tab.get_filenames()
        txt = super(SequanaFactory, self).__repr__()
        txt += "\npipeline:%s\ninput:\n - %s\n - %s\n - directory:%s\n"
        if self.clusterconfigfile:
            txt += " - cluster config: %s\n" % self.clusterconfigfile
        if self.schemafile:
            txt += " - schema config: %s" % self.schemafile
        if self.multiqcconfigfile:
            txt += " - schema config: %s" % self.multiqcconfigfile
        return txt % (self.pipeline, in1, in2, self.directory)


class GenericFactory(BaseFactory):
    def __init__(self, run_button):
        super(GenericFactory, self).__init__("generic", run_button)

        # Define the Snakefile browser and config widgets
        self._snakefile_browser = FileBrowser(directory=False)
        self._config_browser = FileBrowser(directory=False, file_filter="YAML file (*.json *.yaml *.yml)")

        # when a snakefile or config is chosen, switch off run button
        self._config_browser.clicked_connect(self._switch_off_run)
        self._snakefile_browser.clicked_connect(self._switch_off_run)
        self._schema = None
        self._multiqcconfigfile = None

    def _return_none(self, this):
        if this is None or len(this) == 0:
            return None
        else:
            return this

    def _get_snakefile(self):
        return self._return_none(self._snakefile_browser.get_filenames())

    snakefile = property(_get_snakefile)

    def _get_configfile(self):
        return self._return_none(self._config_browser.get_filenames())

    configfile = property(_get_configfile)

    def _get_schemafile(self):
        return self._return_none(self._schema)

    schemafile = property(_get_schemafile)

    def _get_multiqcconfigfile(self):
        return self._return_none(self._multiqcconfigfile)

    multiqcconfigfile = property(_get_multiqcconfigfile)

    def _get_config(self):  # pragma: no cover
        filename = self._return_none(self._config_browser.get_filenames())
        if filename:
            try:
                configfile = snaketools.SequanaConfig(filename)
            except AssertionError:
                self.logger.critical("Could not parse the config file %s" % filename)
                return
            except Exception:
                self.logger.critical("Could not parse the config file %s. 2" % filename)
                return
            return configfile

    config = property(_get_config)

    def is_runnable(self):
        flag1 = self._directory_browser.path_is_setup()
        flag2 = self._snakefile_browser.path_is_setup()
        flag3 = self._config_browser.path_is_setup()

        # flag1 and flag2 are compulsary
        # flag3 (configfile) is most tricky to handle since it may be required
        # or not. So we just deal with the flag1 and 2
        return flag1 and flag2

    def __repr__(self):
        txt = super(GenericFactory, self).__repr__()
        txt += "\nsnakefile:%s\nconfigfile:%s\ndirectory:%s\nschema:%s\nmultiqcconfigfile:%s"
        return txt % (self.snakefile, self.configfile, self.directory, self.schemafile, self.multiqcconfigfile)


class SequanixGUI(QW.QMainWindow):
    """

    If quiet, progress bar cannot work.

    - do not copy again requirements if already there
    - extension of the different widgets ?

    Developer Guide
    ------------------

    - The GUI is designed with qt designer as much as possible.
    - All GUI objects are in the **ui** attributes. Additional dialog such as the
      snakemake and preferences dialog have their own modules and stored in attributes
      ending in _dialog

    """

    _not_a_rule = {"requirements", "ignore"}
    _browser_keywords = {"reference"}
    _to_exclude = ["atac-seq", "compressor"]

    def __init__(self, parent=None, ipython=True, user_options={}):
        super(SequanixGUI, self).__init__(parent=parent)
        self.logger = Logger()

        colorlog.getLogger().setLevel("INFO")
        colorlog.info("Welcome to Sequana GUI (aka Sequanix)")

        self._tempdir = QTemporaryDir()
        self.shell = ""
        self.shell_error = ""
        self._colors = {
            "green": QtGui.QColor(0, 170, 0),
            "red": QtGui.QColor(170, 0, 0),
            "orange": QtGui.QColor(170, 150, 0),
            "blue": QtGui.QColor(0, 90, 154),
        }

        # some global attributes
        self._undefined_section = "Parameters in no sections/rules"

        # Set the regex to catch steps in the progres bar
        self._step_regex = re.compile("([0-9]+) of ([0-9]+) steps")

        self._ipython_tab = ipython
        self.initUI()
        self.read_settings()

        # this should be after initUI and read_settings
        self.set_style_sheet()

        # User option.
        def isset(options, key):
            if key in options and getattr(options, key):
                return True
            else:
                return False

        if isset(user_options, "wkdir"):
            self.logger.info("Setting working directory using user's argument %s" % user_options.wkdir)
            if os.path.exists(user_options.wkdir) is False:
                easydev.mkdirs(user_options.wkdir)
            # We must use the absolute path
            abspath = os.path.abspath(user_options.wkdir)
            self.sequana_factory._directory_browser.set_filenames(abspath)
            self.generic_factory._directory_browser.set_filenames(abspath)

        if isset(user_options, "snakefile"):
            filename = user_options.snakefile
            if os.path.exists(filename) is True:
                self.logger.info("Setting snakefile using user's argument %s" % user_options.snakefile)
                self.generic_factory._snakefile_browser.set_filenames(filename)
            else:
                self.logger.error("%s does not exist" % filename)
            self.ui.tabs_pipeline.setCurrentIndex(1)

        if isset(user_options, "configfile"):
            filename = user_options.configfile
            if os.path.exists(filename) is True:
                self.logger.info("Setting config file using user's argument %s" % user_options.configfile)
                self.generic_factory._config_browser.set_filenames(filename)
            self.ui.tabs_pipeline.setCurrentIndex(1)

        if isset(user_options, "pipeline"):  # pragma: no cover
            self.logger.info("Setting Sequana pipeline %s " % user_options.pipeline)
            pipelines = self.sequana_factory.valid_pipelines

            if user_options.pipeline in pipelines:
                index = self.ui.choice_button.findText(user_options.pipeline)
                self.ui.choice_button.setCurrentIndex(index)
                # set focus on pipeline tab
                self.ui.tabs_pipeline.setCurrentIndex(0)
            else:
                self.logger.error("unknown pipeline. Use one of %s " % pipelines)

        self._user_input_pattern = None
        self._user_input_directory = None

        if isset(user_options, "input_directory"):  # pragma: no cover
            directory = user_options.input_directory
            self.logger.info("Setting Sequana input directory")
            if directory and os.path.exists(directory) is False:
                self.logger.warning("%s does not exist" % directory)
            elif directory:
                abspath = os.path.abspath(user_options.input_directory)
                self._user_input_directory = directory

        if isset(user_options, "input_pattern"):  # pragma: no cover
            self.logger.info("Setting Sequana input pattern")
            self._user_input_pattern = user_options.input_pattern

        if isset(user_options, "sequana_configfile"):
            cfg = user_options.sequana_configfile
            self.logger.info("Replace Sequana config file")
            self.menuImportConfig(cfg)

        if isset(user_options, "schemafile"):
            schemafile = user_options.schemafile
            self.logger.info("Set the schema file")
            self.menuImportSchema(schemafile)

        # We may have set some pipeline, snakefile, working directory
        self.create_base_form()

    def initUI(self):
        # The logger is not yet set, so we use the module directly
        colorlog.info("Initialising GUI")

        # Set up the user interface from Designer. This is the general layout
        # without dedicated widgets and connections
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 2 more dialogs from designer
        self.preferences_dialog = PreferencesDialog(self)
        self.snakemake_dialog = SnakemakeDialog(self)
        self.preferences_dialog.ui.buttonBox.accepted.connect(self.set_level)

        # The IPython dialog, which is very useful for debugging
        if self._ipython_tab is True:
            self.ipyConsole = QIPythonWidget(
                customBanner="Welcome to Sequanix embedded ipython console\n"
                + "The entire GUI interface is stored in the variable gui\n"
                + "Note also that you can use this interface as a shell \n"
                + "command line interface preceding your command with ! character\n"
            )
            self.ipyConsole.pushVariables({"gui": self})
            self.ui.layout_ipython.addWidget(self.ipyConsole)

        # layout for config file parameters
        widget_form = QW.QWidget()
        self.form = QW.QVBoxLayout(widget_form)
        self.form.setSpacing(10)
        self.ui.scrollArea.setWidget(widget_form)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setMinimumHeight(200)

        # layout for the snakemake output
        self.output = QW.QTextEdit()
        self.output.setReadOnly(True)
        self.ui.layout_snakemake.addWidget(self.output)

        # Add the new logging box widget to the layout
        self.logTextBox = QPlainTextEditLogger(self)
        self.logTextBox.setFormatter(
            colorlog.ColoredFormatter(
                "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
                log_colors={
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                },
            )
        )
        colorlog.getLogger().addHandler(self.logTextBox)
        self.set_level()
        self.ui.layout_logger.addWidget(self.logTextBox.widget)

        # Connectors to actions related to the menu bar
        self.ui.actionQuit.triggered.connect(self.menuQuit)
        self.ui.action_import_configfile.triggered.connect(self.menuImportConfig)
        self.ui.action_import_schemafile.triggered.connect(self.menuImportSchema)
        self.ui.actionHelp.triggered.connect(self.menuHelp)
        self.ui.actionAbout.triggered.connect(self.menuAbout)
        self.ui.actionSnakemake.triggered.connect(self.snakemake_dialog.exec_)
        self.ui.actionPreferences.triggered.connect(self.preferences_dialog.exec_)

        self.preferences_dialog.ui.preferences_options_general_tooltip_value.clicked.connect(self.set_style_sheet)

        # connectors related to the pipeline tabs (pipeline/generic)
        self.set_sequana_pipeline()
        self.set_generic_pipeline()

        # The run/save/dag footer buttons
        self.connect_footer_buttons()

        self.process = QtCore.QProcess(self)
        self.process.started.connect(lambda: self.ui.run_btn.setEnabled(False))
        self.process.started.connect(lambda: self.ui.stop_btn.setEnabled(True))
        self.process.started.connect(lambda: self.ui.unlock_btn.setEnabled(False))
        self.process.started.connect(lambda: self.start_progress)
        self.process.started.connect(lambda: self.ui.save_btn.setEnabled(False))
        self.process.started.connect(lambda: self.ui.tabs_pipeline.setEnabled(False))

        self.process.finished.connect(lambda: self.ui.run_btn.setEnabled(True))
        self.process.finished.connect(lambda: self.ui.stop_btn.setEnabled(False))
        self.process.finished.connect(lambda: self.ui.unlock_btn.setEnabled(True))
        self.process.finished.connect(lambda: self.ui.save_btn.setEnabled(True))
        self.process.finished.connect(lambda: self.ui.tabs_pipeline.setEnabled(True))
        self.process.finished.connect(self.end_run)

        self.process.readyReadStandardOutput.connect(self.snakemake_data_stdout)
        self.process.readyReadStandardError.connect(self.snakemake_data_error)

        # This is for the show dag btn. Created here once for all
        self.process1 = QtCore.QProcess(self)
        self.process2 = QtCore.QProcess(self)

        #self.ui.tabWidget.currentChanged.connect(lambda: self.ui.run_btn.setEnabled(False))

        # if we are on one of those clusters, switch to the cluster choice in
        # the pipeline control combo box
        if on_cluster() is True:
            self.ui.comboBox_local.setCurrentText("cluster")

    def _get_opacity(self):
        dialog = self.preferences_dialog
        box = dialog.ui.preferences_options_general_tooltip_value
        if box.isChecked():
            return 255
        else:
            return 0

    tooltip_opacity = property(_get_opacity)

    def set_style_sheet(self):
        self.setStyleSheet(
            """QToolTip {
                           background-color: #aabbcc;
                           color: black;
                           border-style: double;
                           border-width: 3px;
                           border-color: green;
                           border-radius: 5px;
                           margin:5px;
                           opacity: %s;
                           } ;

                            """
            % self.tooltip_opacity
        )

    # |-----------------------------------------------------|
    # |                       MENU related                  |
    # |-----------------------------------------------------|
    def menuImportConfig(self, configfile=None):  # pragma: no cover
        # The connector send a False signal but default is None
        # so we need to handle the two cases
        if self.snakefile is None:
            self.logger.error("You must set a pipeline first")
            msg = WarningMessage(("You must set a pipeline first"))
            msg.exec_()
            return

        if configfile and os.path.exists(configfile) is False:
            self.logger.error("Config file (%s) does not exists" % configfile)
            return

        if configfile is None or configfile is False:
            self.logger.info("Importing config file.")
            file_filter = "YAML file (*.json *.yaml *.yml)"
            browser = FileBrowser(file_filter=file_filter)
            browser.browse_file()
            configfile = browser.paths

        if configfile:
            self.sequana_factory._imported_config = configfile
        else:
            self.sequana_factory._imported_config = None
        self.create_base_form()

    def menuImportSchema(self, schemafile=None):  # pragma: no cover
        if schemafile:
            self.generic_factory._schema = schemafile
            return

        self.logger.info("Importing YAML schema file.")
        file_filter = "YAML file (*.yaml *.yml)"
        browser = FileBrowser(file_filter=file_filter)
        browser.browse_file()
        schemafile = browser.paths
        if schemafile:
            self.generic_factory._schema = schemafile
        else:
            self.generic_factory._schema = None

    def menuAbout(self):
        from sequanix import version

        url = "sequana.readthedocs.io"
        widget = About()
        widget.setText("Sequanix version %s " % version)
        widget.setInformativeText(
            """Sequanix was originally part of Sequana, which online documentation is available on <a
href="http://%(url)s">%(url)s</a>. Sequanix is now independent with its own <a
href="https://github.com/sequana/sequanix">github repository</a>.
            <br><br>
            How to cite: Desvillechabrol et al (2018), Sequanix: A Dynamic Graphical Interface for Snakemake Workflows.
Bioinformatics v34, <a href="https://doi.org/10.1093/bioinformatics/bty034">doi.org/10.1093/bioinformatics/bty034</a>
            <br><br>

            Authors: Thomas Cokelaer and Dimitri Desvillechabrol, 2017-2018
            """
            % {"url": url}
        )
        widget.setWindowTitle("Sequanix from Sequana project")
        retval = widget.exec_()
        if retval == QW.QMessageBox.Ok:
            widget.close()

    def menuHelp(self):
        url = "sequana.readthedocs.io"
        pipelines_text = "<ul>\n"
        url = "http://github.com/sequana/"
        for pipeline in snaketools.pipeline_names:
            name = pipeline.replace("pipeline:", "")
            pipelines_text += f'    <li><a href="{url}/{name}">{pipeline}</a></li>\n'
        pipelines_text += "</ul>"

        msg = HelpDialog(pipelines=pipelines_text)
        retval = msg.exec_()
        if retval == QW.QMessageBox.Ok:
            msg.close()

    def menuQuit(self):
        self._quit_msg = WarningMessage("Do you really want to quit ?")
        self._quit_msg.setStandardButtons(QW.QMessageBox.Yes | QW.QMessageBox.No)
        self._quit_msg.setDefaultButton(QW.QMessageBox.No)
        quit_answer = self._quit_msg.exec_()
        if quit_answer == QW.QMessageBox.Yes:
            self.close()

    def set_level(self):
        # Set the level of the logging system
        pref = self.preferences_dialog.ui
        level = pref.preferences_options_general_logging_value.currentText()
        level = colorlog.getLogger().level
        colorlog.getLogger().setLevel(level)

    # ---------------------------------------------------------------
    # More GUI / reading the snakefile (sequana or generic)
    # ---------------------------------------------------------------
    def set_sequana_pipeline(self):
        # The pipeline connectors
        pipelines = sorted(snaketools.pipeline_names)
        pipelines = [this for this in pipelines if this not in self._to_exclude]
        self.ui.choice_button.addItems(pipelines)
        self.ui.choice_button.activated[int].connect(self._update_sequana)

        # FIXME do we want to use this ?
        self.ui.choice_button.installEventFilter(self)

        # populate the factory with the choice button
        self.sequana_factory = SequanaFactory(combobox=self.ui.choice_button, run_button=self.ui.run_btn)
        self.sequana_factory.valid_pipelines = pipelines

        # a local alias
        saf = self.sequana_factory

        # add widgets for the working dir
        self.ui.layout_sequana_wkdir.addWidget(saf._directory_browser)

    @pyqtSlot(str)
    def _update_sequana(self, index):
        """Change options form when user changes the pipeline."""
        if self.ui.choice_button.findText(str(index)) == 0:
            self.clear_form()
            self.rule_list = []
            return

        self.logger.info("Reading sequana %s pipeline" % index)
        self.create_base_form()
        # Is there a cluster config file ?
        dialog = self.snakemake_dialog.ui

        if self.sequana_factory.clusterconfigfile:
            dialog.snakemake_options_cluster_cluster__config_value.set_filenames(self.sequana_factory.clusterconfigfile)
        else:
            dialog.snakemake_options_cluster_cluster__config_value.set_filenames("")
        self.switch_off()
        # Reset imported config file in SequanaFactory
        self.sequana_factory._imported_config = None

    def set_generic_pipeline(self):

        self.generic_factory = GenericFactory(self.ui.run_btn)
        gaf = self.generic_factory

        # The config file connectors
        gaf._config_browser.clicked_connect(self.create_base_form)

        # Update the main UI with
        self.ui.layout_generic_snakefile.addWidget(gaf._snakefile_browser)
        self.ui.layout_generic_config.addWidget(gaf._config_browser)
        self.ui.layout_generic_wkdir.addWidget(gaf._directory_browser)

        # When user press the cancel button, the config file browser is reset
        self.ui.cancel_push_button.clicked.connect(self.generic_factory._config_browser.set_empty_path)

    # ---------------------------------------------------------------------
    # Footer connectors
    # ---------------------------------------------------------------------

    def connect_footer_buttons(self):
        self.ui.run_btn.setEnabled(False)
        self.ui.run_btn.clicked.connect(self.click_run)

        self.ui.stop_btn.clicked.connect(self.click_stop)
        self.ui.stop_btn.setEnabled(False)

        self.ui.unlock_btn.clicked.connect(self.ui.run_btn.setEnabled)
        self.ui.unlock_btn.clicked.connect(self.unlock_snakemake)
        self.ui.unlock_btn.setEnabled(True)

        self.ui.report_btn.setEnabled(True)
        self.ui.report_btn.clicked.connect(self.open_report)

        self.ui.save_btn.clicked.connect(self.save_project)

        self.ui.dag_btn.setEnabled(False)
        self.ui.dag_btn.clicked.connect(self.show_dag)

    # -----------------------------------------------------------------
    # function to link to the factory (sequana or generic)
    # -----------------------------------------------------------------

    def _get_mode(self):
        # figure out if we are dealing with a sequana pipeline or not
        index = self.ui.tabs_pipeline.currentIndex()
        if index == 0:
            return "sequana"
        elif index == 1:
            return "generic"

    mode = property(_get_mode)

    def _get_factory(self):
        return getattr(self, "%s_factory" % self.mode)

    factory = property(_get_factory)

    def _get_config(self):
        return getattr(self, "%s_factory" % self.mode).config

    config = property(_get_config)

    def _get_configfile(self):
        return getattr(self, "%s_factory" % self.mode).configfile

    configfile = property(_get_configfile)

    def _get_snakefile(self):
        return getattr(self, "%s_factory" % self.mode).snakefile

    snakefile = property(_get_snakefile)

    def _get_working_dir(self):
        return getattr(self, "%s_factory" % self.mode).directory

    working_dir = property(_get_working_dir)

    # ----------------------------------------------------------
    #  Config file related
    # ---------------------------------------------------------

    def _set_focus_on_config_tab(self):
        # Set focus on config file
        if self._ipython_tab:
            self.ui.tabs.setCurrentIndex(3)
        else:
            self.ui.tabs.setCurrentIndex(2)

    # --------------------------------------------------------------------
    # Others
    # --------------------------------------------------------------------

    def clear_layout(self, layout):
        """Clean all widgets contained in a layout."""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clear_layout(child.layout())

    # --------------------------------------------------------------------
    # Running snakemake
    # --------------------------------------------------------------------

    def _clean_line(self, line):
        # TODO: surely there is a better way to do that and not overlap
        # with tools.py ...
        line = line.replace("b'\\r'", "")
        line = line.replace("b'\r'", "")
        line = line.replace("b'\\r '", "")
        line = line.replace("b'\r '", "")
        line = line.replace("b' '", "")
        line = line.replace("\\t", "&nbsp;" * 4)
        line = line.replace("'b'", "")
        for this in ["b'", 'b"', "\r"]:
            if line.startswith(this):
                line = line.replace(this, "")
        if line.startswith('b"'):
            line = line.replace('b"', "")
        line = line.rstrip("\\x1b[0m")
        line = line.replace("\\x1b[33m", "")
        return line

    def snakemake_data_stdout(self):  # pragma: no cover
        """Read standard output of snakemake process"""
        data = str(self.process.readAllStandardOutput())
        self.shell += data
        self.update_progress_bar(data)

        for this in data.split("\\n"):
            line = this.strip()
            if line and len(line) > 3 and "complete in" not in line:  # prevent all b'' strings
                line = self._clean_line(line)
                if len(line.strip()) == 0:
                    continue
                self.output.append('<font style="color:blue">' + line + "</font>")

    def snakemake_data_error(self):
        """Read error output of snakemake process"""
        error = str(self.process.readAllStandardError())
        self.shell_error += error
        self.update_progress_bar(error)
        for this in error.split("\\n"):
            line = this.strip()
            if line and len(line) > 3 and "complete in" not in line:  # prevent all b'' strings
                line = self._clean_line(line)
                if line.startswith("b'"):
                    line = line[2:]
                    line.rstrip("'")
                grouprex = self._step_regex.findall(line)
                if grouprex:
                    self.output.append('<font style="color:orange">' + line + "</font>")
                elif "Error" in line:
                    self.output.append('<font style="color:red">' + line + "</font>")
                else:
                    self.output.append('<font style="color:green">' + line + "</font>")

    def _get_snakemake_command(self, snakefile):  # pragma: no cover
        """If the cluster option is selected, then the cluster field in
        the snakemake menu must be set to a string different from empty string.

        If we are on TARS, we also must set the option to cluster (not local)

        If one of the previous cases is true, this function returns None

        """
        dialog = self.snakemake_dialog  # an alias
        # let us remove --stat stats.txt to make it simple (v0.2)
        #snakemake_line = ["-s", snakefile, "--stat", "stats.txt", "-p"]
        snakemake_line = ["-s", snakefile, "-p"]

        if self.ui.comboBox_local.currentText() == "local":
            if on_cluster():
                msg = WarningMessage(
                    (
                        "You are on a SLURM scheduler. Please set the"
                        "sbatch options and select the cluster option (not local)"
                    )
                )
                msg.exec_()
                return None
            snakemake_line += dialog.get_snakemake_local_options()
        elif self.ui.comboBox_local.currentText() == "cluster":
            cluster = dialog.ui.snakemake_options_cluster_cluster_value.text()
            if len(cluster.strip()) == 0:
                msg = WarningMessage(
                    (
                        "You selected a 'cluster run' but the "
                        "cluster preferences are not set. Either switch to a local "
                        "run or set a correct string in the Snakemake options menu "
                        "(in cluster tab/ cluster field.)"
                    )
                )
                msg.exec_()
                return None
            snakemake_line += dialog.get_snakemake_cluster_options()

        snakemake_line += dialog.get_snakemake_general_options()

        # add --wrapper option if any provided in the preferences dialog
        snakemake_line += self._get_wrapper()

        # apptainers
        action_apptainer = self.ui.action_apptainer
        if action_apptainer.isChecked():
            snakemake_line += ["--use-singularity"]
            if self.mode == "sequana":
                prefix = self.preferences_dialog.ui.preferences_options_sequana_apptainer_value.text()
                if prefix.strip():
                    snakemake_line += f"--singularity-prefix {prefix}".split()
                args = self.preferences_dialog.ui.preferences_options_sequana_apptainer_args_value.text()
                if args.strip():
                    snakemake_line += f"--singularity-args {args}".split()
            else:
                prefix = self.preferences_dialog.ui.preferences_options_general_apptainer_value.text()
                if prefix.strip():
                    snakemake_line += f"--singularity-prefix {prefix}".split()
                args = self.preferences_dialog.ui.preferences_options_general_apptainer_args_value.text()
                if args.strip():
                    snakemake_line += f"--singularity-args {args}".split()

        # other options provided in the dialog
        others = self.snakemake_dialog.ui.snakemake_options_general_custom.text()
        if others.strip():
            snakemake_line += others.split()

        if self.configfile:
            configfile = os.path.basename(self.configfile)
            snakemake_line += ["--configfile", configfile]

        return snakemake_line

    def _get_wrapper(self):

        # by default, no wrapper used
        snakemake_cmd = []

        # add --wrapper option if any provided in the preferences dialog
        if self.mode == "sequana":
            # for sequana, we use it anyway.
            wrapper = self.preferences_dialog.ui.preferences_options_sequana_wrapper_value.text()
            wrapper = wrapper.strip()
            if wrapper:
                if not wrapper.endswith("/"):
                    wrapper += "/"
                snakemake_cmd += f"--wrapper-prefix {wrapper}".split()
        else:
            # for other generic pipeline, we use it if provided
            wrapper = self.preferences_dialog.ui.preferences_options_general_wrapper_value.text()
            wrapper = wrapper.strip()
            if wrapper:
                if not wrapper.endswith("/"):
                    wrapper += "/"
                snakemake_cmd += f"--wrapper-prefix {wrapper}".split()

        return snakemake_cmd

    def _set_pb_color(self, color):
        self.ui.progressBar.setStyleSheet(
            """
            QProgressBar {{
                color: black;
                border: 2px solid grey;
                margin: 2px;
                border-radius: 5px;
                text-align: center;
            }}
            QProgressBar::chunk {{
                background: {};
                }}""".format(
                color
            )
        )

    def click_run(self):
        # set focus on the snakemake output
        if self.snakefile is None or self.working_dir is None:
            self.logger.warning("Working directory or snakefile not set.")
            return
        self.ui.tabs.setCurrentIndex(0)
        self.shell_error = ""
        self.shell = ""

        # Prepare the command and working directory.
        if self.working_dir is None:
            self.logger.warning("Set the working directory first")
            return

        # We copy the sequana and generic snakefile into a filename called
        # Snakefile
        snakefile = self.working_dir + os.sep + os.path.basename(self.snakefile)

        if os.path.exists(snakefile) is False:
            self.logger.critical("%s does not exist" % snakefile)
            return

        snakemake_args = self._get_snakemake_command(snakefile)
        if snakemake_args is None:
            return

        # the progress bar
        self._set_pb_color(self._colors["blue"].name())
        self.ui.progressBar.setValue(1)

        # Start process
        # If an argument contains spaces, we should use quotes. However,
        # with PyQt quotes must be escaped

        args = []
        for this in snakemake_args:
            if re.search(r"\s", this) is True:
                args.append('"%s"' % this)
            else:
                args.append(this)
        snakemake_args = args
        self.logger.info("Starting process with snakemake %s " % " ".join(snakemake_args))
        self.output.clear()
        self.process.setWorkingDirectory(self.working_dir)
        self.process.start("snakemake", snakemake_args)

    # -------------------------------------------------------------------
    # Create the base form
    # -------------------------------------------------------------------
    def create_base_form(self):
        """Create form with all options necessary for a pipeline.

        ::

            ########################################################
            #   valid python docstring to be interepreted by sphinx
            #
            #   section:
            #      item1: 10
            #      item2: 20

        """
        if self.config is None:
            self.clear_form()
            return

        self.logger.info("Creating form based on config file")
        self.clear_form()


        rules_list = list(self.config._yaml_code.keys())

        # key/value not in rules
        self.necessary_dict = {}


        docparser = YamlDocParser(self.configfile)
        import ruamel.yaml.comments

        # place holder for all rule boxes
        rule_boxes = []

        for count, rule in enumerate(rules_list):
            self.logger.debug("Scanning rule %s" % rule)
            # Check if this is a dictionnary
            contains = self.config._yaml_code[rule]

            # If this is a section/dictionary, create a section
            if isinstance(contains, (ruamel.yaml.comments.CommentedMap, dict)) and (
                rule not in SequanixGUI._not_a_rule
            ):
                # Get the docstring from the Yaml section/rule
                docstring = docparser._block2docstring(rule)

                # Get any special keywords
                specials = docparser._get_specials(rule)
                logger.debug(f"In rule {rule} found {specials}")

                # self.ui.preferences_options_general_addbrowser_value
                dialog = self.preferences_dialog.ui
                option = dialog.preferences_options_general_addbrowser_value.text()
                option = option.strip()
                option = option.replace(";", " ").replace(",", " ")

                if len(option):
                    keywords = option.split()
                else:
                    keywords = []
                keywords += self._browser_keywords
                keywords = list(set(keywords))

                rule_box = Ruleform(rule, contains, count, keywords, specials=specials)
                rule_box.connect_all_option(lambda: self.ui.run_btn.setEnabled(False))

                # Try to interpret it with sphinx

                try:
                    self.logger.debug("parsing docstring of %s" % rule)
                    comments = rest2html(docstring).decode()
                    rule_box.setToolTip(comments)
                except Exception as err:
                    print(err)
                    self.logger.warning("Could not interpret docstring of %s" % rule)
                    rule_box.setToolTip("")

                rule_boxes.append(rule_box)
            else:
                # The first time sequanix is launched, we fill the form with the possible
                # user input_directory and input_pattern if provided. If so, we reset them
                #
                if self.mode == "sequana":
                    if rule ==  'input_directory' and self._user_input_directory:
                        contains = self._user_input_directory
                        self._user_input_directory = None
                    if rule ==  'input_pattern' and self._user_input_pattern:
                        contains = self._user_input_pattern
                        self._user_input_pattern = None

                # field/key in no section, which may be
                # a list, a None or something else
                if isinstance(contains, list):
                    self.necessary_dict = dict(self.necessary_dict, **{rule: contains})
                elif contains is None or contains in ["''", '""']:
                    self.necessary_dict = dict(self.necessary_dict, **{rule: None})
                else:
                    self.necessary_dict = dict(self.necessary_dict, **{rule: "{0}".format(contains)})

        if len(self.necessary_dict):
            if self.mode == "generic":
                rule_box = Ruleform(self._undefined_section, self.necessary_dict, -1, generic=True)
            else:
                rule_box = Ruleform(self._undefined_section, self.necessary_dict, -1, generic=False)
            rule_boxes.insert(0, rule_box)

        # now add all rule boxes in the form
        for rule_box in rule_boxes:
            self.form.addWidget(rule_box)

        self._set_focus_on_config_tab()

    # ----------------------------------------------------------
    # STOP footer button
    # ----------------------------------------------------------

    def click_stop(self):
        """The stop button"""
        self._set_pb_color(self._colors["orange"].name())

        # For windows:
        # http://stackoverflow.com/questions/8232544/how-to-terminate-a-process-without-os-kill-osgeo4w-python-2-5

        if self.process.state() != 0:
            self.process.pid = self.process.processId
            pid = self.process.pid()
            #pid = self.process.processId

            self.logger.warning(f"Process {pid} running , stopping it... ")
            # We must use a ctrl+C interruption so that snakemake
            # handles the interruption smoothly. However, child processes
            # are lost so we also need to get their IDs and kill them.
            self.logger.info("killing the main snakemake process. This may take a few seconds ")
            try:
                self.logger.info(f"process pid={pid} being killed")
                pid_children = [this.pid for this in psutil.Process(pid).children(recursive=True)]
                # Kills the main process
                os.kill(pid, signal.SIGINT)
                # And the children
                for this in pid_children:  # pragma: no cover
                    self.logger.info(f"Remove pid {this} ")
                    try:
                        os.kill(this, signal.SIGINT)
                    except Exception as err:
                        print(err)
                time.sleep(4)

            except Exception as err:
                print(err)
                pass  # already stopped ?
            self.logger.info("Process killed successfully.")
        self.ui.save_btn.setEnabled(True)
        self.ui.run_btn.setEnabled(True)
        self.ui.stop_btn.setEnabled(False)
        self.ui.tabs_pipeline.setEnabled(True)

    # --------------------------------------------------------------------
    # Progress bar
    # --------------------------------------------------------------------

    def update_progress_bar(self, line):
        """Parse with a regex to retrieve current step and total step."""
        grouprex = self._step_regex.findall(line)
        # Use last "x of y" (not the first item at position 0)
        if grouprex:
            step = int(grouprex[-1][0]) / float(grouprex[-1][1]) * 100
            self.ui.progressBar.setValue(step)
        if "Nothing to be done" in line:
            self.ui.progressBar.setValue(100)

    def start_progress(self):
        self.ui.progressBar.setRange(0, 1)

    def end_run(self):  # pragma: no cover
        if self.ui.progressBar.value() >= 100:
            self._set_pb_color(self._colors["green"].name())
            self.logger.info("Run done. Status: successful")
        else:
            self._set_pb_color(self._colors["red"].name())
            text = "Run manually to check the exact error or check the log."
            if "--unlock" in self.shell_error:
                text += "<br>You may need to unlock the directory. "
                text += "click on Unlock button"
                self.logger.critical(text)
            return

    def _get_force(self):
        dialog = self.preferences_dialog
        box = dialog.ui.preferences_options_general_overwrite_value
        return box.isChecked()

    def _set_force(self, boolean):  # pragma: no cover
        assert boolean in [True, False]
        dialog = self.preferences_dialog
        box = dialog.ui.preferences_options_general_overwrite_value
        box.setChecked(boolean)

    force = property(_get_force, _set_force)

    def save_project(self):  # pragma: no cover
        self.logger.info("Saving project")

        if self.configfile is None:
            if self.mode == "generic":
                if self.generic_factory.is_runnable():
                    self.logger.critical("save_project: Generic case without config file")
                    self._save_teardown()
                else:
                    msg = WarningMessage("You must select a Snakefile and a working directory.")
                    msg.exec_()
            elif self.mode == "sequana":
                msg = WarningMessage("You must choose a pipeline first.")
                msg.exec_()
            return

        if self.working_dir is None:
            self.logger.critical("save_project: no working dir: return")
            msg = WarningMessage("You must select a working directory first.")
            msg.exec_()
            return

        try:
            form_dict = dict(self.create_form_dict(self.form), **self.necessary_dict)
        except AttributeError as err:
            self.logger.error(err)
            msg = WarningMessage("You must choose a pipeline before saving.")
            msg.exec_()
            return

        # Here we save the undefined section in the form.
        if self._undefined_section in form_dict.keys():
            for key, value in form_dict[self._undefined_section].items():
                form_dict[key] = value
            del form_dict[self._undefined_section]

        # Let us update the attribute with the content of the form
        # This uses the user's information

        cfg = self.config
        cfg.config.update(form_dict)
        cfg._update_yaml()
        self.cfg = cfg

        pref = self.preferences_dialog.ui
        box = pref.preferences_options_general_schema_value
        checked_schema = box.isChecked()

        if self.working_dir:
            # Save the configuration file
            if self.mode == "sequana":
                yaml_path = self.working_dir + os.sep + "config.yaml"
                self.logger.warning("copy requirements (if any)")
                try:
                    cfg.copy_requirements(target=self.working_dir)
                except AttributeError:
                    pass
            elif self.mode == "generic":
                yaml_path = os.sep.join((self.working_dir, os.path.basename(self.generic_factory.configfile)))

            if os.path.isfile(yaml_path) and self.force is False:
                save_msg = WarningMessage("The file <i>{0}</i> already exist".format(yaml_path))
                save_msg.setInformativeText("Do you want to overwrite the file?")
                save_msg.setStandardButtons(QW.QMessageBox.Yes | QW.QMessageBox.Discard | QW.QMessageBox.Cancel)
                save_msg.setDefaultButton(QW.QMessageBox.Yes)
                # Yes == 16384
                # Save == 2048
                retval = save_msg.exec_()
                if retval in [16384, 2048]:
                    self.logger.info("Saving config file (exist already)")
                    if checked_schema is False:
                        cfg.save(yaml_path)
                    else:
                        ret = self._check_and_save_config(cfg, yaml_path)
                        if ret is False:
                            # we do not want to save the config file and call
                            # _save_teardown
                            return
            else:
                self.logger.warning("Saving config file (does not exist)")
                if checked_schema is False:
                    cfg.save(yaml_path)
                else:
                    ret = self._check_and_save_config(cfg, yaml_path)
                    if ret is False:
                        # we do not want to save the config file and call
                        # _save_teardown
                        return

            # Save the configuration file for the cluster
            if self.mode == "sequana" and self.sequana_factory.clusterconfigfile:
                target = os.sep.join((self.working_dir, "cluster_config.json"))
                shutil.copy(self.sequana_factory.clusterconfigfile, target)
                # replace the name of the original file with the target one so
                # that the target can be edited. The target will also be used in
                # place of the original version when launnching snakemake!
                self.snakemake_dialog.ui.snakemake_options_cluster_cluster__config_value.set_filenames(target)

            # Save the multiqc_config file if provided in sequana pipeline
            if self.mode == "sequana" and self.sequana_factory.multiqcconfigfile:
                target = self.working_dir + os.sep + "multiqc_config.yaml"
                shutil.copy(self.sequana_factory.multiqcconfigfile, target)

        else:
            self.logger.critical("Config file not saved (no wkdir)")
            msg = WarningMessage("You must set a working directory", self)
            msg.exec_()
            self.switch_off()
            return

        self._save_teardown()

    def _save_teardown(self):
        # Finally, save project and update footer run button
        self.factory._copy_snakefile(self.force)
        self.logger.debug("Switching RUN and DAG button on")
        self.ui.run_btn.setEnabled(True)
        self.ui.dag_btn.setEnabled(True)

    def _check_and_save_config(self, cfg, yaml_path):
        # Here we save the config.yaml file when changed
        # However, before that if there is a schema, we can
        # use it. This is the case for some sequana pipelines

        # return False if the config is invalid and do not save it

        if self.mode == "sequana" and self.sequana_factory.schemafile is None:
            self.logger.warning("No Schema found to validate the config file")

        if self.mode == "sequana" and self.sequana_factory.schemafile:
            schemafile = self.sequana_factory.schemafile
        elif self.mode == "generic" and self.generic_factory.schemafile:
            schemafile = self.generic_factory.schemafile
        else:
            schemafile = None

        if schemafile:
            # check that the config file is correct before saving it
            # only if we have a schema_config file.
            self.logger.info("Checking config file with provided schema file.")
            # We save the config as a dummy temporary file to check it
            # if correct, we then save the file. If not, we provide an help
            # message
            from easydev import TempFile

            with TempFile(suffix=".yaml") as fout:
                # save a temporary version
                cfg.save(fout.name)
                import ruamel
                import warnings
                from pykwalify.core import Core

                # causes issue with ruamel.yaml 0.12.13. Works for 0.15
                try:
                    warnings.simplefilter("ignore", ruamel.yaml.error.UnsafeLoaderWarning)
                except Exception:
                    pass

                try:
                    # open the config and the schema file
                    c = Core(source_file=fout.name, schema_files=[schemafile])
                except Exception as err:
                    print(err)
                    return False

                try:
                    c.validate()
                except Exception as err:
                    print(err)
                    error_msg = "<b>CRITICAL: INVALID CONFIGURATION FILE</b>\n"
                    error_msg += "<pre>" + str(err) + "</pre>"
                    self.logger.critical(error_msg)
                    self.switch_off()
                    msg = WarningMessage(error_msg, self)
                    msg.exec_()
                    return False
        cfg.save(yaml_path)

    def switch_off(self):
        self.logger.debug("Switching RUN and DAG button off")
        self.ui.run_btn.setEnabled(False)
        self.ui.dag_btn.setEnabled(False)

    def _reset_schema(self):
        self.schemafile = None

    # -----------------------------------------------------------------------
    # UNLOCK footer button
    # -----------------------------------------------------------------------

    def unlock_snakemake(self):
        if self.working_dir is None or self.snakefile is None:
            self.logger.warning("working directory or snakefile not set")
            return

        # FIXME this does not work as expected
        self.ui.run_btn.setEnabled(False)

        if os.path.exists(self.snakefile) is False:
            self.logger.warning("snakefile not found. should not happen")
            return

        self.cmd = ["snakemake", "-s", self.snakefile, "--unlock"]
        self.logger.info("Running " + " ".join(self.cmd))
        self.logger.info("Please wait a second. Unlocking working directory")
        # focus on tab with snakemake output
        self.ui.tabs.setCurrentIndex(0)

        self.ui.tabs_pipeline.setEnabled(False)
        try:
            snakemake_proc = sp.Popen(self.cmd, cwd=self.working_dir)
            snakemake_proc.wait()
        except:
            self.logger.critical("Issue while unlocking the directory")
        finally:
            self.ui.tabs_pipeline.setEnabled(True)

        self.logger.info("unlocking done")
        self.output.append('<font style="color:brown">Unlocking working directory</font>')

        self.ui.run_btn.setEnabled(True)
        self.ui.stop_btn.setEnabled(False)

    # -----------------------------------------------------------------------
    # DAG footer button
    # -----------------------------------------------------------------------

    def show_dag(self):  # pragma: no cover
        try:
            # This command should work on various platform, just in case
            # we add a try/except
            if easydev.cmd_exists("dot") is False:
                msg = "**dot** command not found. Use 'conda install graphviz' to install it."
                self.logger.warning(msg)
                msg = WarningMessage((msg))
                msg.exec_()
                return
        except:
            pass
        finally:
            self.logger.info("Creating DAG image.")

        if self.snakefile is None:
            self.logger.warning("No snakefile")
            return

        # We just need the basename because we will run it in the wkdir
        snakefile = os.path.basename(self.snakefile)
        snakemake_line = ["snakemake", "-s", snakefile]
        snakemake_line += ["--rulegraph"]
        snakemake_line += self._get_wrapper()
        if self.mode == "generic" and self.configfile:
            # make sure to copy the config file
            snakemake_line += ["--configfile"]
            snakemake_line += [os.path.basename(self.generic_factory.configfile)]

        # Where to save the SVG (temp directory)
        svg_filename = self._tempdir.path() + os.sep + "test.svg"

        self.logger.info(snakemake_line)
        self.process1.setWorkingDirectory(self.working_dir)
        self.process1.setStandardOutputProcess(self.process2)

        self.process1.start("snakemake", snakemake_line[1:])
        self.process2.start("dot", ["-Tsvg", "-o", svg_filename])

        self.process1.waitForFinished(50000)
        self.process2.waitForFinished(50000)

        if os.path.exists(svg_filename):
            self.diag = SVGDialog(svg_filename)
            self.diag.show()
        else:
            msg = "Could not create the DAG file."
            error = str(self.process1.readAllStandardError())
            msg = CriticalMessage(msg, error)
            msg.exec_()
            return

    def open_report(self):
        pref = self.preferences_dialog.ui
        filename = pref.preferences_options_general_htmlpage_value.text()
        if filename == "":
            filename = QW.QFileDialog.getOpenFileNames(
                self, "Select your HTML report", self.working_dir, "HTML files (*.html)"
            )[0]
            if len(filename) and os.path.exists(filename[0]):
                filename = filename[0]
            else:
                self.logger.warning("No valid HTML selected and none specified in the preferences.")
                return
        else:  # we have a filename hardcoded in the preferences
            if self.working_dir is None:
                self.logger.error("Working directory not set yet")
                return

            filename = self.working_dir + os.sep + filename
            if os.path.exists(filename) is False:
                self.logger.error("%s page does not exist. Check the preferences dialog." % filename)
                return
            else:
                self.logger.info("Reading and openning %s" % filename)

        url = "file://" + filename

        # The browser executable itself
        self.browser = Browser(url)
        self.browser.show()

    def create_form_dict(self, layout):
        def _cleaner(value):
            # This is to save the YAML file correctly since the widgets tend to
            # convert None and empty strings as '""' or "''"
            if value in ["None", None, "", '""', "''"]:
                return None
            else:
                # this tries to convert to a list #issue #515
                try:
                    return eval(value)
                except:
                    return value

        widgets = (layout.itemAt(i).widget() for i in range(layout.count()))
        form_dict = {
            w.get_name(): _cleaner(w.get_value()) if w.is_option() else self.create_form_dict(w.get_layout())
            for w in widgets
        }
        return form_dict

    def clear_form(self):
        self.clear_layout(self.form)

    def eventFilter(self, source, event):
        """Inactivate wheel event of combobox"""
        if event.type() == QtCore.QEvent.Wheel and source is self.ui.choice_button:
            return True
        return False

    # ---------------------------------------------------
    #  settings and close
    # ---------------------------------------------------

    def read_settings(self):
        self.logger.info("Reading settings")
        settings = QtCore.QSettings("sequana_gui", "mainapp")
        if settings.value("tab_position") is not None:
            index = settings.value("tab_position")
            self.ui.tabs_pipeline.setCurrentIndex(int(index))

        if settings.value("tab_generic_position") is not None:
            index = settings.value("tab_generic_position")
            self.ui.tabs_generic.setCurrentIndex(int(index))

        if settings.value("tab_sequana_position") is not None:
            index = settings.value("tab_sequana_position")
            self.ui.tabs_sequana.setCurrentIndex(int(index))

        #if settings.value("tab_sequana_input_position") is not None:
        #    index = settings.value("tab_sequana_input_position")
        #    self.ui.tabWidget.setCurrentIndex(int(index))

    def write_settings(self):
        settings = QtCore.QSettings("sequana_gui", "mainapp")

        # tab snakemake output/logger/ipython
        index = self.ui.tabs_pipeline.currentIndex()
        settings.setValue("tab_position", index)

        index = self.ui.tabs_generic.currentIndex()
        settings.setValue("tab_generic_position", index)

        index = self.ui.tabs_sequana.currentIndex()
        settings.setValue("tab_sequana_position", index)

        #index = self.ui.tabWidget.currentIndex()
        #settings.setValue("tab_sequana_input_position", index)

    def _close(self):
        self.write_settings()
        # end any process running that may be running
        self.click_stop()

        self._tempdir.remove()
        try:
            self.browser.close()
        except:
            pass

    def closeEvent(self, event):
        # Close button (red X)
        self._close()

    def close(self):
        # Menu or ctrl+q
        self._close()
        super().close()


class Options(argparse.ArgumentParser):
    def __init__(self, prog="sequana_gui"):
        usage = """Sequanix (part of Sequana project) is a GUI for running Snakefiles

        For Sequana project, you can pre-filled sections as follows:

            sequanix -p quality_control -w analysis -i .

        to prefill the quality_control pipeline to used the local directory to
        search for input files (fastq.gz) and run the analysis in the working
        directory "analysis"

        For Generic snakefiles:

            sequanix -s SNAKEFILE -c CONFIGFILE -w analysis

        will run the snakefile (with its config file) into a working directory.

        """
        description = """"""
        super(Options, self).__init__(
            usage=usage, prog=prog, description=description, formatter_class=easydev.SmartFormatter
        )
        group = self.add_argument_group("GENERAL")
        group.add_argument("-w", "--working-directory", dest="wkdir", help="Set working directory", default=None)
        group.add_argument("-n", "--no-splash", dest="nosplash", action="store_true", help="No splash screen")

        group = self.add_argument_group("SEQUANA")
        group.add_argument("-p", "--pipeline", dest="pipeline", default=None,  help="A valid sequana pipeline name e.g., multitax, lora, variant_calling")

        group_mut = group.add_mutually_exclusive_group()
        group_mut.add_argument(
            "-i",
            "--input-directory",
            dest="input_directory",
            default=None,
            help="input directory where to find the input data",
        )
        group.add_argument(
            "-f",
            "--input-pattern",
            dest="input_pattern",
            default=None,
            help="input pattern to filter input data (e.g. '*fastq.gz'; use quotess !!)",
        )
        group.add_argument(
            "-C",
            "--replace-configfile",
            dest="sequana_configfile",
            default=None,
            help="Replace default sequana config file with local configfile",
        )

        group = self.add_argument_group("GENERIC PIPELINES")
        group.add_argument("-s", "--snakefile", dest="snakefile", default=None, help="A valid Snakefile")
        group.add_argument(
            "-c",
            "--configfile",
            dest="configfile",
            default=None,
            help="optional config file to be used by the Snakefile",
        )
        group.add_argument(
            "-y", "--schema", dest="schemafile", default=None, help="optional schema file to check the config file"
        )


def main(args=None):  # pragma: no cover

    if args is None:
        args = sys.argv[:]
    user_options = Options()
    options = user_options.parse_args(args[1:])
    if options.pipeline and not options.pipeline.startswith("pipeline:"):
        options.pipeline = f"pipeline:{options.pipeline}"

    signal.signal(signal.SIGINT, sigint_handler)

    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QW.QApplication(sys.argv)

    filename = pkg_resources.resource_filename("sequanix", "media/sequana_logo_circle_512.png")

    if options.nosplash:
        app.processEvents()
        sequanix_gui = SequanixGUI(user_options=options)
        sequanix_gui.show()
    else:
        # Show the splash screen for a few seconds
        splash_pix = QtGui.QPixmap(filename)
        splash = QW.QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setMask(splash_pix.mask())
        splash.show()

        for i in range(0, 100):
            t = time.time()
            while time.time() < t + 0.5 / 100.0:
                app.processEvents()

        app.processEvents()
        sequanix_gui = SequanixGUI(user_options=options)
        sequanix_gui.show()
        splash.finish(sequanix_gui)

    # Make sure the main window is the active one
    sequanix_gui.raise_()
    sequanix_gui.activateWindow()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
