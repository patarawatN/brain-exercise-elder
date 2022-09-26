from datetime import datetime
import json
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, 
                                QHBoxLayout, QSlider, QGroupBox, QRadioButton,
                                QButtonGroup, QProgressBar)
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import Qt

class Math_Title(QWidget):
    def __init__(self, main_ui):
        super().__init__()

        self.verticalLayout = QVBoxLayout()

        self.math_title = QLabel()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.math_title.sizePolicy().hasHeightForWidth())
        self.math_title.setSizePolicy(sizePolicy)
        big_font = QFont()
        big_font.setPointSize(72)
        big_font.setBold(True)
        big_font.setFamily("TH-Chara")
        big_font.setWeight(75)
        self.math_title.setFont(big_font)
        self.math_title.setAlignment(Qt.AlignCenter)
        self.math_title.setText("ฝึกคำนวนชวนคิด")
        self.verticalLayout.addWidget(self.math_title)

        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(36)

        self.math_lateststatisitc = QLabel()
        self.math_lateststatisitc.setAlignment(Qt.AlignCenter)
        self.math_lateststatisitc.setFont(font)
        self.math_lateststatisitc.setText("การเล่นล่าสุด\n \n ")
        self.verticalLayout.addWidget(self.math_lateststatisitc)

        self.horizontalLayout = QHBoxLayout()

        self.math_difficulty = QLabel()
        self.math_difficulty.setFont(font)
        self.math_difficulty.setText("ระดับความยาก")
        self.horizontalLayout.addWidget(self.math_difficulty)
        
        self.math_difficultyNumber = QLabel()
        self.math_difficultyNumber.setFont(font)
        self.math_difficultyNumber.setText("1")
        self.horizontalLayout.addWidget(self.math_difficultyNumber)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.math_difficultySlider = QSlider()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.math_difficultySlider.sizePolicy().hasHeightForWidth())
        self.math_difficultySlider.setSizePolicy(sizePolicy)
        self.math_difficultySlider.setStyleSheet("QSlider::groove:horizontal { \n"
"    background-color: black;\n"
"    border: 1px solid #424242; \n"
"    height: 100px; \n"
"    border-radius: 4px;\n"
"    margin: 2px 0}\n"
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
        self.math_difficultySlider.setMaximum(4)
        self.math_difficultySlider.setOrientation(Qt.Horizontal)
        self.verticalLayout.addWidget(self.math_difficultySlider)

        # self.verticalLayout.addLayout(self.verticalLayout_15)

        big_font = QFont()
        big_font.setFamily("TH-Chara")
        big_font.setPointSize(72)

        self.math_startButton = QPushButton()
        self.math_startButton.setFont(big_font)
        self.math_startButton.setStyleSheet("QPushButton {\n"
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
        self.math_startButton.setAutoDefault(True)
        self.math_startButton.setText("เริ่ม")
        self.verticalLayout.addWidget(self.math_startButton)

        self.math_backButton = QPushButton()
        self.math_backButton.setFont(font)
        self.math_backButton.setStyleSheet("QPushButton {\n"
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
        self.math_backButton.setAutoDefault(True)
        self.math_backButton.setText("กลับหน้าเลือกเกม")
        self.verticalLayout.addWidget(self.math_backButton)

        self.setLayout(self.verticalLayout)

        self.main_ui = main_ui
        self.difficulty = 0
        # self.difficulty = self.main_ui.user['math_game']['reccommend_difficulty']
        self.changeDifficulty()
        self.connectEvent()


    def connectEvent(self):
        self.math_difficultySlider.valueChanged.connect(self.changeDifficulty)
        self.math_startButton.clicked.connect(self.toMathPlay)
        self.math_backButton.clicked.connect(self.toGamePage)


    def changePage(self, index):
        self.main_ui.changePage(index)

    def toGamePage(self):
        self.changePage(2)

    def toMathPlay(self):
        mathPlay_ui = self.main_ui.stackedWidget.widget(4)
        mathPlay_ui.startQuiz(self.difficulty)
        self.changePage(4)

    def changeDifficulty(self):
        difficulty = self.math_difficultySlider.value()
        if difficulty == 0:
            self.math_difficultyNumber.setText("บวก ลบ ไม่เกิน 9")
        elif difficulty == 1:
            self.math_difficultyNumber.setText("บวก ลบ ไม่เกิน 9 มี 2 ขั้นตอน")
        elif difficulty == 2:
            self.math_difficultyNumber.setText("บวก ลบ ไม่เกิน 20")
        elif difficulty == 3:
            self.math_difficultyNumber.setText("บวก ลบ ไม่เกิน 20 มี 2 ขั้นตอน")
        else:
            self.math_difficultyNumber.setText("บวก ลบ ไม่เกิน 20 มี 2 ขั้นตอน และคูณ")
        self.difficulty = difficulty

    def setDifficulty(self, difficulty):
        self.math_difficultySlider.setValue(difficulty)

class Math_Play(QWidget):
    def __init__(self, main_ui):
        super().__init__()

        self.verticalLayout = QVBoxLayout()

        # self.math_progressBar = QProgressBar()
        # self.math_progressBar.setProperty("value", 24)
        # self.math_progressBar.setTextVisible(True)
        # self.math_progressBar.setInvertedAppearance(False)
        # self.verticalLayout.addWidget(self.math_progressBar)

        self.math_questionLayout = QHBoxLayout()

        self.math_questionLayout.addStretch()

        self.math_question = QLabel()
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.math_question.setFont(font)
        self.math_question.setText("33 + 55 = ")
        self.math_questionLayout.addWidget(self.math_question)

        self.math_ans_lineEdit = QLineEdit()
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(72)
        self.math_ans_lineEdit.setFont(font)
        self.math_ans_lineEdit.setPlaceholderText("ใส่คำตอบที่นี่ได้นะ")
        self.onlyInt = QIntValidator()
        self.math_ans_lineEdit.setValidator(self.onlyInt)
        self.math_questionLayout.addWidget(self.math_ans_lineEdit)

        self.math_questionLayout.addStretch()

        self.verticalLayout.addLayout(self.math_questionLayout)

        self.math_choiceGroup = QGroupBox()
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.math_choiceGroup.setFont(font)
        self.math_choiceGroup.setTitle("ตัวเลือกไหนนะเป็นคำตอบที่ถูก")
        
        self.choice_layout = QVBoxLayout()

        self.math_choice1 = QRadioButton()
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.math_choice1.setFont(font)
        self.math_choice1.setStyleSheet("QRadioButton::indicator{width: 50px; height: 50px;}")
        self.math_choice1.setText("1")
        self.math_choiceButtonGroup = QButtonGroup()
        self.math_choiceButtonGroup.addButton(self.math_choice1)
        self.choice_layout.addWidget(self.math_choice1)

        self.math_choice2 = QRadioButton()
        self.math_choice2.setStyleSheet("QRadioButton::indicator{width: 50px; height: 50px;}")
        self.math_choice2.setFont(font)
        self.math_choiceButtonGroup.addButton(self.math_choice2)
        self.math_choice2.setText("2")
        self.choice_layout.addWidget(self.math_choice2)

        self.math_choice3 = QRadioButton()
        self.math_choice3.setStyleSheet("QRadioButton::indicator{width: 50px; height: 50px;}")
        self.math_choice3.setFont(font)
        self.math_choiceButtonGroup.addButton(self.math_choice3)
        self.math_choice3.setText("3")
        self.choice_layout.addWidget(self.math_choice3)

        self.math_choiceGroup.setLayout(self.choice_layout)

        self.verticalLayout.addWidget(self.math_choiceGroup)

        self.math_playButton = QHBoxLayout()
        self.math_previousButton = QPushButton()
        self.math_previousButton.setEnabled(False)
        font = QFont()
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("TH-Chara")
        self.math_previousButton.setFont(font)
        self.math_previousButton.setStyleSheet("QPushButton {\n"
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
        self.math_previousButton.setAutoDefault(True)
        self.math_previousButton.setText("ข้อก่อนหน้า")
        self.math_playButton.addWidget(self.math_previousButton)

        self.math_nextButton = QPushButton()
        self.math_nextButton.setEnabled(False)
        font = QFont()
        font.setFamily("TH-Chara")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.math_nextButton.setFont(font)
        self.math_nextButton.setStyleSheet("QPushButton {\n"
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
        self.math_nextButton.setAutoDefault(True)
        self.math_nextButton.setText("ข้อถัดไป")
        self.math_playButton.addWidget(self.math_nextButton)

        self.verticalLayout.addLayout(self.math_playButton)

        self.setLayout(self.verticalLayout)

        self.main_ui = main_ui
        self.arithmetic = None
        self.question_number = 0
        self.answer = None
        self.score = None
        self.time_start = None
        self.connectEvent()


    def connectEvent(self):
        self.math_ans_lineEdit.textChanged.connect(self.text_answer)
        self.math_ans_lineEdit.returnPressed.connect(self.nextQuestion)
        self.math_choiceButtonGroup.buttonClicked.connect(self.radio_on_click)
        self.math_nextButton.clicked.connect(self.nextQuestion)
        self.math_previousButton.clicked.connect(self.previousQuestion)


    def changePage(self, index):
        self.main_ui.changePage(index)

    def toMathTitle(self):
        self.changePage(3)

    def startQuiz(self,difficulty):
        self.arithmetic = Arithmetic(25)
        self.arithmetic.createQuiz(difficulty)
        self.question_number = 0
        self.answer = []
        self.score = 0
        self.time_start = datetime.now()
        self.display_question()
        self.display_options()

    def display_question(self):
        self.math_question.setText(self.arithmetic.question[self.question_number])

    def display_options(self):            
        self.math_choice1.setText(str(self.arithmetic.options[self.question_number][0]))
        self.math_choice2.setText(str(self.arithmetic.options[self.question_number][1]))
        self.math_choice3.setText(str(self.arithmetic.options[self.question_number][2]))

    def reset_answered(self):
        self.math_nextButton.setEnabled(False)
        self.math_choiceButtonGroup.setExclusive(False)
        self.math_choice1.setChecked(False)
        self.math_choice2.setChecked(False)
        self.math_choice3.setChecked(False)
        self.math_choiceButtonGroup.setExclusive(True)
        self.math_ans_lineEdit.setEnabled(True)
        self.math_ans_lineEdit.setText("")

    def nextQuestion(self):
        if self.math_choiceButtonGroup.checkedButton():
            answer = int(self.math_choiceButtonGroup.checkedButton().text())
        else:
            answer = int(self.math_ans_lineEdit.text())
        self.answer.append(answer)

        self.question_number += 1
        if(self.question_number + 1 > len(self.arithmetic.question)):
            time_played = datetime.now() - self.time_start
            time_played = int(time_played.total_seconds())
            
            for a,r in zip(self.arithmetic.answer,self.answer):
                    if a == r:
                        self.score += 1

            # score multiplier
            score_multiplier = 1
            if time_played <= 300:
                score_multiplier = 5
            elif time_played <= 420:
                score_multiplier = 3
            elif time_played <= 540:
                score_multiplier = 2
            elif time_played <= 600:
                score_multiplier = 1
            mathTitle_ui = self.main_ui.stackedWidget.widget(3)
            time_played_minute = int(time_played / 60)
            time_played_second = int(time_played % 60)
            score_accuracy = (self.score / self.arithmetic.numberOfQuestion) * 100
            score_after_bonus = self.score * score_multiplier
            cheering_word = ""
            max_score = self.arithmetic.numberOfQuestion * 5
            if score_after_bonus == max_score:
                cheering_word = "พ่อๆแม่ๆทำได้ดีแล้วพยายามทำแบบฝึกเป็นประจำด้วยนะ"
            elif score_after_bonus >= max_score * 0.8:
                cheering_word = "พ่อๆแม่ๆยังพลาดไปบ้าง แต่ก็ทำได้ดีมากแล้วนะ"
            elif score_after_bonus >= max_score * 0.6:
                cheering_word = "พ่อๆแม่ๆยังช้าไปบ้าง แต่ก็ทำได้ดีมากแล้วนะ"
            elif score_after_bonus >= max_score * 0.4:
                cheering_word = "พ่อๆแม่ๆยังพลาดไปบ้างไม่ก็ข้าไป แต่ก็ทำได้ดีมากแล้วนะ"
            elif score_after_bonus >= 0:
                cheering_word = "พ่อๆแม่ๆทำได้ดีแล้ว ค่อยๆทำให้ถูกต้องด้วยนะ"
            result_text = "การเล่นล่าสุด\nถูก {5} ข้อ ใช้เวลา {0} นาที {1} วินาที (คะแนนคูณ {2})\nได้ {3} คะแนน ({4})".format(time_played_minute, time_played_second, score_multiplier, score_after_bonus, cheering_word, self.score)
            mathTitle_ui.math_lateststatisitc.setText(result_text)
            # savefile
            record_stat = {
                            "date":self.time_start.isoformat(),
                                "time":time_played,
                                "accuracy":score_accuracy,
                                "score":score_after_bonus,
                            "difficulty":mathTitle_ui.difficulty
                        }
            # print(record_stat)
            user = self.main_ui.user
            user['math_game']['play_history'].append(record_stat)
            # change difficulty
            if len(user['math_game']['play_history']) % 5 == 0:
                user['word_memory_game']['recommend_difficulty'] += 1
            if (user['word_memory_game']['recommend_difficulty'] > 4):
                user['word_memory_game']['recommend_difficulty'] = 4
            save_data = user.copy()
            file_path = save_data.pop('filename')
            with open(file_path, "w") as outfile:
                json.dump(save_data, outfile, ensure_ascii=False)
            self.math_previousButton.setEnabled(False)
            self.math_nextButton.setText("ข้อถัดไป")
            self.toMathTitle()
        else:
            if(self.question_number + 1 == len(self.arithmetic.question)):
                self.math_nextButton.setText("ส่งคำตอบ")
            if(self.question_number > 0):
                self.math_previousButton.setEnabled(True)
            self.display_question()
            self.display_options()
        self.reset_answered()
        
    def previousQuestion(self):
        self.answer.pop()

        self.question_number -= 1
        if(self.question_number == 0):
                self.math_previousButton.setEnabled(False)
        if(self.question_number + 1 < len(self.arithmetic.question)):
                self.math_nextButton.setText("ข้อถัดไป")
        self.display_question()
        self.display_options()
        self.reset_answered()

    def radio_on_click(self):
        self.math_nextButton.setEnabled(True)
        self.math_ans_lineEdit.setEnabled(False)
    
    def text_answer(self):
        if self.math_ans_lineEdit.text() not in ["",None]: 
            self.math_nextButton.setEnabled(True)
            self.math_choiceButtonGroup.setExclusive(False)
            self.math_choice1.setChecked(False)
            self.math_choice2.setChecked(False)
            self.math_choice3.setChecked(False)
            self.math_choiceButtonGroup.setExclusive(True)
        else:
            self.math_nextButton.setEnabled(False)

from random import randint, choice, shuffle

class Arithmetic:
    def __init__(self,numberOfQuestion):
        self.question = []
        self.answer = []
        self.options = []
        self.numberOfQuestion = numberOfQuestion

    def createQuiz(self,difficulty):
        if difficulty == 0:
            for i in range(0,self.numberOfQuestion):
                ops = ['+','-']
                ops = choice(ops)
                max = 9
                num = []
                num.append(randint(0,max))
                if ops == '+': 
                    num.append(self.randomNextAddition(max,num[-1]))
                else:
                    num.append(self.randomNextSubtraction(num[-1]))
                self.question.append(self.createQuestion(num,ops))
                ans =self.calculateAnswer(num,ops)
                self.answer.append(ans)
                self.options.append(self.createOptions(max,ans))
            
        elif difficulty == 1:
            for i in range(0,self.numberOfQuestion):
                ops = ['++','+-','-+','--']
                ops = choice(ops)
                max = 9
                num = []
                num.append(randint(0,max))
                if ops == '++': 
                    num.append(self.randomNextAddition(max,num[-1]))
                    num.append(self.randomNextAddition(max,num[-1]+num[-2]))
                elif ops == '+-':
                    num.append(self.randomNextAddition(max,num[-1]))
                    num.append(self.randomNextSubtraction(num[-1]+num[-2]))
                elif ops == '-+':
                    num.append(self.randomNextSubtraction(num[-1]))
                    num.append(self.randomNextAddition(max,num[-2]-num[-1]))
                else:
                    num.append(self.randomNextSubtraction(num[-1]))
                    num.append(self.randomNextSubtraction(num[-2]-num[-1]))
                self.question.append(self.createQuestion(num,ops))
                ans =self.calculateAnswer(num,ops)
                self.answer.append(ans)
                self.options.append(self.createOptions(max,ans))

        elif difficulty == 2:
            for i in range(0,self.numberOfQuestion):
                ops = ['+','-']
                ops = choice(ops)
                max = 20
                num = []
                num.append(randint(0,max))
                if ops == '+': 
                    num.append(self.randomNextAddition(max,num[-1]))
                else:
                    num.append(self.randomNextSubtraction(num[-1]))
                self.question.append(self.createQuestion(num,ops))
                ans =self.calculateAnswer(num,ops)
                self.answer.append(ans)
                self.options.append(self.createOptions(max,ans))
            
        elif difficulty == 3:
            for i in range(0,self.numberOfQuestion):
                ops = ['++','+-','-+','--']
                ops = choice(ops)
                max = 20
                num = []
                num.append(randint(0,max))
                if ops == '++': 
                    num.append(self.randomNextAddition(max,num[-1]))
                    num.append(self.randomNextAddition(max,num[-1]+num[-2]))
                elif ops == '+-':
                    num.append(self.randomNextAddition(max,num[-1]))
                    num.append(self.randomNextSubtraction(num[-1]+num[-2]))
                elif ops == '-+':
                    num.append(self.randomNextSubtraction(num[-1]))
                    num.append(self.randomNextAddition(max,num[-2]-num[-1]))
                else:
                    num.append(self.randomNextSubtraction(num[-1]))
                    num.append(self.randomNextSubtraction(num[-1]))
                self.question.append(self.createQuestion(num,ops))
                ans =self.calculateAnswer(num,ops)
                self.answer.append(ans)
                self.options.append(self.createOptions(max,ans))
        
        else:
            for i in range(0,self.numberOfQuestion):
                ops = ['+','-','+','-','++','+-','-+','--','x']
                ops = choice(ops)
                if ops not in ['x']:
                    max = 20
                    num = []
                    num.append(randint(0,max))
                    if ops == '+': 
                        num.append(self.randomNextAddition(max,num[-1]))
                    elif ops == '-' :
                        num.append(self.randomNextSubtraction(num[-1]))
                    elif ops == '++': 
                        num.append(self.randomNextAddition(max,num[-1]))
                        num.append(self.randomNextAddition(max,num[-1]+num[-2]))
                    elif ops == '+-':
                        num.append(self.randomNextAddition(max,num[-1]))
                        num.append(self.randomNextSubtraction(num[-1]+num[-2]))
                    elif ops == '-+':
                        num.append(self.randomNextSubtraction(num[-1]))
                        num.append(self.randomNextAddition(max,num[-2]-num[-1]))
                    else: # if ops == '--'
                        num.append(self.randomNextSubtraction(num[-1]))
                        num.append(self.randomNextSubtraction(num[-2]-num[-1]))
                else: # if ops == 'x'
                    max = 9
                    num = []
                    num.append(randint(1,max))
                    num.append(randint(1,max))
                self.question.append(self.createQuestion(num,ops))
                ans=self.calculateAnswer(num,ops)
                self.answer.append(ans)
                self.options.append(self.createOptions(max,ans,ops,num))

    def randomNextAddition(self,max,num):
        num = randint(0,max-num)
        return num
    
    def randomNextSubtraction(self,num):
        num = randint(0,num)
        return num
        
    def createQuestion(self,num,ops):
        # print(num,ops)
        question = str(num[0])
        for o in range(0,len(ops)):
            question += ' ' + ops[o] + ' ' + str(num[o+1])
        question += ' = '
        # print(question)
        return question

    def calculateAnswer(self,num,ops):
        if ops not in ['x']:
            ans = num[0]
            for o in range(0,len(ops)):
                if ops[o] == '+':
                    ans += num[o+1]
                else:
                    ans -= num[o+1]
        else:
            ans = num[0] * num[1]
        return ans
        
    def createOptions(self,max,ans,ops = '+',num= []):
        if ops != 'x':
            options = [ans]
            while len(options) < 3:
                o = choice(list(set([x for x in range(0, max)]) - set(options)))
                options.append(o)
            shuffle(options)
            return options
        # if ops == 'x' 
        options = []
        numCof = [num[1]]
        while len(numCof) < 3:
            o = choice(list(set([x for x in range(0, max)]) - set(numCof)))
            numCof.append(o)
        shuffle(numCof)
        # print(numCof)
        options = [n * num[0] for n in numCof]
        return options
