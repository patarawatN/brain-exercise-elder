from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy, 
                                QHBoxLayout, QSlider, QProgressBar, QFrame, QGridLayout, QCheckBox,
                                QButtonGroup)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from random import sample, shuffle
from datetime import datetime
import json

class Word_Title(QWidget):
    def __init__(self, main_ui):
        super().__init__()

        self.main_ui = main_ui

        self.verticalLayout = QVBoxLayout()

        self.title = QLabel()
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setText("จำคำศัพท์")
        self.verticalLayout.addWidget(self.title)

        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(36)

        self.last_play = QLabel()
        self.last_play.setAlignment(Qt.AlignCenter)
        self.last_play.setFont(font)
        self.last_play.setText("การเล่นล่าสุด\n \n ")
        self.verticalLayout.addWidget(self.last_play)

        self.difficulty_layout = QHBoxLayout()
        self.difficulty_label = QLabel()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.difficulty_label.sizePolicy().hasHeightForWidth())
        self.difficulty_label.setSizePolicy(sizePolicy)
        self.difficulty_label.setFont(font)
        self.difficulty_label.setText("ระดับความยาก")
        self.difficulty_layout.addWidget(self.difficulty_label)

        self.difficulty_number = QLabel()
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.difficulty_number.sizePolicy().hasHeightForWidth())
        self.difficulty_number.setSizePolicy(sizePolicy)
        self.difficulty_number.setFont(font)
        self.difficulty_number.setText("1")

        self.difficulty_layout.addWidget(self.difficulty_number)
        self.verticalLayout.addLayout(self.difficulty_layout)

        self.difficulty_slider = QSlider()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.difficulty_slider.sizePolicy().hasHeightForWidth())
        self.difficulty_slider.setSizePolicy(sizePolicy)
        self.difficulty_slider.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: black;\n"
