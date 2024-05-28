# try:
#     try:
#         num1 = int(input("Birinchi sonni kiriting: "))
#         num2 = int(input("Ikkinchi sonni kiriting: "))
#         print(num1/num2)
#     except ValueError as e:
#         print("Son kiriting!")
#
# except ZeroDivisionError as e:
#     print("Oga bo'lish mumkin emas!")



#kata
# The_Stealth_Warrior ->TheStealthWarrior
#the-stealth-warrior -> theStealthWarrior
# def to_camel_case(text):
#     split_text = text.split('-')
#     new_split =[]
#     for t in split_text:
#         new_split.extend(t.split('_'))
#     for t in range(1, len(new_split)):
#         cap= new_split[t].capitalize()
#         new_split[t] = cap
#     return "".join(new_split)
#
# print(to_camel_case('the_Stealth-Warrior'))

# def to_camel_case(text):
#     words = text.replace('_', '-').split('-')
#     return words[0] + ''.join([x.title() for x in words[1:]])
#
# def to_camel_case(text):
#     return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
# print(to_camel_case('The_Stealth-Warrior'))

#kata
#
# def array_plus_array(arr1,arr2):
#     return sum(arr1)+sum(arr2)
#
#
# print (array_plus_array([1,2,3], [4,5,6]))

#kata
# def sum_str(a, b): #"4",  "5" --> "9"
#     return str(int(a or 0)+int(b or 0))
#
# print(sum_str("4",  "" ))
#kata
# def powers_of_two(n):
#     return [2**x for x in range (n+1)]
#
# print(powers_of_two(2))
# def divisors(integer):
#     list =[]
#     for n in range (2,integer):
#         if integer%n==0:
#             list.append(n)
#         elif integer%n==1:
#             print(f"'{integer} is prime'")
#     return list
#
#
# # def divisors(integer):
# #     list =[]
# #     for n in range (2,integer):
# #         if
# #             list.append(n)
# #     if len(list)==0:
# #         print(f"{integer} is prime")
# #     return list
#
# print(divisors(12)) #should return [2,3,4,6]
# print(divisors(25)) #should return [5]
# print(divisors(13)) #should return "13 is prime"

#kata
# def convert_hash_to_array(h):
#     result = h.items()
#     new_result = []
#     for i in result:
#         new_result.append(list(i))
#     return sorted(new_result)
#
# print(convert_hash_to_array({"name": "Jeremy", "age": 24}))
# #other answers
# def convert_hash_to_array(hash):
#     return sorted(map(list, hash.items()))
#
# def convert_hash_to_array(hash):
#     return [[k, hash[k]] for k in sorted(hash)]
#
# def convert_hash_to_array(dct):
#     return sorted(list(item) for item in dct.items())
#
# def convert_hash_to_array(h):
#     return [*map(list,sorted(h.items()))]

#kata
# def array_conversion(arr):
#     pass
#[1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186]
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# new_arr=[]
# new_arr2=[]
#
#     for n in range(1,len(arr),2):
#         a = arr[n] + arr[n-1]
#         new_arr.append(a)
#
#     for n in range(1, len(new_arr),2):
#         a = new_arr[n] * new_arr[n - 1]
#         new_arr2.append(a)
#
#
# print(new_arr, new_arr2)

# '123'   ==>  ['321', '21', '1']
# 'abcde' ==>  ['edcba', 'dcba', 'cba', 'ba', 'a']
text = '123'
a=[]
print(text.strip())
# for i in range(len(text)):
#     b= text.rstrip()
#     a.append(b)
# print(a)




