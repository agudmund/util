import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class BlankWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("blankito")
        self.resize(640, 480)           # change size if you prefer

        # That's literally it — empty window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")          # clean / modern base look
    window = BlankWindow()
    window.show()
    sys.exit(app.exec())