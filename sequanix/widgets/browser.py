from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWebEngineWidgets import *
# QWebEngineSettings
#from PyQt6.WebEngine import QWebEngineView

# potential resources for improvements:
# https://github.com/ralsina/devicenzo/blob/master/devicenzo.py

from PySide6.QtWidgets import QMainWindow

from PySide6.QtWebEngineCore import QWebEnginePage

class Browser(QMainWindow):
    """

    On purpose, there is no caching so that (if re-generated), the
    new content of an HTML is shown.

    """

    def __init__(self, url):
        QMainWindow.__init__(self)

        # Progress bar
        # ------------------------------------------------------------
        self.progress = 0
        # Main page QWebView
        # -------------------------------------------------------------
        self.wb = SequanixQWebView(parent=self, titleChanged=self.setWindowTitle)
        self.wb.urlChanged.connect(lambda u: self.url.setText(u.toString()))

        self.wb.titleChanged.connect(self.adjustTitle)
        self.wb.loadProgress.connect(self.setProgress)

        self.setCentralWidget(self.wb)

        # Main menu tool bar
        # -------------------------------------------------------------
        self.tb = self.addToolBar("Main Toolbar")
        for a in (
            QWebEnginePage.Back,
            QWebEnginePage.Forward,
            QWebEnginePage.Reload,
            QWebEnginePage.DownloadLinkToDisk,
        ):
            self.tb.addAction(self.wb.pageAction(a))

        self.url = QLineEdit(returnPressed=lambda: self.wb.setUrl(QtCore.QUrl.fromUserInput(self.url.text())))
        self.tb.addWidget(self.url)

        # status bar ---------------------------------------------------
        self.sb = self.statusBar()
        try:
            # pyqt5.6
            self.wb.statusBarMessage.connect(self.sb.showMessage)
        except:
            pass
        self.wb.page().linkHovered.connect(lambda l: self.sb.showMessage(l, 3000))

        # Search bar
        # ------------------------------------------------------------
        self.search = QLineEdit(returnPressed=lambda: self.wb.findText(self.search.text()))
        self.search.show()
        self.search.hide()  # To make ctrl+F effective, need to show/hide ?

        # The shortcuts
        # ---------------------------------------------------------
        self.showSearch = Qt.QShortcut("Ctrl+F", self, activated=lambda: (self.search.show(), self.search.setFocus()))
        self.hideSearch = Qt.QShortcut("Esc", self, activated=lambda: (self.search.hide(), self.wb.setFocus()))
        self.quit = Qt.QShortcut("Ctrl+Q", self, activated=self.close)
        self.zoomIn = Qt.QShortcut("Ctrl++", self, activated=lambda: self.wb.setZoomFactor(self.wb.zoomFactor() + 0.2))
        self.zoomOut = Qt.QShortcut("Ctrl+-", self, activated=lambda: self.wb.setZoomFactor(self.wb.zoomFactor() - 0.2))
        self.zoomOne = Qt.QShortcut("Ctrl+=", self, activated=lambda: self.wb.setZoomFactor(1))

        # Add alt+left and right keys to navigate backward and forward
        Qt.QShortcut(QtCore.Qt.AltModifier + QtCore.Qt.Key_Left, self, activated=lambda: self.wb.back())
        Qt.QShortcut(QtCore.Qt.AltModifier + QtCore.Qt.Key_Right, self, activated=lambda: self.wb.forward())

        # Add components on the page
        self.sb.addPermanentWidget(self.search)

        # Finally, load the URL
        self.wb.load(QtCore.QUrl(url))

        try:
            self.wb.settings().setObjectCacheCapacities(0, 0, 0)
        except Exception:
            pass

    def adjustTitle(self):
        if 0 < self.progress < 100:
            self.setWindowTitle("%s (%s%%)" % (self.wb.title(), self.progress))
        else:
            self.setWindowTitle(self.wb.title())

    def setProgress(self, p):
        self.progress = p
        self.adjustTitle()


class SequanixQWebView(QWebEngineView):
    """This is the webview for the application.

    It represents a browser window, either the main one or a popup.
    It's a simple wrapper around QWebView that configures some basic settings.
    """

    def __init__(self, parent=None, **kwargs):
        """Constructor for the class"""
        super().__init__(parent, **kwargs)
        self.kwargs = kwargs

        # Javascript and other settings
        # ------------------------------------------------------------
        try:
            self.settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
            self.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
            self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        except:
            print("QtWebKit.QWebSettings not available for you PyQt version")

    def createWindow(self, type):
        """Handle requests for a new browser window.

        Method called whenever the browser requests a new window
        (e.g., <a target='_blank'> or window.open()).
        Overridden from QWebView to allow for popup windows, if enabled.
        """
        # this = Browser(self.url())
        # this.show()

        self.popup = SequanixQWebView(**self.kwargs)
        self.popup.setObjectName("web_content")
        self.popup.setWindowTitle("Sequana browser")
        self.popup.page().windowCloseRequested.connect(self.popup.close)
        self.popup.show()
        return self.popup
