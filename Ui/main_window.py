import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLabel,
    QStackedWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont


class PuppetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Puppet Parts Swapper")
        self.resize(600, 500)

        # Central widget that holds stacked pages
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Page 1: welcome / start screen
        self.page_start = QWidget()
        layout_start = QVBoxLayout(self.page_start)
        layout_start.setContentsMargins(60, 60, 60, 60)
        layout_start.setSpacing(30)

        btn = QPushButton("Start → Open Canvas")
        btn.setFixedHeight(70)
        btn.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        btn.clicked.connect(self.show_canvas)
        layout_start.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_start.addStretch()

        # Page 2: the "blank" canvas area (we'll put preview here later)
        self.page_canvas = QWidget()
        layout_canvas = QVBoxLayout(self.page_canvas)
        layout_canvas.setContentsMargins(20, 20, 20, 20)

        # Placeholder for now — big centered text / later image viewer
        self.placeholder_label = QLabel("Canvas Area\n(preview will appear here)\n\nReady for parts swapping")
        self.placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.placeholder_label.setStyleSheet("font-size: 24px; color: #888;")
        layout_canvas.addWidget(self.placeholder_label)

        # Add both pages to stack
        self.stack.addWidget(self.page_start)
        self.stack.addWidget(self.page_canvas)

        # Start on welcome page
        self.stack.setCurrentWidget(self.page_start)

    def show_canvas(self):
        self.stack.setCurrentWidget(self.page_canvas)
        self.setWindowTitle("Puppet Parts Swapper – Canvas")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")          # clean modern base style
    window = PuppetApp()
    window.show()
    sys.exit(app.exec())