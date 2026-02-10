# main.py
import sys

from PySide6.QtWidgets import QApplication

from main_window import TrelloCushionsWindow
from utils.logging import log_message


if __name__ == "__main__":
    log_message("Script launched")
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = TrelloCushionsWindow()
    window.show()
    sys.exit(app.exec())