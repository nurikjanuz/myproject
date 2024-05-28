# 1
#args
# def display_person_information (*args):
#     name, age = args
#     print(f"Salom {name}")
#     print(f"Sizning yoshingiz {age}da")
#
# name = input("Ismingizni kiriting:")
# age = input("Yoshingizni kiriting: ")
#
# print(display_person_information(name, age))
#kwargs
# def display_person_information (**kwargs):
#     print(f"Salom {kwargs['name']}")
#     print(f"Sizning yoshingiz {kwargs['age']}da")
#
# print(display_person_information(name = input("Ismingizni kiriting:"), age = input("Yoshingizni kiriting: ")))
# #
# 2
#args
# def even_number(*args):
#     start, end = args
#     start = 1
#     return [arg for arg in range(start, end) if arg % 2 == 0]
#
# print(even_number(1, int(input("n raqamini kiriting: "))))
#kwargs
# def even_number(**kwargs):
#     kwargs['start'] = 1
#     return [arg for arg in range(kwargs['start'], kwargs['end']) if arg % 2 == 0]
#
# print(even_number(start=1, end=int(input("n raqamini kiriting: "))))

# 3
#args
# def ears_count (*args):
#     start, legs =args
#     if legs%4>0:
#         print("Qo'ylarning jami quloqlari soni: -1")
#     else:
#         print(f"Qo'ylarning jami quloqlari soni: {round(legs/2, 0)}")
#
# legs = int(input("Qo'ylarning jami oyoqlari sonini kiriting: "))
# print(ears_count(1, legs))

# #kwargs
# def ears_count (**kwargs):
#     if kwargs['legs']%4>0:
#         print("Qo'ylarning jami quloqlari soni: -1")
#     else:
#         print(f"Qo'ylarning jami quloqlari soni: {round(kwargs['legs']/2, 0)}")
#
#
# print(ears_count(legs = int(input("Qo'ylarning jami oyoqlari sonini kiriting: "))))

# 4 #2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022
#args
# def kabisa_checker (*args):
#     x, years = args
#     years = years.split(",")
#     count_of_years = 0
#     for i in years:
#         count_of_years += 1
#     print(f"{count_of_years}ta yil qabul qilindi!")
#     for year in years:
#         if int(year) % 400 == 0:
#             print(f"{year} - kabisa yili")
#         elif int(year) % 4 == 0 and int(year)%100 != 0:
#             print(f"{year} - kabisa yili")
#         else:
#             print(f"{year} - kabisa yili emas")
#
# years=input("Yillarni vergul orqali kiriting: ")
# kabisa_checker(0, years)

#kwargs
# def kabisa_checker (**kwargs):
#     kwargs['years'] = kwargs['years'].split(",")
#     count_of_years = 0
#     for i in kwargs['years']:
#         count_of_years += 1
#     print(f"{count_of_years}ta yil qabul qilindi!")
#     for year in kwargs['years']:
#         if int(year) % 400 == 0:
#             print(f"{year} - kabisa yili")
#         elif int(year) % 4 == 0 and int(year)%100 != 0:
#             print(f"{year} - kabisa yili")
#         else:
#             print(f"{year} - kabisa yili emas")
# kabisa_checker(years=input("Yillarni vergul orqali kiriting: "))

# 5
#args
# def season(*args):
#     n, month = args
#     months = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May','Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr' ]
#     if month in range(0, len(months)):
#         if 3<=month<=5:
#             print(f"{months[month]} oyi Bahor fasliga kiradi")
#         elif 6<=month<=8:
#             print(f"{months[month]} oyi Yoz fasliga kiradi")
#         elif 9<=month<=11:
#             print(f"{months[month]} oyi Kuz fasliga kiradi")
#         else:
#             print(f"{months[month]} oyi Qish fasliga kiradi")
#     else:
#         print("Bunday oy mavjud emas!")
# month = int(input("Oyni kiriting: "))-1
# season(0, month)

#kwargs
# def season(**kwargs):
#     months = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May','Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr' ]
#     if kwargs['month'] in range(0, len(months)):
#         if 3<=kwargs['month']<=5:
#             print(f"{months[kwargs['month']]} oyi Bahor fasliga kiradi")
#         elif 6<=kwargs['month']<=8:
#             print(f"{months[kwargs['month']]} oyi Yoz fasliga kiradi")
#         elif 9<=kwargs['month']<=11:
#             print(f"{months[kwargs['month']]} oyi Kuz fasliga kiradi")
#         else:
#             print(f"{months[kwargs['month']]} oyi Qish fasliga kiradi")
#     else:
#         print("Bunday oy mavjud emas!")
#
# season(month= int(input("Oyni kiriting: "))-1)

