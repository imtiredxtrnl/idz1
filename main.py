import sys
import os
from dbcontext import Context
from ResultModel import ResultModel
from analizer import TextAnalizatorCore
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPushButton
from PySide6.QtGui import QStandardItem, QStandardItemModel
from design import Ui_MainWindow

class TextAnalizator(QMainWindow):
    def __init__(self):
        super(TextAnalizator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        Context.create_table()
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
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Result")
        box_text = self.set_response_str(result)
        msg_box.setText(box_text)
        result.print_fields()
        ok_button = QPushButton('OK', msg_box)
        msg_box.addButton(ok_button, QMessageBox.AcceptRole)
        new_button = QPushButton('Save', msg_box)
        msg_box.addButton(new_button, QMessageBox.ActionRole)
        result_choise = msg_box.exec()
        if result_choise == 1:
            Context.insert_result(result)
            self.generate_report()
            
        
    
    def set_response_str(self, result):
        res_str = ""
        res_str += "Total words:" + str(result.words) + "\n"
        res_str += "Specified words amount:" + str(result.specWords) + "\n"
        res_str += "Symbols:" + str(result.symbols) + "\n"
        res_str += "Symbols (No Spaces):" + str(result.symbolsNoSpaces) + "\n"
        res_str += "Letters:" + str(result.letters) + "\n"
        res_str += "Foreign Words:" + str(result.foreignWords) + "\n"
        res_str += "Water percentage:" + str(result.waterPercenatge) + "\n"
        res_str += "Marks:" + str(result.marks) + "\n"
        res_str += "Stop Words:" + str(result.stopWords) + "\n"
        res_str += "Words distribution through text with water:" + "\n"
        for word, count, percentage in result.wordsDistribution:
            res_str += (f"Word: {word}, Count: {count}, Percentage: {percentage:.2f}%") + "\n"
        res_str += "Words distribution through text without water:" + "\n"
        for word, count, percentage in result.wordsDistributionNoStopWords:
            res_str += (f"Word: {word}, Count: {count}, Percentage: {percentage:.2f}%") 
        return res_str
        
        




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TextAnalizator()
    window.show()

    sys.exit(app.exec())