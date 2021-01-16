from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sqlite3
import sys

import PyQt5
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QInputDialog, QWidget, QVBoxLayout, QLabel, \
    QLineEdit, QComboBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.do()

    def do(self):
        self.con = sqlite3.connect("coffee.db")
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

