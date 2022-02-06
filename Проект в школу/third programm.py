import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500, 300, 800, 600)
        self.setFixedSize(800, 600)
        self.setWindowTitle('Тестовое окно')

        self.font1 = QFont()
        self.font1.setPointSize(20)

        self.btn1 = QPushButton(self)
        self.btn1.setText('Приветствие\nпользователя')
        self.btn1.resize(300, 100)
        self.btn1.move(50, 200)
        self.btn1.setFont(self.font1)
        self.btn1.clicked.connect(self.btn1_pushed)

        self.btn2 = QPushButton(self)
        self.btn2.setText('Прощание\nс пользователем')
        self.btn2.resize(300, 100)
        self.btn2.move(450, 200)
        self.btn2.setFont(self.font1)
        self.btn2.clicked.connect(self.btn2_pushed)

        self.lbl = QLabel(self)
        self.lbl.setText('Введите имя пользователя')
        self.lbl.setFont(self.font1)
        self.lbl.move(250, 50)
        self.lbl.resize(400, 50)

        self.edit = QLineEdit(self)
        self.edit.setFont(self.font1)
        self.edit.move(100, 500)
        self.edit.resize(600, 50)

    def btn1_pushed(self):
        st = self.edit.text()
        if len(st) == 0:
            self.lbl.setText('Вы ничего не ввели')
        else:
            self.lbl.setText(f'Приветствую, {st}')

    def btn2_pushed(self):
        st = self.edit.text()
        if len(st) == 0:
            self.lbl.setText('Вы ничего не ввели')
        else:
            self.lbl.setText(f'Всего хорошего, {st}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
