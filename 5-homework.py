# 1
# name = input("Ismingizni kiriting: ")
# age = input("Yoshingizni kiriting: ")
# def display_person_information (name, age):
#     print(f"Salom {name}")
#     print(f"Sizning yoshingiz {age}da")
#
# display_person_information(name, age)
#
# 2
# def even_number (n=20):
#     list = []
#
#     for i in range(1, n):
#         if i%2==0:
#             number = i
#             list.append(number)
#         else: n=20
#     return list
#
# print(even_number())

# 3
# def ears_count (legs):
#     if legs%4>0:
#         print("Qo'ylarning jami quloqlari soni: -1")
#     else:
#         print(f"Qo'ylarning jami quloqlari soni: {round(legs/2, 0)}")
#
# legs = int(input("Qo'ylarning jami oyoqlari sonini kiriting: "))
# print(ears_count(legs))

# 4 #2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022
# def kabisa_checker (years):
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
# kabisa_checker(years=input("Yillarni vergul orqali kiriting: "))
#
# 5
# def season(month):
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
#
# season(month = int(input("Oyni kiriting: "))-1)

# 6
# def replace_tuple_with_index(my_tuple, old, new):
#     my_tuple=(13,'python', 26, 'c++', 89, 56, 'java', 23, 47, 'c#', 78)
#
#     # old = input("Almshtirilishi kerak bo'lgan elementni kiriting: ")
#     # new = input("Qanday ma'lumot joylashtiramiz: ")
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
# print("Yakuniy natija: ", replace_tuple_with_index(my_tuple,old = input("Almshtirilishi kerak bo'lgan elementni kiriting: "), new = input("Qanday ma'lumot joylashtiramiz: ") ))

# 7
# lst=[]
# for i in range(1,4):
#     number=int(input(f"{i}-raqam: "))
#     lst.append(number)
#
# def average(lst):
#     return sum(lst) / len(lst)
#
# print(average(lst))

# 8 #python c++ java c# javascript
# def string_to_list(my_list):
#     my_list = my_list.split()
#     print(my_list)
#     my_list.reverse()
#     return my_list
#
# my_list=input("Listni kiriting: ")
# print(string_to_list(my_list))

# 9
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Parol generatorga xush kelibsiz!")
# count_letters= int(input("Parolda nechta harf bo'lishini xoxlaysiz: "))
# count_symbols = int(input(f"Parolda nechta belgi bo'lishini xoxlaysiz: "))
# count_numbers = int(input(f"Parolda nechta son bo'lishini xoxlaysiz: "))
# password=[]
# if count_letters>0:
#     for element in range(0, count_letters):
#         password.append(random.choice(letters))
# if count_symbols>0:
#     for element in range(0, count_symbols):
#         password.append(random.choice(symbols))
# if count_numbers>0:
#     for element in range(0, count_numbers):
#         password.append(random.choice(numbers))
# print("".join(password))
