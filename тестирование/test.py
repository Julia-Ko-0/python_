import json
# открытие файла с вопросами и ответами
with open("C:/Users/MSI/Desktop/phyton/тестирование/questions.txt", "r") as file:
    data = json.load(file)
# получение списка вопросов
questions = data["questions"]
# инициализация переменной для подсчета правильных ответо
score = 0
# проход по каждому вопросу
for i in range(len(questions)):
    # вывод вопроса на экран
    print(f"Вопрос {i + 1}. {questions[i]['question']}")
    
    # вывод каждого варианта ответа на экран
    for j, answer in enumerate(questions[i]['answers']):
        print(f"{j + 1}. {answer}")
    
    # получение ответа от пользователя
    user_answer = input("Введите номер правильного ответа и нажмите Enter: ")
    
    # проверка ответа
    if user_answer == questions[i]['correct_answer']:
        score += 1

print(f"Вы набрали {score} из {len(questions)} возможных баллов.")
if(score/(len(questions)) == 1):
    print("Оценка",5 )
if(2/3<score/(len(questions))<1 ):
    print("Оценка",4 )
if(1/2<=score/(len(questions))<2/3):
    print("Оценка",3)
if(score/(len(questions))<1/2):
    print("Оценка",2)