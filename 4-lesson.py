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
#
# import random
# alphabet = [chr(i) for i in range(97, 123)] #harflar
# numbers = [str(i) for i in range(10)] #sonlar
# symbols = ["!", "@", "#", "$","%"]
#
# count_of_password = int(input("Parol necha xonadan iborat?: "))
# password=[]
# full_list=[]
# is_letters = input("Harflar qatnashsinmi? y/n")
# is_digits = input("Sonlar qatnashsinmi? y/n")
# is_symbols = input("Belgilar qatnashsinmi? y/n")
# if is_letters=="y":
#     full_list.append(alphabet)
# if is_digits=="y":
#     full_list.append(numbers)
# if is_symbols=="y":
#     full_list.append(symbols)
#
# for element in range (0, count_of_password):
#     password.append(random.choice(full_list))
# print("".join(password))