"    border: 0px solid #424242; \n"
"    height: 100px; \n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"    background-color: rgb(0, 80, 255); \n"
"    border: 5px solid rgb(12, 6, 56); \n"
"    width: 50px; \n"
"    height: 50px; \n"
"    line-height: 20px; \n"
"    margin-top: -50px; \n"
"    margin-bottom: -50px;  \n"
"    border-radius: 10px; \n"
"}"
"""QSlider::add-page:horizontal {
    background: black;
}
QSlider::sub-page:horizontal {
    background: rgb(0, 80, 255);
}""")
        self.difficulty_slider.setMaximum(4)
        self.difficulty_slider.setOrientation(Qt.Horizontal)
        self.verticalLayout.addWidget(self.difficulty_slider)

        self.play_button = QPushButton()
        font = QFont()
        font.setPointSize(72)
        font.setFamily("TH-Chara")
        self.play_button.setFont(font)
        self.play_button.setStyleSheet("QPushButton {\n"
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
        self.play_button.setText("เริ่ม")
        self.verticalLayout.addWidget(self.play_button)

        self.back_button = QPushButton()
        font.setPointSize(36)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton {\n"
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
        self.back_button.setObjectName("back_button")
        self.back_button.setText("กลับหน้าเลือกเกม")
        self.verticalLayout.addWidget(self.back_button)

        self.setLayout(self.verticalLayout)

        self.difficulty = 0
        self.changeDifficulty()
        self.connectEvent()
    
    def connectEvent(self):
        self.difficulty_slider.valueChanged.connect(self.changeDifficulty)
        self.play_button.clicked.connect(self.toWordMemo)
        self.back_button.clicked.connect(self.toGamePage)

    def changePage(self, index):
        self.main_ui.changePage(index)

    def changeDifficulty(self):
        difficulty = self.difficulty_slider.value()
        self.difficulty_number.setText("{0} คำ".format(difficulty + 3))
        self.difficulty = difficulty

    def setDifficulty(self, difficulty):
        self.difficulty_slider.setValue(difficulty)
        self.difficulty = difficulty

    def toGamePage(self):
        self.changePage(2)

    def toWordMemo(self):
        wordMemo_ui = self.main_ui.stackedWidget.widget(6)
        wordMemo_ui.start(self.difficulty)
        self.changePage(6)

class Word_Memo(QWidget):
    def __init__(self, main_ui):
        super().__init__()

        self.main_ui = main_ui

        self.verticalLayout = QVBoxLayout()

        # self.progressBar = QtWidgets.QProgressBar()
        # self.progressBar.setProperty("value", 24)
        # self.verticalLayout.addWidget(self.progressBar)

        big_font = QFont()
        big_font.setPointSize(72)
        big_font.setFamily("TH-Chara")

        self.font = QFont()
        self.font.setPointSize(36)
        self.font.setFamily("TH-Chara")
        self.font.setBold(True)

        self.label_order = QLabel()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_order.sizePolicy().hasHeightForWidth())
        self.label_order.setSizePolicy(sizePolicy)
        self.label_order.setAlignment(Qt.AlignCenter)
        self.label_order.setFont(self.font)
        self.label_order.setText("พ่อๆ แม่ๆ ช่วยจำคำศัพท์พวกนี้หน่อยนะ")
        self.verticalLayout.addWidget(self.label_order)

        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout.addWidget(self.line)
        
        self.gridLayout = QGridLayout()

        # Component will be generated
        
        self.verticalLayout.addLayout(self.gridLayout)

        

        self.next_button = QPushButton()
        self.next_button.setEnabled(True)
        self.next_button.setFont(big_font)
        self.next_button.setStyleSheet("QPushButton {\n"
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
        self.next_button.setText("จำได้หมดแล้ว")
        self.verticalLayout.addWidget(self.next_button)
        
        self.setLayout(self.verticalLayout)

        self.connectEvent()

    def connectEvent(self):
        self.next_button.clicked.connect(self.toWordMemPlay)

    def changePage(self, index):
        self.main_ui.changePage(index)

    def toWordMemPlay(self):
        wordPlay_ui = self.main_ui.stackedWidget.widget(7)
        wordPlay_ui.generateChoice(self.word_toPlay)
        self.clearLayout(self.gridLayout)
        self.changePage(7)

    def start(self,difficulty):
        difficulty += 3
        max_row = int(difficulty / 2)
        if difficulty % 2 == 1:
            max_row += 1
        max_col = 2
        positions = [(row,col) for row in range(max_row) for col in range(max_col)]

        with open("data/words.TXT","r") as file:
                words = file.read()
        word_list = words.split('\n')
        shuffle(word_list)
        self.word_toPlay = sample(word_list, int(difficulty * 2))
        self.word_memo = sample(self.word_toPlay, difficulty)
        self.time_start = datetime.now()
        for position,word in zip(positions,self.word_memo):
                label = QLabel(word)
                label.setFont(self.font)
                self.gridLayout.addWidget(label,*position)
        
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())



class Word_Play(QWidget):
    def __init__(self, main_ui):
        super().__init__()

        self.main_ui = main_ui

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_order = QLabel()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_order.sizePolicy().hasHeightForWidth())
        self.label_order.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setPointSize(36)
        font.setFamily("TH-Chara")
        self.font = QFont()
        self.font.setPointSize(36)
        self.font.setFamily("TH-Chara")
        self.font.setBold(True)
        self.label_order.setFont(font)
        self.label_order.setText("จำคำไหนได้บ้างนะ")
        self.label_order.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_order)

        self.gridLayout = QGridLayout()

        self.verticalLayout.addLayout(self.gridLayout)

        self.submit_button = QPushButton()
        font.setPointSize(72)
        font.setFamily("TH-Chara")
        font.setBold(False)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("QPushButton {\n"
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
        self.submit_button.setText("ส่งคำตอบ")
        self.verticalLayout.addWidget(self.submit_button)

        self.setLayout(self.verticalLayout)

        self.connnectEvent()

    def connnectEvent(self):
        self.submit_button.clicked.connect(self.submit)

    def changePage(self, index):
        self.main_ui.changePage(index)

    def toWordTitle(self):
        self.clearLayout(self.gridLayout)
        self.changePage(5)

    def submit(self):
        answer_list = []
        for checkbox in self.checkBox_list:
            if checkbox.isChecked():
                answer_list.append(checkbox.text())
        wordMemo_ui = self.main_ui.stackedWidget.widget(6)
        correct_list = wordMemo_ui.word_memo
        score_right = len(set(answer_list).intersection(set(correct_list)))
        score_panalty = len(set(answer_list).difference(set(correct_list)))
        score = score_right - score_panalty
        if score < 0 :
                score = 0
        accuracy = (score / len(correct_list)) * 100
        time_start = wordMemo_ui.time_start
        time_played = datetime.now() - time_start
        time_played = int(time_played.total_seconds())
        # score multiplier
        score_multiplier = 1
        if time_played <= 20:
            score_multiplier = 5
        elif time_played <= 30:
            score_multiplier = 3
        elif time_played <= 45:
            score_multiplier = 2
        elif time_played <= 60:
            score_multiplier = 1
        score = score * score_multiplier
        time_played_minute = int(time_played / 60)
        time_played_second = int(time_played % 60)
        cheering_word = ""
        max_score = len(correct_list)
        if score == max_score * 5:
            cheering_word = "พ่อๆแม่ๆทำได้ดีมากแล้วพยายามทำแบบฝึกเป็นประจำด้วยนะ"
        elif score >= max_score * 3:
            cheering_word = "พ่อๆแม่ๆยังพลาดไปบ้าง แต่ก็ทำได้ดีมากแล้วนะ"
        elif score >= max_score * 2:
            cheering_word = "พ่อๆแม่ๆยังช้าไปบ้าง แต่ก็ทำได้ดีมากแล้วนะ"
        elif score >= max_score * 1:
            cheering_word = "พ่อๆแม่ๆยังพลาดไปบ้างไม่ก็ข้าไป แต่ก็ทำได้ดีมากแล้วนะ"
        elif score >= 0:
            cheering_word = "พ่อๆแม่ๆทำได้ดีแล้ว ค่อยๆทำให้ถูกต้องไม่ก็เร็วขึ้นด้วยนะ"
        result_text = "การเล่นล่าสุด\nใช้เวลา {0} นาที {1} วินาที (โบนัสคะแนนคูณ {6}) จำถูก {4} คำ จำผิด {5} คำ \nได้ {2} คะแนน ({3})".format(time_played_minute, time_played_second, score, cheering_word, score_right, score_panalty, score_multiplier)
        wordTitle_ui = self.main_ui.stackedWidget.widget(5)
        wordTitle_ui.last_play.setText(result_text)
        record_stat = {
                            "date":time_start.isoformat(),
                                "time":time_played,
                                "score":score,
                                "accuracy":accuracy,
                                "right":score_right,
                                "wrong":score_panalty,
                            "difficulty":wordTitle_ui.difficulty
                        }
        # print(record_stat)
        user = self.main_ui.user
        user['word_memory_game']['play_history'].append(record_stat)
        # change difficulty
        if len(user['word_memory_game']['play_history']) % 5 == 0:
            user['word_memory_game']['recommend_difficulty'] += 1
        if (user['word_memory_game']['recommend_difficulty'] > 4):
            user['word_memory_game']['recommend_difficulty'] = 4
        save_data = user.copy()
        file_path = save_data.pop('filename')
        with open(file_path, "w") as outfile:
                json.dump(save_data, outfile, ensure_ascii=False)
        self.toWordTitle()

    def generateChoice(self, word_list):
        num = len(word_list)
        max_row = int(num / 2)
        # if num % 2 == 1:
        #         max_row += 1
        max_col = 2
        positions = [(row,col) for row in range(max_row) for col in range(max_col)]

        self.checkBox_list = []

        for position,word in zip(positions,word_list):
                choice = QCheckBox(word)
                choice.setFont(self.font)
                choice.setStyleSheet(" QCheckBox::indicator {width: 40px; height: 40px;} ")
                self.gridLayout.addWidget(choice,*position)
                self.checkBox_list.append(choice)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())