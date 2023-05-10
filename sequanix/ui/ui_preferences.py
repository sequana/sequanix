# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGridLayout,
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        if not Preferences.objectName():
            Preferences.setObjectName(u"Preferences")
        Preferences.resize(546, 407)
        Preferences.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(Preferences)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tabs = QTabWidget(Preferences)
        self.tabs.setObjectName(u"tabs")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.verticalLayout_2 = QVBoxLayout(self.tab_general)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.preferences_options_general_overwrite_value = QCheckBox(self.tab_general)
        self.preferences_options_general_overwrite_value.setObjectName(u"preferences_options_general_overwrite_value")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.preferences_options_general_overwrite_value)

        self.label = QLabel(self.tab_general)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.preferences_options_general_browser_value = QComboBox(self.tab_general)
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.setObjectName(u"preferences_options_general_browser_value")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.preferences_options_general_browser_value)

        self.label_3 = QLabel(self.tab_general)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.preferences_options_general_logging_value = QComboBox(self.tab_general)
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.setObjectName(u"preferences_options_general_logging_value")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.preferences_options_general_logging_value)

        self.label_4 = QLabel(self.tab_general)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.preferences_options_general_htmlpage_value = QLineEdit(self.tab_general)
        self.preferences_options_general_htmlpage_value.setObjectName(u"preferences_options_general_htmlpage_value")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.preferences_options_general_htmlpage_value)

        self.label_2 = QLabel(self.tab_general)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.preferences_options_general_addbrowser_value = QLineEdit(self.tab_general)
        self.preferences_options_general_addbrowser_value.setObjectName(u"preferences_options_general_addbrowser_value")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.preferences_options_general_addbrowser_value)

        self.preferences_options_general_tooltip_value = QCheckBox(self.tab_general)
        self.preferences_options_general_tooltip_value.setObjectName(u"preferences_options_general_tooltip_value")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.preferences_options_general_tooltip_value)

        self.preferences_options_general_schema_value = QCheckBox(self.tab_general)
        self.preferences_options_general_schema_value.setObjectName(u"preferences_options_general_schema_value")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.preferences_options_general_schema_value)

        self.label_6 = QLabel(self.tab_general)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.preferences_options_general_wrapper_value = QLineEdit(self.tab_general)
        self.preferences_options_general_wrapper_value.setObjectName(u"preferences_options_general_wrapper_value")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.preferences_options_general_wrapper_value)

        self.label_7 = QLabel(self.tab_general)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.preferences_options_general_apptainer_value = QLineEdit(self.tab_general)
        self.preferences_options_general_apptainer_value.setObjectName(u"preferences_options_general_apptainer_value")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.preferences_options_general_apptainer_value)

        self.label_9 = QLabel(self.tab_general)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_9)

        self.preferences_options_general_apptainer_args_value = QLineEdit(self.tab_general)
        self.preferences_options_general_apptainer_args_value.setObjectName(u"preferences_options_general_apptainer_args_value")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.preferences_options_general_apptainer_args_value)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.tabs.addTab(self.tab_general, "")
        self.tab_sequana = QWidget()
        self.tab_sequana.setObjectName(u"tab_sequana")
        self.verticalLayout = QVBoxLayout(self.tab_sequana)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.wrapperURLLabel = QLabel(self.tab_sequana)
        self.wrapperURLLabel.setObjectName(u"wrapperURLLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.wrapperURLLabel)

        self.preferences_options_sequana_wrapper_value = QLineEdit(self.tab_sequana)
        self.preferences_options_sequana_wrapper_value.setObjectName(u"preferences_options_sequana_wrapper_value")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.preferences_options_sequana_wrapper_value.sizePolicy().hasHeightForWidth())
        self.preferences_options_sequana_wrapper_value.setSizePolicy(sizePolicy1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.preferences_options_sequana_wrapper_value)

        self.preferences_options_sequana_apptainer_value = QLineEdit(self.tab_sequana)
        self.preferences_options_sequana_apptainer_value.setObjectName(u"preferences_options_sequana_apptainer_value")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.preferences_options_sequana_apptainer_value)

        self.label_5 = QLabel(self.tab_sequana)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_8 = QLabel(self.tab_sequana)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.preferences_options_sequana_apptainer_args_value = QLineEdit(self.tab_sequana)
        self.preferences_options_sequana_apptainer_args_value.setObjectName(u"preferences_options_sequana_apptainer_args_value")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.preferences_options_sequana_apptainer_args_value)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.tabs.addTab(self.tab_sequana, "")

        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Preferences)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.tabs, self.preferences_options_general_browser_value)

        self.retranslateUi(Preferences)
        self.buttonBox.accepted.connect(Preferences.accept)
        self.buttonBox.rejected.connect(Preferences.reject)

        self.tabs.setCurrentIndex(1)
        self.preferences_options_general_logging_value.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Preferences)
    # setupUi

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QCoreApplication.translate("Preferences", u"Preferences", None))
#if QT_CONFIG(tooltip)
        self.preferences_options_general_overwrite_value.setToolTip(QCoreApplication.translate("Preferences", u"<html>\n"
"<body>\n"
"<p>The config file and the snakefile are copied in the working directory when the SAVE button is pressed. If the files exist already, a dialog ask a confirmation. You can force the copy by checking this box.</p>\n"
"</body>\n"
"</html>", None))
#endif // QT_CONFIG(tooltip)
        self.preferences_options_general_overwrite_value.setText(QCoreApplication.translate("Preferences", u"overwrites files", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Preferences", u"<html>\n"
"<body>\n"
"<p>Select your favorite web browser to show an HTML reports.</p>\n"
"</body>\n"
"</html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Preferences", u"Select the browser to be used", None))
        self.preferences_options_general_browser_value.setItemText(0, QCoreApplication.translate("Preferences", u"pyqt/pyside", None))
        self.preferences_options_general_browser_value.setItemText(1, QCoreApplication.translate("Preferences", u"firefox", None))
        self.preferences_options_general_browser_value.setItemText(2, QCoreApplication.translate("Preferences", u"safari", None))
        self.preferences_options_general_browser_value.setItemText(3, QCoreApplication.translate("Preferences", u"chrome", None))

