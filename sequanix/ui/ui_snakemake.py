# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'snakemake.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_Snakemake(object):
    def setupUi(self, Snakemake):
        if not Snakemake.objectName():
            Snakemake.setObjectName(u"Snakemake")
        Snakemake.resize(426, 484)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Snakemake.sizePolicy().hasHeightForWidth())
        Snakemake.setSizePolicy(sizePolicy)
        Snakemake.setAcceptDrops(False)
        Snakemake.setAutoFillBackground(False)
        Snakemake.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(Snakemake)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabs = QTabWidget(Snakemake)
        self.tabs.setObjectName(u"tabs")
        self.tab_local = QWidget()
        self.tab_local.setObjectName(u"tab_local")
        self.verticalLayoutWidget_2 = QWidget(self.tab_local)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(19, 19, 151, 81))
        self.vertical_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.vertical_layout.setContentsMargins(5, 5, 5, 5)
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.horizontal_layout.setContentsMargins(5, 5, 5, 5)
        self.snakemake_options_local_cores_label = QLabel(self.verticalLayoutWidget_2)
        self.snakemake_options_local_cores_label.setObjectName(u"snakemake_options_local_cores_label")

        self.horizontal_layout.addWidget(self.snakemake_options_local_cores_label)

        self.snakemake_options_local_cores_value = QSpinBox(self.verticalLayoutWidget_2)
        self.snakemake_options_local_cores_value.setObjectName(u"snakemake_options_local_cores_value")
        self.snakemake_options_local_cores_value.setMinimum(1)
        self.snakemake_options_local_cores_value.setMaximum(100000)

        self.horizontal_layout.addWidget(self.snakemake_options_local_cores_value)


        self.vertical_layout.addLayout(self.horizontal_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout.addItem(self.verticalSpacer)

        self.tabs.addTab(self.tab_local, "")
        self.tab_cluster = QWidget()
        self.tab_cluster.setObjectName(u"tab_cluster")
        self.gridLayout_3 = QGridLayout(self.tab_cluster)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.snakemake_options_cluster_jobs_label = QLabel(self.tab_cluster)
        self.snakemake_options_cluster_jobs_label.setObjectName(u"snakemake_options_cluster_jobs_label")

        self.horizontalLayout_2.addWidget(self.snakemake_options_cluster_jobs_label)

        self.snakemake_options_cluster_jobs_value = QSpinBox(self.tab_cluster)
        self.snakemake_options_cluster_jobs_value.setObjectName(u"snakemake_options_cluster_jobs_value")
        self.snakemake_options_cluster_jobs_value.setMinimum(1)
        self.snakemake_options_cluster_jobs_value.setMaximum(10000)
        self.snakemake_options_cluster_jobs_value.setValue(4)

        self.horizontalLayout_2.addWidget(self.snakemake_options_cluster_jobs_value)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.snakemake_options_cluster_cluster_label = QLabel(self.tab_cluster)
        self.snakemake_options_cluster_cluster_label.setObjectName(u"snakemake_options_cluster_cluster_label")

        self.horizontalLayout.addWidget(self.snakemake_options_cluster_cluster_label)

        self.snakemake_options_cluster_cluster_value = QLineEdit(self.tab_cluster)
        self.snakemake_options_cluster_cluster_value.setObjectName(u"snakemake_options_cluster_cluster_value")

        self.horizontalLayout.addWidget(self.snakemake_options_cluster_cluster_value)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.snakemake_options_cluster_config_label = QLabel(self.tab_cluster)
        self.snakemake_options_cluster_config_label.setObjectName(u"snakemake_options_cluster_config_label")

        self.horizontalLayout_4.addWidget(self.snakemake_options_cluster_config_label)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabs.addTab(self.tab_cluster, "")
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.formLayoutWidget_3 = QWidget(self.tab_general)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(20, 10, 331, 268))
        self.layout_general = QFormLayout(self.formLayoutWidget_3)
        self.layout_general.setObjectName(u"layout_general")
        self.layout_general.setContentsMargins(0, 0, 0, 0)
        self.snakemake_options_general_quiet_value = QCheckBox(self.formLayoutWidget_3)
        self.snakemake_options_general_quiet_value.setObjectName(u"snakemake_options_general_quiet_value")

        self.layout_general.setWidget(1, QFormLayout.LabelRole, self.snakemake_options_general_quiet_value)

        self.snakemake_options_general_forceall_value = QCheckBox(self.formLayoutWidget_3)
        self.snakemake_options_general_forceall_value.setObjectName(u"snakemake_options_general_forceall_value")

        self.layout_general.setWidget(2, QFormLayout.LabelRole, self.snakemake_options_general_forceall_value)

        self.snakemake_options_general_keep__going_value = QCheckBox(self.formLayoutWidget_3)
        self.snakemake_options_general_keep__going_value.setObjectName(u"snakemake_options_general_keep__going_value")

        self.layout_general.setWidget(3, QFormLayout.LabelRole, self.snakemake_options_general_keep__going_value)

        self.snakemake_options_general_no__hooks_value = QCheckBox(self.formLayoutWidget_3)
        self.snakemake_options_general_no__hooks_value.setObjectName(u"snakemake_options_general_no__hooks_value")

        self.layout_general.setWidget(4, QFormLayout.LabelRole, self.snakemake_options_general_no__hooks_value)

        self.label_restart__times = QLabel(self.formLayoutWidget_3)
        self.label_restart__times.setObjectName(u"label_restart__times")

        self.layout_general.setWidget(5, QFormLayout.LabelRole, self.label_restart__times)

        self.snakemake_options_general_restart__times_value = QSpinBox(self.formLayoutWidget_3)
        self.snakemake_options_general_restart__times_value.setObjectName(u"snakemake_options_general_restart__times_value")

        self.layout_general.setWidget(5, QFormLayout.FieldRole, self.snakemake_options_general_restart__times_value)

        self.snakemake_options_general_verbose_value = QCheckBox(self.formLayoutWidget_3)
        self.snakemake_options_general_verbose_value.setObjectName(u"snakemake_options_general_verbose_value")

        self.layout_general.setWidget(6, QFormLayout.LabelRole, self.snakemake_options_general_verbose_value)

        self.snakemake_options_general_summary_value = QCheckBox(self.formLayoutWidget_3)
        self.snakemake_options_general_summary_value.setObjectName(u"snakemake_options_general_summary_value")

        self.layout_general.setWidget(7, QFormLayout.LabelRole, self.snakemake_options_general_summary_value)

        self.label = QLabel(self.formLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.layout_general.setWidget(8, QFormLayout.LabelRole, self.label)

        self.snakemake_options_general_custom = QLineEdit(self.formLayoutWidget_3)
        self.snakemake_options_general_custom.setObjectName(u"snakemake_options_general_custom")

        self.layout_general.setWidget(8, QFormLayout.FieldRole, self.snakemake_options_general_custom)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_general.setItem(9, QFormLayout.FieldRole, self.spacer)

        self.tabs.addTab(self.tab_general, "")

        self.verticalLayout.addWidget(self.tabs)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Snakemake)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.tabs, self.snakemake_options_local_cores_value)
        QWidget.setTabOrder(self.snakemake_options_local_cores_value, self.snakemake_options_cluster_cluster_value)
        QWidget.setTabOrder(self.snakemake_options_cluster_cluster_value, self.snakemake_options_cluster_jobs_value)

        self.retranslateUi(Snakemake)
        self.buttonBox.accepted.connect(Snakemake.accept)
        self.buttonBox.rejected.connect(Snakemake.reject)

        self.tabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Snakemake)
    # setupUi

    def retranslateUi(self, Snakemake):
        Snakemake.setWindowTitle(QCoreApplication.translate("Snakemake", u"Snakemake options", None))
