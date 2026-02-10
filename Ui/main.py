# main.py
import sys
from PySide6.QtWidgets import QApplication
# from utils.logging import log_message

log_message("Template")

if __name__ == "__main__":
    try:
        log_message("Script launched")
        app = QApplication(sys.argv)
        app.setStyle("Fusion")
        window = TextAnimatorWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        log_message(f"Startup catastrophically failed: {str(e)}", level="CRITICAL")
        print(f"Template has entered the void: {str(e)}", file=sys.stderr)
        sys.exit(1)