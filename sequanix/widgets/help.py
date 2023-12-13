"""Sequana GUI. Can also be used for any snakemake pipeline"""
from PySide6 import QtWidgets as QW

from sequanix.ui import Ui_Help

helptxt = """
<div style="fontsize:12px">
<p>
<b>Sequanix</b> can be used to run Sequana NGS pipelines (see
<a href="http://sequana.readthedocs.io">Sequana.readthedocs.io</a> for details)
but also any Snakefile/configuration pairs
(see <a href="http://snakemake.readthedocs.io">snakemake.readthedocs.io</a>).
</p>
        <p>
        In both cases, a working directory must be set where the Snakefile
        and possibly a configuration file will be copied.
        </p>
        <p>The generic Snakefile must be executable meaning that users should
take care of dependencies. Sequana pipelines should work out of the box
(dependencies or Sequana pipelines being the same as <b>Sequanix</b>).</p>

        <h2>Sequana pipelines</h2>
        There are downloaded automatically with their config file from the
Sequana
        library. Here is a typical set of actions to run Sequana pipelines:

        <ol>
        <li> Select a pipeline</li>
        <li> Select the working directory</li>
        </ol>

        <h2> Generic pipelines </h2>
        Similarly, if you have your own Snakefile (and config file)
        <ol>
        <li>Select a Snakefile </li>
        <li>Select a config file (optional)</li>
        <li> Select the working directory</li>
        </ol>


        Once done, go to the config section and fill the required entries.
        For Sequana pipeline, you will most probably need to fill the input_directory and input_pattern fields.
        Then, you will need to look at the dedicated help for each pipeline.


        <h2> Sequana pipeline dedicated help </help>
             %(pipelines)s
        </div>
"""


class HelpDialog(QW.QDialog):
    """todo"""

    def __init__(self, parent=None, pipelines=""):
        super().__init__(parent=parent)
        self.ui = Ui_Help()
        self.ui.setupUi(self)
        self.ui.textBrowser.setText(helptxt % {"pipelines": pipelines})
        self.ui.buttonBox.accepted.connect(self.close)
