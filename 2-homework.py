# 1
# temperature = int(input("Bugungi havo haroratini Celcius o'lchovida kiriting: "))
# if temperature > 40:
#     print("Bu juda issiq kun")
# elif 25<temperature <40:
#     print("Bu issiq kun")
# elif temperature==25:
#     print("Bu ajoyib kun")
# elif 10<=temperature<25:
#     print("Bu salqin kun")
# else:
#     print("Bu sovuq kun")

# 2
# name = input("Ismingizni kiriting: ")
# check_name = len(name)
# if check_name <3:
#     print("Ism 3ta belgidan kam bo'lishi mumkin emas!")
# elif check_name > 13:
#     print("Ism 13ta belgidan ko'p bo'lishi mumkin emas!")

# 3
# lang = input("Iltimos tilni tanlang / Пожалуйста, выберите язык: (o'zbek / rus): ")
# if lang == "o'zbek":
#     print("Assalomu alaykum! Siz o'zbek tilini tanladingiz")
# elif lang == "rus":
#     print("Здравствуйте, вы выбрали русский язык")
# else:
#     print("To'g'ri tilni tanlang / Выберите правильный язык")

# 4
# books = int(input("Jamshid nechta kitob sotib oldi: "))
# if books >=3:
#     print("Jamshid sovg'aga ega bo'ldi")
#     print(f"Jamshidning jami kitoblari {books+1} ta")
# else:
#     print("Jamshidga sovg'a berilmaydi")
#     print(f"Jamshidning jami kitoblari {books} ta")

# 5
#
# usd = 12400
# rub = 160
#
# money = int(input("Almashtirilishi kerak bo'lgan miqdorni UZS da kiriting: "))
# currency = input("Qaysi valyutaga o'zgartirishni hohlaysiz [RUB/USD]: ")
# if  currency == "USD":
#     print(f"{money} so'm {round(money/usd,1)} USD ga almashtirildi")
# elif currency =="RUB":
#     print(f"{money} so'm {round(money /rub, 1)} RUB ga almashtirildi")
# else:
#     print("Bunday valyutani ayirboshlay olmaymiz!")

# 6
# number = int(input("3 xonali raqamni kiriting: "))
# first = number //100
# second = number//10%10
# third = number%10
# if  second==third:
#     print("Ikkinchi va uchinchi raqam bir-biriga teng!")
# elif first==third:
#     print("Birinchi va uchinchi raqam bir-biriga teng!")
# elif first==second:
#     print("Birinchi va ikkinchi raqam bir-biriga teng!")
# else:
#     print("Hech biri bir-biriga teng emas!")


# 7
#
# number = int(input("Raqamni kiriting: "))
# if  number%2==0:
#     if number%3==0 and number%7==0:
#         print(f"{number} raqami juft, 3 ga va 7 ga qoldiqsiz bo'linganligi uchun siz musoboqa g'olibiga aylandingiz!")
#         print(f"Siz {round(number*0.9,0)} USD yutuqga ega bo'ldingiz!")
#     elif number%3==0 and number%7>0:
#         print(f"{number} raqami juft, 3 ga qoldiqsiz bo'linadi, lekin 7 ga qoldiqsiz bo'linmaydi!")
#     elif number % 3>0:
#         print(f"{number} raqami juft, lekin 3 ga qoldiqsiz bo'linmaydi!")
# else:
#     print(f"{number} raqami juft emas! ")

# 8
#
# weather = input("Bugun obhavo qanday (sunny / cloudy): ")
# auto = input("Avtomobil bormi (yes/ no): ")
# ok = input("Hamma rozimi sayrga chiqishga (yes/no): ")
#
# if weather=="sunny" and auto == "yes" and ok== "yes":
#     print("Jo’rabek do’stlari bilan sayrga chiqishadi")
# else:
#     print("Jo’rabek do’stlari bilan sayrga chiqishmaydi")

# 9
# weekday = int(input("Hafta kunini kiriting: "))
# days = ["dushanba", "seshanba","chorshanba","payshanba", "juma", "shanba", "yakshanba"]
#
# if 0< weekday <8:
#     day = days[weekday-1]
#     print(f"Bugun {day}!")
# else:
#     print("Kechirasiz, bu hafta kuni emas!")

# 10
# first = input("Istalgan sonni kiriting (1/3): ")
# second = input("Istalgan sonni kiriting (2/3): ")
# third = input("Istalgan sonni kiriting (3/3): ")
# print(max(first, second, third))

# 11
# sum = int(input("Siz yechib olmoqchi bo‘lgan miqdorni kiriting: "))
# if  sum%100!=0:
#     print("Bunday summani yechib olishning iloji yo‘q. Boshqa bankomatdan foydalaning.")

# 12
# date = int(input("Kunni kiriting: "))
# if date%2==0:
#     print("Tish ipidan foydalanish maslahat beriladi")
# else:
#     print("Tish ipidan foydalanish maslahat berilmaydi")

# 13
# rus = int(input("Rus tili bo‘yicha ballar miqdorini kiriting: "))
# math = int(input("Matematika bo‘yicha ballar miqdorini kiriting: "))
# it = int(input("Informatika bo‘yicha ballar miqdorini kiriting: "))
# if  rus+math+it >= 270:
#     print("Tabriklaymiz, siz byudjet asosida qabul qilindingiz!")
# else:
#     print("Afsuski, sen byudjet asosida qabul qilinmading.")

# 14
# distance = int(input("Bosib o'tish kerak bo'lgan masofani kilometrda kiriting: "))
# if distance > 400:
#     print("Sizning yoqilg'ingiz bu masofaga yetmaydi, iltimos zapravka qiling")
# else:
#     print("Siz bu masofani be'malol bosib o'ta olasiz")
