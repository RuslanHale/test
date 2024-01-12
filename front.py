from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from game_configuration import place_1, place_2, red_team, blue_team
from random import randint
import sys


class MainWindow(QMainWindow):  # главное окно
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Tanks")  # заголовок окна
        self.move(100, 300)  # положение окна
        self.resize(600, 300)  # размер окна
        self.lbl = QLabel('Поле игрока/противника', self)
        self.lbl.move(150, 0)


class Group_of_button(MainWindow):
    buttons_list = []
    def __init__(self, window, place, base_coord_x=0, base_coord_y=0, visible=False):
        super().__init__()
        self.window = window
        self.buttons_list = []
        self.base_coord_x = base_coord_x
        self.base_coord_y = base_coord_y
        self.visible = visible

        for row in range(len(place.matrix)):
            for elem in range(len(place.matrix[row])):
                text = '_'
                active = True
                if visible:
                    text = place.matrix[row][elem]
                    active = False

                new_btn = Button(
                    self.base_coord_x + elem * 50,
                    self.base_coord_y + row * 50,
                    self.window,
                    text,
                    active
                )
                if place.matrix[row][elem] != '_':
                    new_btn.is_tank = True
                    new_btn.brand_copy = place.matrix[row][elem]

                Group_of_button.buttons_list.append(new_btn)


class Button():
    def __init__(self, x, y, window, text, active):
        self.button1 = QPushButton(window)
        self.button1.resize(50, 50)
        self.button1.setText(text)
        self.button1.setFont(QFont('Times', 8, QFont.Bold))
        self.button1.move(x, y)
        self.button1.clicked.connect(self.press)
        self.is_tank = False
        self.brand_copy = ''
        self.dead = False
        if not active:
            self.button1.setEnabled(False)

    def press(self):
        if self.button1.text() == '_':
            if self.is_tank:
                self.button1.setText(f'{self.brand_copy}\n УБИТ')
                score.blue_team -= 1
                score.get_score()
            else:
                self.button1.setText("x")
            self.button1.setEnabled(False)

        n_max = len(Group_of_button.buttons_list) // 2 - 1
        is_not_choice_killed = True
        n = 0
        while is_not_choice_killed:
            n = randint(0, n_max)
            if Group_of_button.buttons_list[n].dead == False:
                is_not_choice_killed = False
        Group_of_button.buttons_list[n].kill_text()
        Group_of_button.buttons_list[n].dead = True



    def kill_text(self):
        if self.button1.text() == '_':
            self.button1.setText('x')
        else:
            self.button1.setText(f'{self.brand_copy}\n УБИТ')
            score.red_team -= 1
            score.get_score()

class Score:
    def __init__(self, red_team, blue_team):
        self.red_team = len(red_team)
        self.blue_team = len(blue_team)

    def get_score(self):
        if self.red_team == 0:
            self.show_win_message('Blue Team wins')
        elif self.blue_team == 0:
            self.show_win_message('Red Team wins')

    def show_win_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Information MessageBox")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    btn = Group_of_button(win, place_1, 10, 30, True)
    btn2 = Group_of_button(win, place_2, 300, 30)

    score = Score(red_team, blue_team)

    win.show()
    sys.exit(app.exec_())