#if QT_CONFIG(tooltip)
        self.preferences_options_general_browser_value.setToolTip(QCoreApplication.translate("Preferences", u"<html>\n"
"<body>\n"
"<p>Select your favorite web browser to show an HTML reports.</p>\n"
"</body>\n"
"</html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Select the <span style=\" font-style:italic;\">logging verbosity</span> parameter to change the level of verbosity.</p><p>We recommend to use the <span style=\" font-weight:600;\">INFO</span> level. </p><p>For lowest verbosity, set to CRITICAL.</p><p>For highest verbosity, set to DEBUG.</p><p><span style=\" font-weight:600;\">Example</span>: Selecting INFO level means: show INFO and following levels (WARNING, ERROR and CRITICAL) but not the level above (here, DEBUG).</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Preferences", u"Logging verbosity", None))
        self.preferences_options_general_logging_value.setItemText(0, QCoreApplication.translate("Preferences", u"DEBUG", None))
        self.preferences_options_general_logging_value.setItemText(1, QCoreApplication.translate("Preferences", u"INFO", None))
        self.preferences_options_general_logging_value.setItemText(2, QCoreApplication.translate("Preferences", u"WARNING", None))
        self.preferences_options_general_logging_value.setItemText(3, QCoreApplication.translate("Preferences", u"ERROR", None))
        self.preferences_options_general_logging_value.setItemText(4, QCoreApplication.translate("Preferences", u"CRITICAL", None))

#if QT_CONFIG(tooltip)
        self.preferences_options_general_logging_value.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Select the <span style=\" font-style:italic;\">logging verbosity</span> parameter to change the level of verbosity.</p><p>We recommend to use the <span style=\" font-weight:600;\">INFO</span> level. </p><p>For lowest verbosity, set to CRITICAL.</p><p>For highest verbosity, set to DEBUG.</p><p><span style=\" font-weight:600;\">Example</span>: Selecting INFO level means: show INFO and following levels (WARNING, ERROR and CRITICAL) but not the level above (here, DEBUG).</p><p><br/><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>If you already know what HTML page you will open, set its filename here to open it automatically. when you click on <span style=\" font-style:italic;\">Open Report</span> button.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Preferences", u"HTML page to open as a report", None))
#if QT_CONFIG(tooltip)
        self.preferences_options_general_htmlpage_value.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>If you already know what HTML page you will open, set its filename here to open it automatically. when you click on <span style=\" font-style:italic;\">Open Report</span> button.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.preferences_options_general_htmlpage_value.setText(QCoreApplication.translate("Preferences", u"summary.html", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>In Sequanix, when a config file is imported or loaded, we dynamically create a form that is editable. In the form, widgets are automatically included in place of  fields ending in _file or _browser. One can add specific field to be transformed into a browser widget by adding such suffix in this preference box. </p><p>Fields must be separated by commas, semi-columns or spaces</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Preferences", u"Form browser keywords", None))
