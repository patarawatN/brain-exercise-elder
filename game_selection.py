from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QRadioButton
from PyQt5.QtGui import QFont, QPixmap

class Game_Selection(QWidget):
    def __init__(self, main_ui):
        super().__init__()

        self.verticalLayout = QVBoxLayout()
        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout_selected = QVBoxLayout()

        self.gameSelect_title = QLabel()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gameSelect_title.sizePolicy().hasHeightForWidth())
        self.gameSelect_title.setSizePolicy(sizePolicy)
        bold_font = QFont()
        bold_font.setFamily("TH-Chara")
        bold_font.setPointSize(36)
        bold_font.setBold(True)
        self.gameSelect_title.setFont(bold_font)
        self.gameSelect_title.setText("เลือกเกมที่ต้องการเล่นดีกว่า")
        self.verticalLayout_selected.addWidget(self.gameSelect_title)

        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(36)

        self.gameSelect_game1 = QRadioButton()
        self.gameSelect_game1.setFont(font)
        self.gameSelect_game1.setText("ฝึกคำนวนชวนคิด")
        self.gameSelect_game1.setChecked(True)
        self.verticalLayout_selected.addWidget(self.gameSelect_game1)
        self.gameSelect_game2 = QRadioButton()
        self.gameSelect_game2.setFont(font)
        self.gameSelect_game2.setText("จำคำศัพท์")
        self.verticalLayout_selected.addWidget(self.gameSelect_game2)
        self.horizontalLayout.addLayout(self.verticalLayout_selected)

        self.verticalLayout_description = QVBoxLayout()
        self.description_image_label = QLabel()
        self.description_image_math = QPixmap('/home/pi/brain-exercie-elder/data/image/pay-gd00e9afc9_1280.jpg')
        self.description_image_word = QPixmap('/home/pi/brain-exercie-elder/data/image/words.jpg')
        self.description_image_label.setPixmap(self.description_image_math)
        self.description_image_label.setScaledContents(True)
        self.description_image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.verticalLayout_description.addWidget(self.description_image_label)
        self.gameSelect_description = QLabel()
        self.gameSelect_description.setFont(font)
        self.gameSelect_description.setText("คำอธิบาย \nฝึกคำนวนตัวเลขง่าย ๆ\nมีบวก ลบ คูณ\nจำนวน 25 ข้อ")
        self.verticalLayout_description.addWidget(self.gameSelect_description)
        self.horizontalLayout.addLayout(self.verticalLayout_description)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.game_startButton = QPushButton()
        big_font = QFont()
        big_font.setPointSize(72)
        big_font.setBold(True)
        big_font.setWeight(75)
        big_font.setFamily("TH-Chara")
        self.game_startButton.setFont(big_font)
        self.game_startButton.setStyleSheet("QPushButton {\n"
"background-color:rgb(0, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 147, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgb(0, 53, 168);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:rgb(221, 221, 221);\n"
"color:rgb(97, 97, 97);\n"
"}")
        self.game_startButton.setText("เลือกเกม")
        self.verticalLayout.addWidget(self.game_startButton)

        self.game_backButton = QPushButton()
        # font = QFont()
        # font.setPointSize(36)
        # font.setFamily("TH-Chara")
        # font.setBold(False)
        self.game_backButton.setFont(font)
        self.game_backButton.setStyleSheet("QPushButton {\n"
"background-color:rgb(255, 255, 255);\n"
"border:1px solid rgb(0, 85, 255);\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border:5px solid rgb(24, 147, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border:5px solid rgb(0, 53, 168);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:rgb(221, 221, 221);\n"
"border:none;\n"
"color:rgb(97, 97, 97);\n"
"}")
        self.game_backButton.setText("กลับไปหน้าเลือกชื่อ")
        self.verticalLayout.addWidget(self.game_backButton)

        self.setLayout(self.verticalLayout)

        self.main_ui = main_ui
        self.game = 1
        self.connectEvent()


    def connectEvent(self):
        self.game_startButton.clicked.connect(self.toGameTitle)
        self.game_backButton.clicked.connect(self.toSelectionPage)
        self.gameSelect_game1.toggled.connect(lambda:self.choosedGame(1))
        self.gameSelect_game2.toggled.connect(lambda:self.choosedGame(2))


    def changePage(self, index):
        self.main_ui.changePage(index)

    def choosedGame(self, game):
        self.game = game
        if self.game == 1:
            self.description_image_label.setPixmap(self.description_image_math)
            self.gameSelect_description.setText("คำอธิบาย \nฝึกคำนวนตัวเลขง่าย ๆ\nมีบวก ลบ คูณ\nจำนวน 25 ข้อ")
        else:
            self.description_image_label.setPixmap(self.description_image_word)
            self.gameSelect_description.setText("คำอธิบาย \nจำคำที่ให้มาเร็วที่สุด\nและเลือกคำที่จำได้")

    def toGameTitle(self):
        if self.game == 1:
                self.toMathTitle()
        else:
                self.toWordTitle()

    def toSelectionPage(self):
        self.main_ui.setUser(None)
        self.changePage(1)

    def toMathTitle(self):
        user = self.main_ui.user
        difficulty = user['math_game']['recommend_difficulty']
        mathTitle_ui = self.main_ui.stackedWidget.widget(3)
        mathTitle_ui.setDifficulty(difficulty)
        self.changePage(3)

    def toWordTitle(self):
        user = self.main_ui.user
        difficulty = user['word_memory_game']['recommend_difficulty']
        wordTitle_ui = self.main_ui.stackedWidget.widget(5)
        wordTitle_ui.setDifficulty(difficulty)
        self.changePage(5)