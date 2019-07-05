from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from sys import exit, argv
from os import chdir, path
from random import choice
chdir(path.abspath(path.dirname(argv[0])))

class Window(QWidget):
    repeat = True
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        mainLayout = QVBoxLayout()
        gameLayout = QHBoxLayout()
        PlayerLayout = QVBoxLayout()
        RivalLayout = QVBoxLayout()
        ButtonsLayout = QHBoxLayout()

        self.Scores = QLabel("Scores Going To Show Here")
        mainLayout.addWidget(self.Scores)
        mainLayout.addLayout(gameLayout)

        gameLayout.addLayout(PlayerLayout)
        gameLayout.addLayout(RivalLayout)

        self.Player = QLabel()
        self.Rival = QLabel()
        self.Player.setPixmap(QPixmap("PlayerDescription.jpg"))
        self.Rival.setPixmap(QPixmap("RivalDescription.jpg"))
        PlayerLayout.addWidget(self.Player)
        RivalLayout.addWidget(self.Rival)

        PlayerLayout.addLayout(ButtonsLayout)

        Rock = QPushButton("Rock")
        Paper = QPushButton("Paper")
        Scissors = QPushButton("Scissors")

        Rock.clicked.connect(self.move)
        Paper.clicked.connect(self.move)
        Scissors.clicked.connect(self.move)

        ButtonsLayout.addStretch()
        ButtonsLayout.addWidget(Rock)
        ButtonsLayout.addWidget(Paper)
        ButtonsLayout.addWidget(Scissors)
        ButtonsLayout.addStretch()

        Status = QLabel("Status Going To Appear Here")
        RivalLayout.addWidget(Status)

        self.Player_score ,self.Rival_score = 0, 0

        self.setLayout(mainLayout)
        self.setWindowTitle("Rock Paper Scissors")
        self.show()

    def move(self):
        Player_selected = self.sender().text()
        Player_full_path = path.join(path.abspath(path.dirname(argv[0])), "mirror" + Player_selected)
        self.Player.setPixmap(QPixmap("{}.jpg".format(Player_full_path)))

        Rival_selected = choice(["Rock", "Paper", "Scissors"])
        Rival_full_path = path.join(path.abspath(path.dirname(argv[0])), Rival_selected)
        self.Rival.setPixmap(QPixmap("{}.jpg".format(Rival_full_path)))

        self.win(Player_selected, Rival_selected)
    
    def win(self, Player_selected, Rival_selected):
        if Player_selected == 'Scissors':
            if Rival_selected == 'Rock':
                self.Rival_score += 1
            elif Rival_selected == 'Paper':
                self.Player_score += 1
        elif Player_selected == 'Rock':
            if Rival_selected == 'Scissors':
                self.Player_score += 1
            elif Rival_selected == 'Paper':
                self.Rival_score += 1
        elif Player_selected == 'Paper':
            if Rival_selected == 'Rock':
                self.Player_score += 1
            elif Rival_selected == 'Scissors':
                self.Rival_score += 1
        
        self.Scores.setText("Player Score: {}    Rival Score:  {}".format(self.Player_score, self.Rival_score))
        
        if self.Player_score == 3 or self.Rival_score == 3:
            self.gameOver()
        
    def gameOver(self):
        scores = {self.Player_score: "Player", self.Rival_score: "Rival"}
        Repeat = QMessageBox.question(self, 'Game Over', '{} Won this game!! Want to play again?'.format(scores[max(scores)]), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if Repeat == QMessageBox.No:
            exit()
        else:
            self.Restart()

    def Restart(self):
        self.Player.setPixmap(QPixmap("PlayerDescription.jpg"))
        self.Rival.setPixmap(QPixmap("RivalDescription.jpg"))
        self.Player_score ,self.Rival_score = 0, 0
        self.Scores.setText("Player Score: {}    Rival Score:  {}".format(self.Player_score, self.Rival_score))
        
if __name__ == "__main__":
    app = QApplication(argv)
    window = Window()
    exit(app.exec_())