# 6
#args
# def replace_tuple_with_index(*args):
#     my_tuple, old, new =args
#     my_tuple = list(my_tuple)
#     new_tuple=()
#     if old in my_tuple:
#         i = my_tuple.index(old)
#         my_tuple[i]=new
#
#     elif int(old) in my_tuple:
#         i = my_tuple.index(int(old))
#         my_tuple[i]=int(new)
#     my_tuple=tuple(my_tuple)
#     return my_tuple
#
# my_tuple=(13,'python', 26, 'c++', 89, 56, 'java', 23, 47, 'c#', 78)
# print("Boshlang'ich tuple:", my_tuple)
# old = input("Almshtirilishi kerak bo'lgan elementni kiriting: ")
# new = input("Qanday ma'lumot joylashtiramiz: ")
# print("Yakuniy natija: ", replace_tuple_with_index(my_tuple,old,new ))

#kwargs
# def replace_tuple_with_index(**kwargs):
#
#     kwargs['my_tuple'] = list(kwargs['my_tuple'])
#     new_tuple=()
#     if kwargs['old'] in kwargs['my_tuple']:
#         i = kwargs['my_tuple'].index(kwargs['old'])
#         kwargs['my_tuple'][i]=kwargs['new']
#
#     elif int(kwargs['old']) in kwargs['my_tuple']:
#         i = kwargs['my_tuple'].index(int(kwargs['old']))
#         kwargs['my_tuple'][i]=int(kwargs['new'])
#     kwargs['my_tuple']=tuple(kwargs['my_tuple'])
#     return kwargs['my_tuple']
#
# print("Boshlang'ich tuple:(13,'python', 26, 'c++', 89, 56, 'java', 23, 47, 'c#', 78)")
# print("Yakuniy natija: ", replace_tuple_with_index(my_tuple=(13,'python', 26, 'c++', 89, 56, 'java', 23, 47, 'c#', 78), old = input("Almshtirilishi kerak bo'lgan elementni kiriting: "),
# new = input("Qanday ma'lumot joylashtiramiz: ") ))

# 7
#args
# lst=[]
# for i in range(1,4):
#     number=int(input(f"{i}-raqam: "))
#     lst.append(number)
#
# def average(*args):
#     x, lst=args
#     return sum(lst) / len(lst)
#
# print(average(0, lst))

#kwargs
# lst=[]
# for i in range(1,4):
#     number=int(input(f"{i}-raqam: "))
#     lst.append(number)
#
# def average(**kwargs):
#     return sum(kwargs['lst']) / len(kwargs['lst'])
#
# print(average(lst = lst))

# 8 #python c++ java c# javascript
#args
# def string_to_list(*args):
#     x, my_list = args
#     my_list = my_list.split()
#     print(my_list)
#     my_list.reverse()
#     return my_list
#
# my_list=input("Listni kiriting: ")
# print(string_to_list(0, my_list))

#kwargs
# def string_to_list(**kwargs):
#     kwargs['my_list'] = kwargs['my_list'].split()
#     print(kwargs['my_list'])
#     kwargs['my_list'].reverse()
#     return kwargs['my_list']
#
# print(string_to_list(my_list=input("Listni kiriting: ")))

# 9
#args
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Parol generatorga xush kelibsiz!")
#
#
# def password_generator(*args):
#     count_letters, count_symbols, count_numbers = args
#     password = []
#     if count_letters>0:
#         for element in range(0, count_letters):
#             password.append(random.choice(letters))
#     if count_symbols>0:
#         for element in range(0, count_symbols):
#             password.append(random.choice(symbols))
#     if count_numbers>0:
#         for element in range(0, count_numbers):
#             password.append(random.choice(numbers))
#     return print("".join(password))
#
# count_letters= int(input("Parolda nechta harf bo'lishini xoxlaysiz: "))
# count_symbols = int(input(f"Parolda nechta belgi bo'lishini xoxlaysiz: "))
# count_numbers = int(input(f"Parolda nechta son bo'lishini xoxlaysiz: "))
#
# print(password_generator(count_letters, count_symbols, count_numbers))
#kwargs
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Parol generatorga xush kelibsiz!")
#
#
# def password_generator(**kwargs):
#     password = []
#     if kwargs['count_letters']>0:
#         for element in range(0, kwargs['count_letters']):
#             password.append(random.choice(letters))
#     if kwargs['count_symbols']>0:
#         for element in range(0, kwargs['count_symbols']):
#             password.append(random.choice(symbols))
#     if kwargs['count_numbers']>0:
#         for element in range(0, kwargs['count_numbers']):
#             password.append(random.choice(numbers))
#     return print("".join(password))
#
#
# print(password_generator(
#                     count_letters= int(input("Parolda nechta harf bo'lishini xoxlaysiz: ")),
#                     count_symbols = int(input(f"Parolda nechta belgi bo'lishini xoxlaysiz: ")),
#                     count_numbers = int(input(f"Parolda nechta son bo'lishini xoxlaysiz: "))
# ))