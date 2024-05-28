# def password_checker (count_password):
#     if count_password>=8:
#         print("Parol talabga javob beradi")
#     else:
#         print("Parol 8ta belgidan ko'p bo'lishi kerak!")

# from Utils import my_calculator
#
# my_calculator()

def oylikni_hisoblash(dars_soati, narxi):
    return dars_soati*narxi

asosiy_maosh = oylikni_hisoblash(12, 300_000)
qushimcha_maosh = oylikni_hisoblash(5, 400_000)
maosh = asosiy_maosh+qushimcha_maosh
print(maosh)

# count_oh_question = int(input("Nechta savol kiritamiz: "))
# questions = []
# for question in range(1, count_oh_question+1):
#     question_text = input(f"Savolni kiriting: ")
#     current_question = {
#         'question_text': question_text,
#         'answers':{},
#         'true_answer':''
#     }
#     for answer in ['a', 'b', 'c']:
#         answer_text = input(f"{answer}:")
#         current_question['answers'][answer] = answer_text
#     current_question['true_answer'] = input("To'g'ri javobni tanlang: ")
#     questions.append(current_question)
# print(current_question)




# my_calculator(5,3)
# my_calculator(7,8)
# my_calculator(7,12)