#if QT_CONFIG(tooltip)
        self.tabs.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Snakemake parameters (those used by the snakemake command)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.snakemake_options_local_cores_label.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Number of CPUs to use locally.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_local_cores_label.setText(QCoreApplication.translate("Snakemake", u"cores", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_local_cores_value.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Number of CPUs to use locally.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabs.setTabText(self.tabs.indexOf(self.tab_local), QCoreApplication.translate("Snakemake", u"&Local", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_cluster_jobs_label.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Use at most N cores in parallel (default: 4). If N is omitted, the limit is set to the number of available cores.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_cluster_jobs_label.setText(QCoreApplication.translate("Snakemake", u"jobs", None))
        self.snakemake_options_cluster_jobs_value.setSuffix("")
#if QT_CONFIG(tooltip)
        self.snakemake_options_cluster_cluster_label.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Execute snakemake rules with a dedicated submit command, e.g. qsub on SGE system.</p><p>Snakemake compiles jobs into scripts that are submitted to the cluster with the given command, once all input files for a particular job are present. </p><p>The submit command can be decorated to make it aware of certain job properties (input, output, params, wildcards, log, threads and dependencies)</p><p>Depending on your cluster, you must set the appropriate command. For instance on SGE:</p><p><span style=\" font-weight:600;\">snakemake --cluster 'qsub -pe threaded 4'</span></p><p>or on SLURM to use 16G of memory:</p><p><span style=\" font-weight:600;\">    snakemake --cluster &quot;sbatch --mem 16000&quot; </span></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_cluster_cluster_label.setText(QCoreApplication.translate("Snakemake", u"cluster", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_cluster_cluster_value.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Execute snakemake rules with a dedicated submit command, e.g. qsub on SGE system.</p><p>Snakemake compiles jobs into scripts that are submitted to the cluster with the given command, once all input files for a particular job are present. </p><p>The submit command can be decorated to make it aware of certain job properties (input, output, params, wildcards, log, threads and dependencies)</p><p>Depending on your cluster, you must set the appropriate command. For instance on SGE:</p><p><span style=\" font-weight:600;\">snakemake --cluster 'qsub -pe threaded 4'</span></p><p>or on SLURM to use 16G of memory:</p><p><span style=\" font-weight:600;\">    snakemake --cluster &quot;sbatch --mem 16000&quot; </span></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.snakemake_options_cluster_config_label.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Name of the cluster config file to be found in the working directory.</p><p><br/></p><p>Sequana pipeline selection will automatically fill the name (cluster_config.json)</p><p><br/></p><p>If set, snakemake is ran with the parameter --cluster-config </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_cluster_config_label.setText(QCoreApplication.translate("Snakemake", u"cluster-config", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_cluster), QCoreApplication.translate("Snakemake", u"&Cluster", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_general_quiet_value.setToolTip(QCoreApplication.translate("Snakemake", u"Do not output any progress or rule information", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_general_quiet_value.setText(QCoreApplication.translate("Snakemake", u"Quiet", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_general_forceall_value.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Force the execution of the selected (or the first) rule and all rules it is dependent on regardless of already created output.</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_general_forceall_value.setText(QCoreApplication.translate("Snakemake", u"forceall", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_general_keep__going_value.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Go on with independent jobs if a job fails.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_general_keep__going_value.setText(QCoreApplication.translate("Snakemake", u"keep-going", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_general_no__hooks_value.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Do not invoke onstart, onsuccess or onerror hooks after execution.</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_general_no__hooks_value.setText(QCoreApplication.translate("Snakemake", u"nohooks", None))
#if QT_CONFIG(tooltip)
        self.label_restart__times.setToolTip(QCoreApplication.translate("Snakemake", u"Number of times to restart failing jobs (defaults to 0).", None))
#endif // QT_CONFIG(tooltip)
        self.label_restart__times.setText(QCoreApplication.translate("Snakemake", u"restart-times", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_general_verbose_value.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p> Print debugging output.</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_general_verbose_value.setText(QCoreApplication.translate("Snakemake", u"verbose", None))
#if QT_CONFIG(tooltip)
        self.snakemake_options_general_summary_value.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Print a summary of all files created by the workflow.</p><p>The has the following columns: filename, modification time, rule version, status, plan. Thereby rule version contains the versionthe file was created with (see the version keyword of rules), and status denotes whether the file is missing, its input files are newer or if version or implementation of the rule changed since file creation. Finally the last column denotes whether the file will be updated or created during the next workflow execution.</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.snakemake_options_general_summary_value.setText(QCoreApplication.translate("Snakemake", u"summary", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Snakemake", u"<html><head/><body><p>Add any other valid snakemake options here</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Snakemake", u"any other options", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_general), QCoreApplication.translate("Snakemake", u"&General", None))
    # retranslateUi

