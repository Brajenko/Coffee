import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from edit_window import editWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.show_table()

    def show_table(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.tableView.setModel(model)
        self.pushButton.clicked.connect(self.show_edit)

    def show_edit(self):
        ew = editWindow()
        ew.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
