# 1
# my_tuple = (10, 14, 26, 43, 31)
# my_tuple=list(my_tuple)
# my_tuple.append(88)
# my_tuple= tuple(my_tuple)
# print(my_tuple)

# 2
# my_tuple = ("Orange", 'apple', 10, 20, 30, 5, 15, 25)
# print("Natija:",my_tuple[3])

# # 3
# my_tuple= (13, 'python', 26, 'c++', 89, 56, 'java', 23, 47, 'c#', 78)
# print(f"Boshlang'ich tuple: {my_tuple}")
# old_element = input("Almshtirilishi kerak bo'lgan elementni kiriting: ")
# new_element = input("Qanday ma'lumot joylashtiramiz: ")
# my_tuple= list(my_tuple)
# if old_element in my_tuple:
#     i = my_tuple.index(old_element)
#     my_tuple[i]= new_element
#     my_tuple=tuple(my_tuple)
#     print(f"Yakuniy natija: {my_tuple}")
# elif int(old_element) in my_tuple:
#     i = my_tuple.index(int(old_element))
#     my_tuple[i]= int(new_element)
#     my_tuple = tuple(my_tuple)
#     print(f"Yakuniy natija: {my_tuple}")
# else:
#     print("Ushbu element tuple ichida mavjud emas!")

# 4
# my_list = [1, 2, 4, 5, 63, 13, 32, 10, 54, 78]
# print(f"Tasodifiy elementlardan tashkil topgan list: {my_list}")
# print(f"Eng katta qiymati: {max(my_list)}")
# print(f"Eng kichik qiymati {min(my_list)}")
# print(f"Yig'indisi: {sum(my_list)}")
#
# 5
# my_list= []
# my_list.append(int(input("1-raqam: ")))
# my_list.append(int(input("2-raqam: ")))
# my_list.append(int(input("3-raqam: ")))
# print(sum(my_list)/len(my_list))

# 6
# my_list = input("Listni kiriting: ") #python c++ java c# javascript
# my_list = my_list.split()
# print(my_list)
# my_list.reverse()
# print(my_list)

# 7
#
# list = [19, 100, 25, 55, 1253, 81, 47, 20, 187]
# print("Eng kichik qiymat indeksi:",min(list))
# print("Eng katta qiymat indeksi:",max(list))
# for x in range(len(list)):
#     if list[x] == min(list):
#          list.insert(x+1, 0)
#     break
# for x in range(len(list)):
#     if list[x] == max(list):
#         list.insert(x+1, 0)
# print("Yakuniy natija:", list)

# 8
# test_list= ['TopSkill is best', 'for learning', 'Awesome']
# print("Boshlang'ich list:", test_list)
# new_list = ""
# for i in test_list:
#     new_list += i+" "
# new_list = new_list.split()
# print(new_list)

# 9
# price = int(input("Olmaning narxini kiriting: "))
# for i in range (1,11):
#     print(f"{i} kg olmaning narxi => {i*price}")
#
# 10
# word = input("So'z kiriting(quit dasturdan chiqish uchun): ")
# if word =="quit":
#     quit()
# else:
#     word = word[::-1]
# print(word)

# 11
# print("Kalkulyator ishga tushdi...")
# while True:
#     a = int(input("1-sonni kiriting: "))
#     b = int(input("2-sonni kiriting: "))
#     c= int(input("Quyidagi amallardan birini tanlang: \n1 - qo'shish \n2 - ayirish \n3 - ko'paytirish \n4 - bo'lish \n:"))
#     if c==1:
#         print(a+b)
#     elif c==2:
#         print(a-b)
#     elif c==3:
#         print(a*b)
#     elif c == 4:
#         print(a / b)
#     d = input("Davom etamizmi? [ha/yo'q] ")
#     if d =="ha":
#         continue
#     elif d=="yo'q":
#         print("Kalkulyatorimizdan foydalanganingiz uchun rahmat!")
#         break


# 11.2
# word = "*"
# new_word = ""
# for i in range(1, 6):
#     new_word = new_word + word
#     print(new_word)

# 12
# time = 10
# for i in range(0,time):
#     d = input("Bombani zararsizlantirishni xohlaysizmi yoki o'yin atmosferasini kuchaytirishda davom etasizmi: ")
#     if d=="yo'q":
#         time-=5;
#         if time==0:
#             print("bomba portladi")
#         print(f"portlashga {time} soniya vaqt qoldi")
#     elif d=="ha":
#         print(f"Portlashdan {time} soniya oldin zararsizlantirildi")
#         break

# 13
# s =0
# for i in range(0,10):
#     word = input("Jamoaga qo'shilish uchun kalit so'zini ayting: ")
#     if word=="Caramba":
#         s+=1
# print(f"Janob kapitan! Sizning topshirig'ingizni faqatgina {s} kishi bajara oldi.")

# 14
# word = ['xm', 'hm', 'ok', 'axa']
# answer = input("SMS xabar: ")
# if answer in word:
#     print(f"Noinsof, shuncha xabarimga bitta {answer} yozasanmi?")
