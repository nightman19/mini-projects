import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QWidget
# from PyQt6.QWidget import 
from PyQt6.QtWebEngineWidgets import QWebEngineView

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.view = QWebEngineView()
        self.view.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.view)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
