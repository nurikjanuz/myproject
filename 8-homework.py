import json

# with open('questions.json', 'w+') as file:
#     count_of_question = int(input("Nechta savol kiritamiz: "))
#     questions = []
#     for question in range(1, count_of_question+1):
#         question_text = input(f"Savolni kiriting: ")
#         current_question = {
#             'question_text': question_text,
#             'answers':{},
#             'true_answer':''
#         }
#         for answer in ['a', 'b', 'c']:
#             answer_text = input(f"{answer}:")
#             current_question['answers'][answer] = answer_text
#         current_question['true_answer'] = input("To'g'ri javobni tanlang: ")
#         questions.append(current_question)
#     questions_json = json.dumps(questions, indent=4)
#     file.write(questions_json)

# with open('questions.json', 'r+') as file:
#     questions = json.load(file)
#     print('Testni yechish')
#     count_of_correct_answers = 0
#     for question in questions:
#         print(f"Savol: {question['question_text']}")
#         for answer in question['answers'].items():
#             print(f"{answer[0]}) {answer[1]}")
#         user_answer = input('Javoni belgilang: ')
#         if question['true_answer'] == user_answer:
#             print("to'g'ri")
#             count_of_correct_answers+=1
#         else:
#             print("noto'g'ri")
#
#     with open('answers.json', 'w+') as file2:
#         answers_json = json.dumps(count_of_correct_answers)
#         file2.write(answers_json)
# import os
# cancl = input("Savollarni o'chirib tashlash uchun d tugmasini bosing: ")
# if cancl =='d':
#     os.remove('questions.json')
#     os.remove('answers.json')






# [
#     {
#         "question_text": "Poytaxt",
#         "answers": {
#             "a": "Toshkent",
#             "b": "Samarqand",
#             "c": "Buxoro"
#         },
#         "true_answer": "a"
#     },
#     {
#         "question_text": "Yil",
#         "answers": {
#             "a": "1992",
#             "b": "1991",
#             "c": "1993"
#         },
#         "true_answer": "b"
#     }
# ]