# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 728)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush1 = QBrush(QColor(247, 10, 46, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush)
        brush2 = QBrush(QColor(255, 170, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionImportConfig = QAction(MainWindow)
        self.actionImportConfig.setObjectName("actionImportConfig")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSnakemake = QAction(MainWindow)
        self.actionSnakemake.setObjectName("actionSnakemake")
        self.actionSnakemake.setCheckable(False)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionIPython = QAction(MainWindow)
        self.actionIPython.setObjectName("actionIPython")
        self.actionIPython.setCheckable(True)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.setEnabled(True)
        self.action_import_configfile = QAction(MainWindow)
        self.action_import_configfile.setObjectName("action_import_configfile")
        self.action_import_schemafile = QAction(MainWindow)
        self.action_import_schemafile.setObjectName("action_import_schemafile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.vlayout = QVBoxLayout()
        self.vlayout.setSpacing(0)
        self.vlayout.setObjectName("vlayout")
        self.vlayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.vlayout.setContentsMargins(5, 0, 5, 0)
        self.tabs_pipeline = QTabWidget(self.centralwidget)
        self.tabs_pipeline.setObjectName("tabs_pipeline")
        sizePolicy.setHeightForWidth(self.tabs_pipeline.sizePolicy().hasHeightForWidth())
        self.tabs_pipeline.setSizePolicy(sizePolicy)
        self.tabs_pipeline.setMinimumSize(QSize(0, 160))
        self.tabs_pipeline.setStyleSheet("background-color:#aaddcc")
        self.tabs_pipeline.setTabPosition(QTabWidget.North)
        self.tabs_pipeline.setTabShape(QTabWidget.Rounded)
        self.tabs_pipeline.setMovable(True)
        self.tab_sequana_pipelines = QWidget()
        self.tab_sequana_pipelines.setObjectName("tab_sequana_pipelines")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab_sequana_pipelines.sizePolicy().hasHeightForWidth())
        self.tab_sequana_pipelines.setSizePolicy(sizePolicy1)
        self.gridLayout_6 = QGridLayout(self.tab_sequana_pipelines)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.tabs_sequana = QTabWidget(self.tab_sequana_pipelines)
        self.tabs_sequana.setObjectName("tabs_sequana")
        self.tabs_sequana.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tabs_sequana.sizePolicy().hasHeightForWidth())
        self.tabs_sequana.setSizePolicy(sizePolicy)
        self.tabs_sequana.setBaseSize(QSize(0, 0))
        palette1 = QPalette()
        brush3 = QBrush(QColor(255, 238, 221, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Active, QPalette.NoRole, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.NoRole, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.NoRole, brush)
        self.tabs_sequana.setPalette(palette1)
        self.tabs_sequana.setStyleSheet("background-color:#ffeedd")
        self.tabs_sequana.setTabPosition(QTabWidget.North)
        self.tabs_sequana.setTabShape(QTabWidget.Rounded)
        self.tabs_sequana.setDocumentMode(False)
        self.tabs_sequana.setTabsClosable(False)
        self.tabs_sequana.setMovable(True)
        self.tabs_sequana.setTabBarAutoHide(False)
        self.Pipeline = QWidget()
        self.Pipeline.setObjectName("Pipeline")
        self.gridLayout_19 = QGridLayout(self.Pipeline)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_19.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_19.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.choice_button = QComboBox(self.Pipeline)
        self.choice_button.addItem("")
        self.choice_button.setObjectName("choice_button")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(89, 100, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush4)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Active, QPalette.NoRole, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.NoRole, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.NoRole, brush)
        self.choice_button.setPalette(palette2)
        self.choice_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.choice_button.setAutoFillBackground(False)
        self.choice_button.setStyleSheet("selection-background-color: rgb(89, 100, 255);")

        self.verticalLayout.addWidget(self.choice_button)

        self.gridLayout_19.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabs_sequana.addTab(self.Pipeline, "")
        self.sequana_working_dir_tab = QWidget()
        self.sequana_working_dir_tab.setObjectName("sequana_working_dir_tab")
        self.gridLayout_8 = QGridLayout(self.sequana_working_dir_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.layout_sequana_wkdir = QHBoxLayout()
        self.layout_sequana_wkdir.setObjectName("layout_sequana_wkdir")

        self.gridLayout_8.addLayout(self.layout_sequana_wkdir, 0, 0, 1, 1)

        self.tabs_sequana.addTab(self.sequana_working_dir_tab, "")

        self.gridLayout_20.addWidget(self.tabs_sequana, 0, 0, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_20, 0, 0, 1, 1)

        self.tabs_pipeline.addTab(self.tab_sequana_pipelines, "")
        self.tab_generic_pipelines = QWidget()
        self.tab_generic_pipelines.setObjectName("tab_generic_pipelines")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab_generic_pipelines.sizePolicy().hasHeightForWidth())
        self.tab_generic_pipelines.setSizePolicy(sizePolicy2)
        self.gridLayout_11 = QGridLayout(self.tab_generic_pipelines)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(6, -1, 6, -1)
        self.tabs_generic = QTabWidget(self.tab_generic_pipelines)
        self.tabs_generic.setObjectName("tabs_generic")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabs_generic.sizePolicy().hasHeightForWidth())
        self.tabs_generic.setSizePolicy(sizePolicy3)
        self.tabs_generic.setStyleSheet("background-color:#ffeedd")
        self.snakefile = QWidget()
        self.snakefile.setObjectName("snakefile")
        self.gridLayout_12 = QGridLayout(self.snakefile)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.layout_generic_snakefile = QHBoxLayout()
        self.layout_generic_snakefile.setObjectName("layout_generic_snakefile")

        self.gridLayout_12.addLayout(self.layout_generic_snakefile, 0, 0, 1, 1)

        self.tabs_generic.addTab(self.snakefile, "")
        self.configfile = QWidget()
        self.configfile.setObjectName("configfile")
        self.gridLayout_13 = QGridLayout(self.configfile)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.layout_generic_config = QHBoxLayout()
        self.layout_generic_config.setSpacing(6)
        self.layout_generic_config.setObjectName("layout_generic_config")

        self.gridLayout_13.addLayout(self.layout_generic_config, 0, 0, 1, 1)

        self.cancel_push_button = QPushButton(self.configfile)
        self.cancel_push_button.setObjectName("cancel_push_button")

        self.gridLayout_13.addWidget(self.cancel_push_button, 1, 0, 1, 1)

        self.tabs_generic.addTab(self.configfile, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_14 = QGridLayout(self.tab)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.layout_generic_wkdir = QHBoxLayout()
        self.layout_generic_wkdir.setObjectName("layout_generic_wkdir")

        self.gridLayout_14.addLayout(self.layout_generic_wkdir, 0, 0, 1, 1)

        self.tabs_generic.addTab(self.tab, "")

        self.verticalLayout_3.addWidget(self.tabs_generic)

        self.gridLayout_11.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.tabs_pipeline.addTab(self.tab_generic_pipelines, "")

        self.vlayout.addWidget(self.tabs_pipeline)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.groupBox.setMinimumSize(QSize(0, 90))
        self.gridLayout_15 = QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.action_apptainer = QCheckBox(self.groupBox)
        self.action_apptainer.setObjectName("action_apptainer")
        self.action_apptainer.setMaximumSize(QSize(200, 21))

        self.gridLayout_15.addWidget(self.action_apptainer, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_3)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox_local = QComboBox(self.frame_3)
        self.comboBox_local.addItem("")
        self.comboBox_local.addItem("")
        self.comboBox_local.setObjectName("comboBox_local")

        self.horizontalLayout_5.addWidget(self.comboBox_local)

        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color:orange")
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(1)

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3.setStretch(0, 1)

        self.gridLayout_18.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)

        self.gridLayout_15.addWidget(self.frame_3, 0, 1, 1, 1)

        self.gridLayout_15.setColumnStretch(0, 1)

        self.vlayout.addWidget(self.groupBox)

        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy5)
        self.tabs.setMinimumSize(QSize(0, 0))
        self.tabs.setMaximumSize(QSize(16777215, 2000))
        self.tabs.setBaseSize(QSize(0, 0))
        self.tabs.setStyleSheet("background-color:#ffffff")
        self.snakemake = QWidget()
        self.snakemake.setObjectName("snakemake")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.snakemake.sizePolicy().hasHeightForWidth())
        self.snakemake.setSizePolicy(sizePolicy6)
        self.gridLayout_5 = QGridLayout(self.snakemake)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.layout_snakemake = QVBoxLayout()
        self.layout_snakemake.setObjectName("layout_snakemake")

        self.gridLayout_5.addLayout(self.layout_snakemake, 0, 0, 1, 1)

        self.tabs.addTab(self.snakemake, "")
        self.ipython = QWidget()
        self.ipython.setObjectName("ipython")
        sizePolicy.setHeightForWidth(self.ipython.sizePolicy().hasHeightForWidth())
        self.ipython.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.ipython)
        self.gridLayout.setObjectName("gridLayout")
        self.layout_ipython = QVBoxLayout()
        self.layout_ipython.setSpacing(6)
        self.layout_ipython.setObjectName("layout_ipython")
        self.layout_ipython.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout.addLayout(self.layout_ipython, 0, 0, 1, 1)

        self.tabs.addTab(self.ipython, "")
        self.logger = QWidget()
        self.logger.setObjectName("logger")
        self.gridLayout_3 = QGridLayout(self.logger)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.layout_logger = QVBoxLayout()
        self.layout_logger.setObjectName("layout_logger")

        self.gridLayout_3.addLayout(self.layout_logger, 0, 0, 1, 1)

        self.tabs.addTab(self.logger, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_3.setAcceptDrops(False)
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QScrollArea(self.tab_3)
        self.scrollArea.setObjectName("scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 595, 251))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabs.addTab(self.tab_3, "")

        self.vlayout.addWidget(self.tabs)

        self.widget_footer = QWidget(self.centralwidget)
        self.widget_footer.setObjectName("widget_footer")
        sizePolicy6.setHeightForWidth(self.widget_footer.sizePolicy().hasHeightForWidth())
        self.widget_footer.setSizePolicy(sizePolicy6)
        self.widget_footer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget_footer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.run_btn = QPushButton(self.widget_footer)
        self.run_btn.setObjectName("run_btn")

        self.horizontalLayout.addWidget(self.run_btn)

        self.stop_btn = QPushButton(self.widget_footer)
        self.stop_btn.setObjectName("stop_btn")

        self.horizontalLayout.addWidget(self.stop_btn)

        self.unlock_btn = QPushButton(self.widget_footer)
        self.unlock_btn.setObjectName("unlock_btn")

        self.horizontalLayout.addWidget(self.unlock_btn)

        self.report_btn = QPushButton(self.widget_footer)
        self.report_btn.setObjectName("report_btn")

        self.horizontalLayout.addWidget(self.report_btn)

        self.save_btn = QPushButton(self.widget_footer)
        self.save_btn.setObjectName("save_btn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy7)
        self.save_btn.setAutoFillBackground(False)
        self.save_btn.setStyleSheet("background-color:orange")

        self.horizontalLayout.addWidget(self.save_btn)

        self.dag_btn = QPushButton(self.widget_footer)
        self.dag_btn.setObjectName("dag_btn")

        self.horizontalLayout.addWidget(self.dag_btn)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.vlayout.addWidget(self.widget_footer)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy8)
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setStyleSheet(
            "border: 2px solid grey;\n" "margin:2px;\n" "border-radius: 5px;\n" "text-align: center;\n" ""
        )
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(1)

        self.vlayout.addWidget(self.progressBar)

        self.gridLayout_2.addLayout(self.vlayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 647, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabs_pipeline, self.choice_button)
        QWidget.setTabOrder(self.choice_button, self.tabs)
        QWidget.setTabOrder(self.tabs, self.run_btn)
        QWidget.setTabOrder(self.run_btn, self.stop_btn)
        QWidget.setTabOrder(self.stop_btn, self.unlock_btn)
        QWidget.setTabOrder(self.unlock_btn, self.report_btn)
        QWidget.setTabOrder(self.report_btn, self.save_btn)
        QWidget.setTabOrder(self.save_btn, self.dag_btn)
        QWidget.setTabOrder(self.dag_btn, self.scrollArea)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_import_configfile)
        self.menuFile.addAction(self.action_import_schemafile)
        self.menuFile.addAction(self.actionQuit)
        self.menuOption.addAction(self.actionSnakemake)
        self.menuOption.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabs_pipeline.setCurrentIndex(0)
        self.tabs_sequana.setCurrentIndex(1)
        self.tabs_generic.setCurrentIndex(0)
        self.tabs.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Sequanix (Sequana GUI)", None))
        self.actionImportConfig.setText(QCoreApplication.translate("MainWindow", "&Import Config File", None))
        # if QT_CONFIG(shortcut)
        self.actionImportConfig.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+I", None))
        # endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", "&Quit", None))
        # if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+Q", None))
        # endif // QT_CONFIG(shortcut)
        self.actionSnakemake.setText(QCoreApplication.translate("MainWindow", "Snakemake &Options", None))
        # if QT_CONFIG(shortcut)
        self.actionSnakemake.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+O", None))
        # endif // QT_CONFIG(shortcut)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", "&Preferences", None))
        # if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+P", None))
        # endif // QT_CONFIG(shortcut)
        self.actionIPython.setText(QCoreApplication.translate("MainWindow", "Show/Hide IPython &Debug dialog", None))
        # if QT_CONFIG(tooltip)
        self.actionIPython.setToolTip(
            QCoreApplication.translate("MainWindow", "Show or Hide an IPython dialog for debugging", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionIPython.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+D", None))
        # endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "&About", None))
        # if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+A", None))
        # endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", "Quick Start", None))
        # if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+H", None))
        # endif // QT_CONFIG(shortcut)
        self.action_import_configfile.setText(
            QCoreApplication.translate("MainWindow", "Import Config File (sequana pipeline only)", None)
        )
        self.action_import_schemafile.setText(
            QCoreApplication.translate("MainWindow", "Import YAML/JSON Schema File (generic pipeline only)", None)
        )
        # if QT_CONFIG(tooltip)
        self.tabs_pipeline.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>Select a Sequana pipeline (left tab) or a generic Snakemake file (right tab).</p><p><br/>Go to Menu Help-&gt;QuickStart for more details (Ctrl+H key).</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.tabs_sequana.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>1. Select one of the pipeline in the 'pipeline selection'. Its config file will appear in the bottom section. </p><p>2. Select the working directory, which is the directory where the pipeline and its config file will be copy and where the analysis will be run</p><p><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.choice_button.setItemText(0, QCoreApplication.translate("MainWindow", "Select a Sequana pipeline", None))

        # if QT_CONFIG(tooltip)
        self.choice_button.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>Sequana pipelines are automatically fetched from sequana library.</p><p>Each pipeline is defined by a pipeline name. Its config file is fetched automatically.</p><p>Each pipeline require the user to define the input. It may be one of:</p><p><ul><li> a directory</li><li> a set of FastQ input file</li></ul></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.choice_button.setCurrentText(QCoreApplication.translate("MainWindow", "Select a Sequana pipeline", None))
        self.tabs_sequana.setTabText(
            self.tabs_sequana.indexOf(self.Pipeline),
            QCoreApplication.translate("MainWindow", "1 - Pipeline selection", None),
        )
        self.tabs_sequana.setTabText(
            self.tabs_sequana.indexOf(self.sequana_working_dir_tab),
            QCoreApplication.translate("MainWindow", "2 - Working directory", None),
        )
        self.tabs_pipeline.setTabText(
            self.tabs_pipeline.indexOf(self.tab_sequana_pipelines),
            QCoreApplication.translate("MainWindow", "A - Sequana pipelines", None),
        )
        # if QT_CONFIG(tooltip)
        self.tabs_generic.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;"><li style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Left tab:</span> Select a valid local Snakefile. </li><li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Middle tab:</span> Select a config file. This is optional. Note that Snakefiles may be using a config file or not. For instance if <i>configfile: "config.yaml"</i> is found, a config file is expected. Users have to check with the author of the snakefile whether a config file is required or not.</li><li style=" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Right tab: </span>Select working directory where Snakefile and config fi'
                "les will be copied. Pipelines are also ran in that directory. </li></ul></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.tabs_generic.setTabText(
            self.tabs_generic.indexOf(self.snakefile), QCoreApplication.translate("MainWindow", "1 - Snakefile", None)
        )
        self.cancel_push_button.setText(QCoreApplication.translate("MainWindow", "cancel selection", None))
        self.tabs_generic.setTabText(
            self.tabs_generic.indexOf(self.configfile),
            QCoreApplication.translate("MainWindow", "2 - Config file", None),
        )
        self.tabs_generic.setTabText(
            self.tabs_generic.indexOf(self.tab), QCoreApplication.translate("MainWindow", "3 - Working directory", None)
        )
        self.tabs_pipeline.setTabText(
            self.tabs_pipeline.indexOf(self.tab_generic_pipelines),
            QCoreApplication.translate("MainWindow", "B - Generic pipelines", None),
        )
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", "Pipeline control", None))
        # if QT_CONFIG(tooltip)
        self.action_apptainer.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>If your pipeline sets apptainers (a.k.a singularity) and you want to use them, tick this box. Strongly advice for Sequana pipelines so that there is no need to install third-party standalones.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.action_apptainer.setText(QCoreApplication.translate("MainWindow", "Use singularity/apptainer", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "<b>Is it a local or cluster run ?</b>", None))
        self.comboBox_local.setItemText(0, QCoreApplication.translate("MainWindow", "local", None))
        self.comboBox_local.setItemText(1, QCoreApplication.translate("MainWindow", "cluster", None))

        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Check the snakemake dialog (<span style=" font-weight:600;">Ctrl+O</span>) to set the number of nodes/jobs, and cluster options.</p></body></html>',
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.tabs.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.snakemake.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.tabs.setTabText(
            self.tabs.indexOf(self.snakemake), QCoreApplication.translate("MainWindow", "&Snakemake output", None)
        )
        # if QT_CONFIG(tooltip)
        self.ipython.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>This is an IPython shell included in the GUI. The entire Sequana GUI is accessible as the variable <span style=" font-weight:600;">gui.</span></p><p>For instance, you can access to layout or values set in the graphical interface with:</p>\n'
                "<pre>    \n"
                "    gui.ui\n"
                "</pre>\n"
                "\n"
                "<p>More generally, this is a pure IPython shell, so you can use e.g. matplotlib/pylab:</p>\n"
                "<pre>    \n"
                "    import pylab\n"
                "    pylab.plot([1,2,3])\n"
                "</pre></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.tabs.setTabText(
            self.tabs.indexOf(self.ipython), QCoreApplication.translate("MainWindow", "&IPython shell", None)
        )
        # if QT_CONFIG(tooltip)
        self.logger.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<p>This tab contains the logging information from Sequana and possibly other Python packages that uses the logging package.</p>\n"
                "\n"
                "Color code:\n"
                "\n"
                "<pre>\n"
                "- debug: cyan\n"
                "- info: green\n"
                "- warning: orange\n"
                "- error: red\n"
                "- critical: bold red \n"
                "</pre>You can change the verbosity in the preferences dialog</p>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.tabs.setTabText(self.tabs.indexOf(self.logger), QCoreApplication.translate("MainWindow", "&Logger", None))
        # if QT_CONFIG(tooltip)
        self.tab_3.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.tabs.setTabText(
            self.tabs.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", "&Config parameters", None)
        )
        # if QT_CONFIG(tooltip)
        self.run_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Execute the Snakemake pipeline </p><p><span style=" font-weight:600;">shortcut: Ctrl+R</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.run_btn.setText(QCoreApplication.translate("MainWindow", "&Run", None))
        # if QT_CONFIG(shortcut)
        self.run_btn.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+R", None))
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(tooltip)
        self.stop_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Stop the running pipeline. This may take a few seconds to stop.</p><p><span style=" font-weight:600;">Shortcut: Ctrl+X</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", "Stop", None))
        # if QT_CONFIG(shortcut)
        self.stop_btn.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+X", None))
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(tooltip)
        self.unlock_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Sometimes, the execution of a pipeline may be interrupted, which locks the working directory. This button allows users to unlock the directory.</p><p>For developers, this is equivalent to the snakemake command:</p><p><span style=" font-style:italic; color:#ff0004;">snakemake -s Snakefile --unlock </span></p><p><br/></p><p><span style=" font-weight:600; color:#000000;">Shortcut: Ctrl+U</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.unlock_btn.setText(QCoreApplication.translate("MainWindow", "&Unlock", None))
        # if QT_CONFIG(shortcut)
        self.unlock_btn.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+U", None))
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(tooltip)
        self.report_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>This button opens an HTML page present in the working directory (if found) if an HTML filename is specified in the <span style=" font-weight:600;">Preferences dialog.</span> If not, a file browser pops up so that one can select an HTML file. </p><p><br/></p><p><br/></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.report_btn.setText(QCoreApplication.translate("MainWindow", "Open Report", None))
        # if QT_CONFIG(shortcut)
        self.report_btn.setShortcut(QCoreApplication.translate("MainWindow", "Shift+W", None))
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(tooltip)
        self.save_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Save the current <span style=" font-style:italic;">configuration</span> (parameters to be used by the pipeline in the Config parameters tab here above) as well as the current <span style=" font-style:italic;">Snakemake pipeline</span>. The two files are saved in the <span style=" font-style:italic;">working directory</span>.</p><p><br/></p><p><span style=" font-weight:600;">Shortcut: Ctrl+S</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.save_btn.setText(QCoreApplication.translate("MainWindow", "&Save", None))
        # if QT_CONFIG(shortcut)
        self.save_btn.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+S", None))
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(tooltip)
        self.dag_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Pressing this button, a DAG is created and shown. </p><p>This is a good way to check your config file (i.e., if there are optional switch).</p><p><br/></p><p><span style=" font-weight:600;">Shortcut: Ctrl+D</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.dag_btn.setText(QCoreApplication.translate("MainWindow", "Show Pipeline", None))
        # if QT_CONFIG(shortcut)
        self.dag_btn.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+D", None))
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(tooltip)
        self.progressBar.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<p>Progress of the pipeline. color codes:\n"
                "    <ul>\n"
                '        <li style="color:red">Red: an error occured</li>\n'
                '        <li style="color:orange">Orange: interrupted by the user</li>\n'
                '        <li style="color:green">Green: completed with success</li>\n'
                '        <li style="color:blue">Blue: in progress</li>\n'
                "    </ul>\n"
                "</p>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "&File", None))
        self.menuOption.setTitle(QCoreApplication.translate("MainWindow", "&Option", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "&Help", None))

    # retranslateUi
