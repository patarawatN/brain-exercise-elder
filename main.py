from user_creation import User_Creation
from user_selection import User_Seletion
from game_selection import Game_Selection
from math_ui import Math_Play, Math_Title
from word_memo_ui import Word_Memo, Word_Play, Word_Title

import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QStackedWidget, QVBoxLayout)

class App(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(User_Creation(self)) 
        self.stackedWidget.addWidget(User_Seletion(self)) 
        self.stackedWidget.addWidget(Game_Selection(self))
        self.stackedWidget.addWidget(Math_Title(self)) 
        self.stackedWidget.addWidget(Math_Play(self))
        self.stackedWidget.addWidget(Word_Title(self))
        self.stackedWidget.addWidget(Word_Memo(self))
        self.stackedWidget.addWidget(Word_Play(self))

        mainLayout.addWidget(self.stackedWidget)
        self.setLayout(mainLayout)
        first_page_index = 0
        user_directory = "/home/pi/brain-exercise-elder/user/"
        # user_directory = "user/"
        if len([f for f in os.listdir(user_directory) if f.endswith('.json')]) > 0:
            first_page_index = 1
        self.stackedWidget.setCurrentIndex(first_page_index) # will change to if there is some file
        self.setWindowTitle("ระบบบริหารสมองอัจฉริยะ")
        self.showMaximized()

        self.user = None

    def changePage(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def setUser(self, user):
        self.user = user

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())
    # shutdown
    # os.system("sudo shutdown -h now")