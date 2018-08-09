from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from shiboken2 import wrapInstance 

def loadUiWidget(uifilename, parent=None):
    loader = QUiLoader()
    uifile = QFile(uifilename)
    uifile.open(QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = loadUiWidget("tester.ui")
    MainWindow.show()
    sys.exit(app.exec_())