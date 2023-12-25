import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow

class TextAnalizator(QMainWindow):
    def __init__(self):
        super(TextAnalizator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TextAnalizator()
    window.show()

    sys.exit(app.exec())