# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(507, 366)
        Preferences.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Preferences)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabs = QtWidgets.QTabWidget(Preferences)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName("tabs")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_general)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.preferences_options_general_overwrite_value = QtWidgets.QCheckBox(self.tab_general)
        self.preferences_options_general_overwrite_value.setObjectName("preferences_options_general_overwrite_value")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.preferences_options_general_overwrite_value)
        self.label = QtWidgets.QLabel(self.tab_general)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.preferences_options_general_browser_value = QtWidgets.QComboBox(self.tab_general)
        self.preferences_options_general_browser_value.setObjectName("preferences_options_general_browser_value")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_browser_value)
        self.label_3 = QtWidgets.QLabel(self.tab_general)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.preferences_options_general_logging_value = QtWidgets.QComboBox(self.tab_general)
        self.preferences_options_general_logging_value.setObjectName("preferences_options_general_logging_value")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_logging_value)
        self.label_4 = QtWidgets.QLabel(self.tab_general)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.preferences_options_general_htmlpage_value = QtWidgets.QLineEdit(self.tab_general)
        self.preferences_options_general_htmlpage_value.setObjectName("preferences_options_general_htmlpage_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_htmlpage_value)
        self.preferences_options_general_addbrowser_value = QtWidgets.QLineEdit(self.tab_general)
        self.preferences_options_general_addbrowser_value.setObjectName("preferences_options_general_addbrowser_value")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_addbrowser_value)
        self.label_2 = QtWidgets.QLabel(self.tab_general)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.preferences_options_general_tooltip_value = QtWidgets.QCheckBox(self.tab_general)
        self.preferences_options_general_tooltip_value.setObjectName("preferences_options_general_tooltip_value")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.preferences_options_general_tooltip_value)
        self.preferences_options_general_schema_value = QtWidgets.QCheckBox(self.tab_general)
        self.preferences_options_general_schema_value.setObjectName("preferences_options_general_schema_value")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.preferences_options_general_schema_value)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.tabs.addTab(self.tab_general, "")
        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Preferences)
        self.tabs.setCurrentIndex(0)
        self.preferences_options_general_logging_value.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Preferences.accept)
        self.buttonBox.rejected.connect(Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.tabs, self.preferences_options_general_browser_value)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.preferences_options_general_overwrite_value.setToolTip(
            _translate(
                "Preferences",
                "<html>\n"
                "<body>\n"
                "<p>The config file and the snakefile are copied in the working directory when the SAVE button is pressed. If the files exist already, a dialog ask a confirmation. You can force the copy by checking this box.</p>\n"
                "</body>\n"
                "</html>",
            )
        )
        self.preferences_options_general_overwrite_value.setText(_translate("Preferences", "overwrites files"))
        self.label.setToolTip(
            _translate(
                "Preferences",
                "<html>\n"
                "<body>\n"
                "<p>Select your favorite web browser to show an HTML reports.</p>\n"
                "</body>\n"
                "</html>",
            )
        )
        self.label.setText(_translate("Preferences", "Select the browser to be used"))
        self.preferences_options_general_browser_value.setToolTip(
            _translate(
                "Preferences",
                "<html>\n"
                "<body>\n"
                "<p>Select your favorite web browser to show an HTML reports.</p>\n"
                "</body>\n"
                "</html>",
            )
        )
        self.preferences_options_general_browser_value.setItemText(0, _translate("Preferences", "pyqt5"))
        self.preferences_options_general_browser_value.setItemText(1, _translate("Preferences", "firefox"))
        self.preferences_options_general_browser_value.setItemText(2, _translate("Preferences", "safari"))
        self.preferences_options_general_browser_value.setItemText(3, _translate("Preferences", "chrome"))
        self.label_3.setToolTip(
            _translate(
                "Preferences",
                '<html><head/><body><p>Select the <span style=" font-style:italic;">logging verbosity</span> parameter to change the level of verbosity.</p><p>We recommend to use the <span style=" font-weight:600;">INFO</span> level. </p><p>For lowest verbosity, set to CRITICAL.</p><p>For highest verbosity, set to DEBUG.</p><p><span style=" font-weight:600;">Example</span>: Selecting INFO level means: show INFO and following levels (WARNING, ERROR and CRITICAL) but not the level above (here, DEBUG).</p><p><br/></p></body></html>',
            )
        )
        self.label_3.setText(_translate("Preferences", "Logging verbosity"))
        self.preferences_options_general_logging_value.setToolTip(
            _translate(
                "Preferences",
                '<html><head/><body><p>Select the <span style=" font-style:italic;">logging verbosity</span> parameter to change the level of verbosity.</p><p>We recommend to use the <span style=" font-weight:600;">INFO</span> level. </p><p>For lowest verbosity, set to CRITICAL.</p><p>For highest verbosity, set to DEBUG.</p><p><span style=" font-weight:600;">Example</span>: Selecting INFO level means: show INFO and following levels (WARNING, ERROR and CRITICAL) but not the level above (here, DEBUG).</p><p><br/><br/></p></body></html>',
            )
        )
        self.preferences_options_general_logging_value.setItemText(0, _translate("Preferences", "DEBUG"))
        self.preferences_options_general_logging_value.setItemText(1, _translate("Preferences", "INFO"))
        self.preferences_options_general_logging_value.setItemText(2, _translate("Preferences", "WARNING"))
        self.preferences_options_general_logging_value.setItemText(3, _translate("Preferences", "ERROR"))
        self.preferences_options_general_logging_value.setItemText(4, _translate("Preferences", "CRITICAL"))
        self.label_4.setToolTip(
            _translate(
                "Preferences",
                '<html><head/><body><p>If you already know what HTML page you will open, set its filename here to open it automatically. when you click on <span style=" font-style:italic;">Open Report</span> button.</p></body></html>',
            )
        )
        self.label_4.setText(_translate("Preferences", "HTML page to open as a report"))
        self.preferences_options_general_htmlpage_value.setToolTip(
            _translate(
                "Preferences",
                '<html><head/><body><p>If you already know what HTML page you will open, set its filename here to open it automatically. when you click on <span style=" font-style:italic;">Open Report</span> button.</p></body></html>',
            )
        )
        self.preferences_options_general_htmlpage_value.setText(_translate("Preferences", "multi_summary.html"))
        self.label_2.setToolTip(
            _translate(
                "Preferences",
                "<html><head/><body><p>In Sequanix, when a config file is imported or loaded, we dynamically create a form that is editable. In the form, widgets are automatically included in place of  fields ending in _file or _browser. One can add specific field to be transformed into a browser widget by adding such suffix in this preference box. </p><p>Fields must be separated by commas, semi-columns or spaces</p></body></html>",
            )
        )
        self.label_2.setText(_translate("Preferences", "Form browser keywords"))
        self.preferences_options_general_tooltip_value.setToolTip(_translate("Preferences", "Turn on/off tootips"))
        self.preferences_options_general_tooltip_value.setText(_translate("Preferences", "Show tooltips"))
        self.preferences_options_general_schema_value.setToolTip(
            _translate(
                "Preferences",
                "<html><head/><body><p>YAML/JSON Schema files can be provided. If so, they can be used to check the validity of the configuration file. </p><p><br/></p><p>For Sequana projects, if a schema file is available with the pipeline, it is automatically fetched.</p><p><br/></p><p>For Generic projects, you can import one in the File menu.</p><p><br/></p><p>Sometimes, the schema file may be wrong. If so, you can uncheck this box to force the config file to be saved.</p><p><br/></p></body></html>",
            )
        )
        self.preferences_options_general_schema_value.setText(_translate("Preferences", "Check config with schema"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_general), _translate("Preferences", "General"))
