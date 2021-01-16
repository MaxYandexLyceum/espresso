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
        uic.loadUi("ui2.ui", self)
        self.upd()
        self.pushButton.clicked.connect(self.add)
        # Создадим виджет и сохраним ссылку на него

    def add(self):
        self.dialog = Dialog()
        self.dialog.resize(200, 200)
        self.dialog.setWindowTitle("Форма")

        self.label = QLabel("Название")

        self.name_input1 = QLineEdit(self)

        self.label1 = QLabel("Год")

        self.name_input2 = QLineEdit(self)

        self.label2 = QLabel("Жанр")

        self.combo = QComboBox(self)

        self.combo.addItem("комедия")
        self.combo.addItem("драма")
        self.combo.addItem("мелодрама")
        self.combo.addItem("детектив")
        self.combo.addItem("документальный")
        self.combo.addItem("ужасы")
        self.combo.addItem("музыка")
        self.combo.addItem("фантастика")
        self.combo.addItem("анимация")
        self.combo.addItem("биография")
        self.combo.addItem("боевик")
        self.combo.addItem("приключения")
        self.combo.addItem("война")
        self.combo.addItem("семейный")
        self.combo.addItem("триллер")
        self.combo.addItem("фэнтези")
        self.combo.addItem("вестерн")
        self.combo.addItem("мистика")
        self.combo.addItem("короткометражный")
        self.combo.addItem("мюзикл")
        self.combo.addItem("исторический")
        self.combo.addItem("нуар")

        self.label3 = QLabel("Длительность")

        self.name_input4 = QLineEdit(self)

        self.label4 = QLabel("")
        self.b = QPushButton("Добавить")
        self.b.clicked.connect(self.do)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name_input1)
        layout.addWidget(self.label1)
        layout.addWidget(self.name_input2)
        layout.addWidget(self.label2)
        layout.addWidget(self.combo)
        layout.addWidget(self.label3)
        layout.addWidget(self.name_input4)
        layout.addWidget(self.b)
        layout.addWidget(self.label4)
        layout.addStretch()

        self.dialog.setLayout(layout)
        self.dialog.show()

    def do(self):
        self.d = {
            "комедия": 1,
            "драма": 2,
            "мелодрама": 3,
            "детектив": 4,
            "документальный": 5,
            "ужасы": 6,
            "музыка": 7,
            "фантастика": 8,
            "анимация": 9,
            "биография": 10,
            "боевик": 11,
            "приключения": 13,
            "война": 15,
            "семейный": 16,
            "триллер": 17,
            "фэнтези": 18,
            "вестерн": 19,
            "мистика": 20,
            "короткометражный": 21,
            "мюзикл": 22,
            "исторический": 23,
            "нуар": 24,
        }
        self.label4.setText("")
        nazvanie = self.name_input1.text()
        try:
            god = int(self.name_input2.text())
            dlitelnost = int(self.name_input4.text())
        except Exception:
            self.label4.setText("Ошибка ввода")
            return
        zhanr = self.combo.currentText()
        if (god < 0 or god > 2021) or dlitelnost < 0 or (not nazvanie or not god or not dlitelnost or not zhanr):
            self.label4.setText("Ошибка ввода")
            return
        self.con = sqlite3.connect("films_db.sqlite")
        cur = self.con.cursor()
        cur.execute('INSERT INTO films (id, title, year, genre, duration) VALUES (?, ?, ?, ?, ?)', (self.n, nazvanie, god, self.d[zhanr], dlitelnost))
        self.con.commit()
        cur.close()
        self.upd()



    def upd(self):
        self.con = sqlite3.connect("films_db.sqlite")
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM films INNER JOIN genres ON films.genre = genres.id").fetchall()
        result1 = []
        for i in result:
            result1.append((i[0], i[1], i[2], i[6], i[4]))
        self.n = result[-1][0] + 1
        self.tableWidget.setRowCount(len(result1))
        self.tableWidget.setColumnCount(len(result1[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result1):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


class Dialog(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