#if QT_CONFIG(tooltip)
        self.preferences_options_general_tooltip_value.setToolTip(QCoreApplication.translate("Preferences", u"Turn on/off tootips", None))
#endif // QT_CONFIG(tooltip)
        self.preferences_options_general_tooltip_value.setText(QCoreApplication.translate("Preferences", u"Show tooltips", None))
#if QT_CONFIG(tooltip)
        self.preferences_options_general_schema_value.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>YAML/JSON Schema files can be provided. If so, they can be used to check the validity of the configuration file. </p><p><br/></p><p>For Sequana projects, if a schema file is available with the pipeline, it is automatically fetched.</p><p><br/></p><p>For Generic projects, you can import one in the File menu.</p><p><br/></p><p>Sometimes, the schema file may be wrong. If so, you can uncheck this box to force the config file to be saved.</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.preferences_options_general_schema_value.setText(QCoreApplication.translate("Preferences", u"Check config with schema", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Set the location of the wrappers. Could be an official github repository or a fork. could also be a local copy. If so, it should be set a as e.g. <span style=\" font-weight:600;\">git+file://path_to_local_copy</span></p><p>Keep empty if not used.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Preferences", u"wrapper URL", None))
#if QT_CONFIG(tooltip)
        self.preferences_options_general_wrapper_value.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Set the location of the wrappers. Could be an official github repository or a fork. could also be a local copy. If so, it should be set a as e.g. <span style=\" font-weight:600;\">git+file://path_to_local_copy</span></p><p>Keep empty if not used.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Set the path to the directory that will store the apptainer images. If empty, apptainers are downloaded in the .snakemake local directory where the pipeline is launched.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Preferences", u"apptainer_prefix", None))
#if QT_CONFIG(tooltip)
        self.preferences_options_general_apptainer_value.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Set the path to the directory that will store the apptainer images. If empty, apptainers are downloaded in the .snakemake local directory where the pipeline is launched.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Preferences", u"apptainer_options", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_general), QCoreApplication.translate("Preferences", u"General", None))
#if QT_CONFIG(tooltip)
        self.wrapperURLLabel.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Set the location of the sequana wrappers. Could be the official github repository or a fork. could also be a local copy. If so, it should be set a as e.g. <span style=\" font-weight:600;\">git+file://path_to_local_copy</span></p><p>The official github repository is :</p><p><span style=\" font-weight:600;\">https://raw.githubusercontent.com/sequana/sequana-wrappers/</span></p><p><span style=\" font-weight:600;\">Note the trailing /</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.wrapperURLLabel.setText(QCoreApplication.translate("Preferences", u"wrapper URL", None))
#if QT_CONFIG(tooltip)
        self.preferences_options_sequana_wrapper_value.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Set the location of the sequana wrappers. Could be the official github repository or a fork. could also be a local copy. If so, it should be set a as e.g. <span style=\" font-weight:600;\">git+file://path_to_local_copy</span></p><p>The official github repository is :</p><p><span style=\" font-weight:600;\">https://raw.githubusercontent.com/sequana/sequana-wrappers/</span></p><p><span style=\" font-weight:600;\">Note the trailing /</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.preferences_options_sequana_wrapper_value.setText(QCoreApplication.translate("Preferences", u"https://raw.githubusercontent.com/sequana/sequana-wrappers/", None))
#if QT_CONFIG(tooltip)
        self.preferences_options_sequana_apptainer_value.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Set the path to the directory that will store the apptainer images. If empty, apptainers are downloaded in the .snakemake local directory where the pipeline is launched.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.preferences_options_sequana_apptainer_value.setText(QCoreApplication.translate("Preferences", u"~/.config/sequana/images", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Preferences", u"<html><head/><body><p>Set the path to the directory that will store the apptainer images. If empty, apptainers are downloaded in the .snakemake local directory where the pipeline is launched.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Preferences", u"apptainer prefix", None))
        self.label_8.setText(QCoreApplication.translate("Preferences", u"apptainer_options", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_sequana), QCoreApplication.translate("Preferences", u"Sequana", None))
    # retranslateUi

