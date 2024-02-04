import sys
import os
from dbcontext import Context
from analizer import TextAnalizatorCore
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel
from design import Ui_MainWindow

class TextAnalizator(QMainWindow):
    def __init__(self):
        super(TextAnalizator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.generate_report()
        self.ui.btnOpenFile.clicked.connect(self.openFileButtonClicked)
        self.ui.btnClear.clicked.connect(self.clearTextBrowser)
        self.ui.btnDelRow.clicked.connect(self.delete_selected_rows)
        self.ui.btnRun.clicked.connect(self.run_analizer)
        self.file_path = ""
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
                self.file_path = file_path
            else:
               self.showMessageBox()

    def clearTextBrowser(self):
        self.ui.textBrowser.clear()

    def showMessageBox(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("ВЫ ДЕБИЛ")
        msg_box.setText("ВЫ ДЕБИЛ")
        msg_box.exec_()
        
    def generate_report(self):
        # Create a data model
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            "ID", "Text", "Words", "Spec Words", "Symbols", "Symbols No Spaces",
            "Letters", "Foreign Words", "Water Percentage", "Marks", "Stop Words",
            "Words Distribution", "Words Distribution No Stop Words"
        ])
        rows = Context.get_all_results()
        print("Fetched rows:", rows)
        for row in rows:
            items = [QStandardItem(str(item)) for item in row]
            self.model.appendRow(items)
        self.ui.tableView.setModel(self.model)
        print("Populated model:", self.model)
        
    def delete_selected_rows(self):
        selected_indexes = self.ui.tableView.selectionModel().selectedIndexes()
        if selected_indexes:
            selected_rows = list(set(index.row() for index in selected_indexes))
            selected_rows.sort(reverse=True)
            for row in selected_rows:
                result_id_item = self.model.item(row, 0)
                result_id = int(result_id_item.text())
                Context.delete_one_result(result_id)
                self.model.removeRow(row)
                
    def run_analizer(self):
        words_to_search = self.ui.textFieldSearch.toPlainText().split()
        words_to_ignore = self.ui.textFieldIgnore.toPlainText().split()
        result = TextAnalizatorCore.Analize(self.file_path, words_to_search, words_to_ignore)
        result.print_fields()





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TextAnalizator()
    window.show()

    sys.exit(app.exec())