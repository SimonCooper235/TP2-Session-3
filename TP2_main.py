import sys
import traceback

from PyQt6.QtWidgets import QApplication

from vue_principale import VuePrincipal

def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

sys.excepthook = qt_exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = VuePrincipal()
    fenetre.show()
    sys.exit(app.exec())