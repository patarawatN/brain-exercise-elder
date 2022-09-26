from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont
import json, datetime

class User_Creation(QWidget):
    def __init__(self, main_ui):
        super().__init__()

        self.verticalLayout = QVBoxLayout()

        big_font = QFont()
        big_font.setFamily("TH-Chara")
        big_font.setPointSize(72)
        big_font.setBold(True)
        big_font.setItalic(False)
        big_font.setWeight(75)

        self.userCreation_title = QLabel()
        self.userCreation_title.setFont(big_font)
        self.userCreation_title.setText("มาสร้างชื่อกันเถอะ")
        self.verticalLayout.addWidget(self.userCreation_title)

        self.userCreation_formName = QLabel()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userCreation_formName.sizePolicy().hasHeightForWidth())
        self.userCreation_formName.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(36)
        self.userCreation_formName.setFont(font)
        self.verticalLayout.addWidget(self.userCreation_formName)
        self.userCreation_formName.setText("โปรดกรอก \"ชื่อ\" ที่ต้องการในกล่องข้างล่าง")

        self.userCreation_formNameInput = QLineEdit()
        self.userCreation_formNameInput.setFont(font)
        self.verticalLayout.addWidget(self.userCreation_formNameInput)

        self.userCreation_createButton = QPushButton()
        self.userCreation_createButton.setEnabled(False)
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(72)
        self.userCreation_createButton.setFont(font)
        self.userCreation_createButton.setStyleSheet("QPushButton {\n"
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
        self.userCreation_createButton.setText("สร้างชื่อใหม่")
        self.verticalLayout.addWidget(self.userCreation_createButton)

        self.userCreation_previousButton = QPushButton()
        self.userCreation_previousButton.setEnabled(True)
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.userCreation_previousButton.setFont(font)
        self.userCreation_previousButton.setStyleSheet("QPushButton {\n"
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
        self.userCreation_previousButton.setAutoDefault(True)
        self.userCreation_previousButton.setObjectName("userCreation_previousButton")
        self.userCreation_previousButton.setText("กลับไปหน้าเลือกชื่อ")
        self.verticalLayout.addWidget(self.userCreation_previousButton)

        self.setLayout(self.verticalLayout)

        self.main_ui = main_ui
        self.connectEvent()

    def connectEvent(self):
        self.userCreation_formNameInput.textChanged.connect(self.text_changed)
        self.userCreation_createButton.clicked.connect(self.createName)
        self.userCreation_previousButton.clicked.connect(self.toSelectionPage)

    def changePage(self, index):
        self.main_ui.changePage(index)

    def text_changed(self, text):
        if text:
            self.userCreation_createButton.setEnabled(True)
        else:
            self.userCreation_createButton.setEnabled(False)

    def createName(self):
        # create file
        name = self.userCreation_formNameInput.text()
        name = name.strip()
        name = name.replace(" ","_")
        now = datetime.datetime.now().isoformat()
        user = {
                "username":name,
                "create_time":now,
                "login_history":[],
                "math_game":{
                        "recommend_difficulty":0,
                        "play_history":[]
                        },
                "word_memory_game":{
                        "recommend_difficulty":0,
                        "play_history":[]
                        }
                }

        file_name = name + "__" + now
        file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "_" + str(hash(file_name))
        file_location = "/home/pi/brain-exercise-elder/user/" + file_name + ".json"
        with open(file_location, "w") as outfile:
                json.dump(user, outfile, ensure_ascii=False)
        self.userCreation_formNameInput.clear()
        # to next page
        self.main_ui.stackedWidget.widget(1).refreshList()
        self.toSelectionPage()

    def toSelectionPage(self):
        self.changePage(1)