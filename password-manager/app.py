import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStyledItemDelegate, QLineEdit, QDialog
from PySide6 import QtSql
from PySide6.QtCore import Qt

from ui.ui_main import Ui_MainWindow
import ui.resources_rc
import buttons_characters
import generate_password
from connect_db import Database
from ui.ui_dialogNew import Ui_Dialog


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


class PasswordManager(QMainWindow):
    def __init__(self):
        super(PasswordManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.connection = Database()
        self.view_data()
        
        delegate = AlignDelegate(self.ui.tableView)
        self.ui.tableView.setItemDelegateForColumn(0, delegate)
        self.ui.tableView.setItemDelegateForColumn(1, delegate)
        self.ui.tableView.setItemDelegateForColumn(2, delegate)
        self.ui.tableView.setItemDelegateForColumn(3, delegate)
        
        self.ui.btn_delete_password.clicked.connect(self.delete_current_password)
        self.connect_slider_to_spinbox()
        self.set_password()
        self.ui.btn_visibility.clicked.connect(self.change_password_visibility)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)
        self.ui.btn_new_password.clicked.connect(self.open_new_password_window)
        self.ui.btn_search.clicked.connect(self.search_table_by_service)
    
        for btn in buttons_characters.GENERATE_PASSWORD:
            getattr(self.ui, btn).clicked.connect(self.set_password)

    def view_data(self) -> None:
        self.model = QtSql.QSqlTableModel()
        self.ui.tableView.setModel(self.model)
        self.model.setTable("Passwords")
        self.model.select()
        
    def open_new_password_window(self) -> None:
        self.new_window = QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_save.clicked.connect(self.add_new_password)
        
    def add_new_password(self) -> None:
        service = self.ui_window.line_service.text()
        login = self.ui_window.line_login.text()
        password = self.ui_window.line_password.text()
        
        self.connection.add_new_password_query(service, login, password)
        self.view_data()
        self.new_window.close()
    
    def delete_current_password(self) -> None:
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        self.connection.delete_password_query(id)
        self.view_data()
        
    def connect_slider_to_spinbox(self) -> None:
        self.ui.slider_lenght.valueChanged.connect(self.ui.box_lenght.setValue)
        self.ui.box_lenght.valueChanged.connect(self.ui.slider_lenght.setValue)
        self.ui.box_lenght.valueChanged.connect(self.set_password)

    def get_characters(self) -> str:
        chars = ''

        for btn in buttons_characters.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value

        return chars

    def set_password(self) -> None:
        try:
            self.ui.password_line.setText(generate_password.create_new(length=self.ui.slider_lenght.value(), characters=self.get_characters()))
        except IndexError:
            self.ui.password_line.clear()

    def change_password_visibility(self) -> None:
        if self.ui.btn_visibility.isChecked():
            self.ui.password_line.setEchoMode(QLineEdit.Password)
        else:
            self.ui.password_line.setEchoMode(QLineEdit.Normal)

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.password_line.text())
        
    def search_table_by_service(self) -> None:
        search = self.ui.line_search.text()
        f = " Service LIKE '%{}%'".format(search) if search else search
        self.model.setFilter(f)
        self.model.select()
        
       
if __name__ == "__main__":
    application = QApplication(sys.argv)

    window = PasswordManager()
    window.show()

    sys.exit(application.exec())
