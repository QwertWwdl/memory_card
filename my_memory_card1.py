#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton,QHBoxLayout, QLabel,QVBoxLayout,QMessageBox,QRadioButton,QGroupBox
from random import *

app = QApplication([])
main_win = QWidget()

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
btn_OK = QPushButton('Ответить')

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

main_Layout = QVBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

main_Layout.addWidget(question,alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_1,alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_2,alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_3,alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_4,alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

main_Layout.addWidget(RadioGroupBox)
main_Layout.addWidget(AnsGroupBox)
RadioGroupBox.setLayout(layout_ans1)
main_Layout.addLayout(layout_ans1)
main_Layout.addWidget(btn_OK)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_answer():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_answer()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Верно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:',main_win.total,'\n-Правильных ответов:',main_win.score)
        print('Рейтинг:',(main_win.score/main_win.total*100),'%')
    elif answers[1].isChecked():
        show_correct('Неверно.')
    elif answers[2].isChecked():
        show_correct('Неверно.')
    elif answers[3].isChecked():
        show_correct('Неверно.')
def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов:',main_win.total,'\n-Правильных ответов:',main_win.score)
    cur_question = randint(0,len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
btn_OK.clicked.connect(click_OK)
main_win.total = 0
main_win.score = 0

questions_list = []
questions_list.append(Question('Государственный язык Португалии?','Португальский','Испанский','Английский','Французский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов?', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Столица Франции?','Париж','Москва','Лондон','Нью-Йорк'))
questions_list.append(Question('Кто написал роман «Война и мир»?','Л. Толстой','А. Чехов','А.Пушкин','Ф. Достоевский'))
questions_list.append(Question('Самый глубокий океан в мире?','Тихий','Атлантический','Южный','Индийский'))
questions_list.append(Question('Самая большая планета в Солнечной системе?','Юпитер','Марс','Сатурн','Земля'))
questions_list.append(Question('Какой элемент таблицы Менделеева обозначается символом «Fe»?','Железо','Азот','Медь','Литий'))
questions_list.append(Question('Какое животное является символом Австралии?','Кенгуру','Панда','Слон','Лев'))
questions_list.append(Question('Сколько будет 7 в кубе?','343','49','14','3000'))
questions_list.append(Question('Какой музыкальный инструмент имеет 88 клавиш?','Фортепиано','Гитара','Виолончель','Флейта'))
questions_list.append(Question('Какой элемент является самым распространенным во Вселенной?','Водород','Кислород','Углерод','Азот'))
questions_list.append(Question('Автор картины «Мона Лиза?»','Леонардо да Винчи','Пабло Пикассо','Клод Моне','Винсент Ван Гог'))
questions_list.append(Question('Самый маленький континент по площади?','Австралия','Европа','Южная Америка','Антарктида'))
questions_list.append(Question('Какой газ составляет 78% атмосферы Земли?','Азот','Кислород','Углекислый газ','Воздух'))
next_question()
main_win.setLayout(main_Layout)
main_win.show()
app.exec_()