import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from design import Ui_MainWindow

class TextAnalizator(QMainWindow):
    def __init__(self):
        super(TextAnalizator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnOpenFile.clicked.connect(self.openFileButtonClicked)
        self.ui.btnClear.clicked.connect(self.clearTextBrowser)
        #self.ui.btnRun.clicked.connect(self.showMessageBox)

    def openFileButtonClicked(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'All files (*)')

        if file_path:
            valid_extensions = ['.txt', '.doc', '.docx', '.rtf', '.pdf']
            _, file_extension = os.path.splitext(file_path)
            if file_extension.lower() in valid_extensions:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    self.ui.textBrowser.setPlainText(file_content)
            else:
               self.showMessageBox()

    def clearTextBrowser(self):
        self.ui.textBrowser.clear()

    def showMessageBox(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("ВЫ ДЕБИЛ")
        msg_box.setText("ВЫ ДЕБИЛ")
        msg_box.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TextAnalizator()
    window.show()

    sys.exit(app.exec())