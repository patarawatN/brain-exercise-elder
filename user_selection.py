from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
from PyQt5.QtGui import QFont

import os, json, datetime

class User_Seletion(QWidget):
        def __init__(self, main_ui):
                super().__init__()
                self.verticalLayout = QVBoxLayout()

                self.userSelection_title = QLabel()
                big_font = QFont()
                big_font.setFamily("TH-Chara")
                big_font.setPointSize(72)
                big_font.setBold(True)
                big_font.setItalic(False)
                big_font.setWeight(75)
                self.userSelection_title.setFont(big_font)
                self.userSelection_title.setAlignment(Qt.AlignCenter)
                self.userSelection_title.setObjectName("userSelection_title")
                self.userSelection_title.setText("ระบบบริหารสมองอัจฉริยะ")
                self.verticalLayout.addWidget(self.userSelection_title)

                self.userSelection_listTitle = QLabel()
                font = QFont()
                font.setFamily("TH-Chara")
                font.setPointSize(36)
                self.userSelection_listTitle.setFont(font)
                self.userSelection_listTitle.setText("เลือกชื่อของตัวเองได้เลย")
                self.verticalLayout.addWidget(self.userSelection_listTitle)

                self.userSelection_list = QListWidget()
                # font = QtGui.QFont()
                # font.setFamily("TH-Chara")
                # font.setPointSize(36)
                self.userSelection_list.setFont(font)

                # item = QListWidgetItem()
                # self.userSelection_list.addItem(item)

                self.verticalLayout.addWidget(self.userSelection_list)

                self.userSelection_selectButton = QPushButton()
                # font = QtGui.QFont()
                # font.setFamily("TH-Chara")
                # font.setPointSize(36)
                self.userSelection_selectButton.setEnabled(False)
                self.userSelection_selectButton.setFont(font)
                self.userSelection_selectButton.setStyleSheet("QPushButton {\n"
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
                self.userSelection_selectButton.setText("เลือกชื่อนี้")
                self.verticalLayout.addWidget(self.userSelection_selectButton)

                self.userSeletion_createNewLable = QLabel()
                # font = QtGui.QFont()
                # font.setFamily("TH-Chara")
                # font.setPointSize(36)
                self.userSeletion_createNewLable.setFont(font)
                self.userSeletion_createNewLable.setObjectName("userSeletion_createNewLable")
                self.userSeletion_createNewLable.setText("ยังไม่มีชื่อของตัวเองหรือ ?")
                self.verticalLayout.addWidget(self.userSeletion_createNewLable)

                self.userSelection_createNewButton = QPushButton()
                # font = QtGui.QFont()
                # font.setFamily("TH-Chara")
                # font.setPointSize(36)
                self.userSelection_createNewButton.setFont(font)
                self.userSelection_createNewButton.setStyleSheet("QPushButton {\n"
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
                self.userSelection_createNewButton.setText("สร้างชื่อใหม่")
                self.verticalLayout.addWidget(self.userSelection_createNewButton)


                self.userSelection_quit = QPushButton()
                # font = QFont()
                # font.setFamily("TH-Chara")
                # font.setPointSize(36)
                self.userSelection_quit.setFont(font)
                self.userSelection_quit.setStyleSheet("QPushButton {\n"
        "background-color:rgb(255, 87, 90);\n"
        "color:rgb(0, 0, 0);\n"
        "border:none;\n"
        "border-radius: 25px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "background-color:rgb(255, 0, 0);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "background-color:rgb(172, 56, 58);\n"
        "}\n"
        "\n"
        "QPushButton:disabled {\n"
        "background-color:rgb(221, 221, 221);\n"
        "color:rgb(97, 97, 97);\n"
        "}")
                self.userSelection_quit.setText("ออกจากระบบ")
                self.verticalLayout.addWidget(self.userSelection_quit)

                self.setLayout(self.verticalLayout)

                self.main_ui = main_ui
                self.connectEvent()
                self.refreshList()

        def connectEvent(self):
                self.userSelection_list.itemSelectionChanged.connect(self.itemSelected)
                self.userSelection_selectButton.clicked.connect(self.logIn)
                self.userSelection_createNewButton.clicked.connect(self.toCreatePage)
                # shut down
                # self.userSelection_quit.clicked.connect(self.shutDown)


        def changePage(self, index):
                self.main_ui.changePage(index)

        # when come to this page
        def refreshList(self):
                # clear list
                self.userSelection_list.clear()
                # fetch list 
                path_to_json = 'user/'
                self.users = []
                for file in os.listdir(path_to_json):
                        if file.endswith('.json'):
                                full_filename = path_to_json + file
                                with open(full_filename,'r') as fi:
                                        dict = json.load(fi)
                                        dict['filename'] = full_filename
                                        self.users.append(dict)

                # locale.setlocale(locale.LC_ALL, 'th_TH.utf8')
                # users = sorted(users, key=lambda k: (k['username']))
                
                for i in range(len(self.users)):
                        name = self.users[i]['username']
                        # time = self.users[i]['create_time']
                        # time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f')
                        # time = datetime.datetime.strftime(time,'%d/%m/%Y %H:%M:%S')
                        item = name.replace("_"," ")
                        self.userSelection_list.addItem(item)
                # self.userSelection_list.sortItems()

        def itemSelected(self):
                self.userSelection_selectButton.setEnabled(True)

        def logIn(self):
                self.main_ui.setUser(self.users[self.userSelection_list.currentRow()])
                now = datetime.datetime.now().isoformat()
                self.main_ui.user['login_history'].append(now)
                save_data = self.main_ui.user.copy()
                file_path = save_data.pop('filename')
                with open(file_path, "w") as outfile:
                        json.dump(save_data, outfile, ensure_ascii=False)
                self.toGamePage()

        def toCreatePage(self):
                self.changePage(0)
        
        def toGamePage(self):
                self.changePage(2)

        def shutDown(self):
                os.system("sudo shutdown -h now")