# def calculate_salary(*args):
#     work_time, price = args
#     return work_time * price

# def calculate_salary(*args):
#     if len(args)==2:
#         return args[0]*args[1]
#     elif len(args)==3:
#         return args[0]*args[1]-args[2]
#     else:
#         pass
#
# salary = calculate_salary(5, 500000)
# print(salary)
#
# def communal_expences(price,used, stock=0, payment_method='Click'):
#     return price*used-stock
#
# def communal_expences(**kwargs):
#     if kwargs.get('stock'):
#         return kwargs['price']*kwargs['used']-kwargs['stock']
#     else:
#         return kwargs['price']*kwargs['used']
#
# print(communal_expences(price=450, used=400))

# def difference_in_ages(ages):
#     new_ages=[]
#     new_ages.append(min(ages))
#     new_ages.append(max(ages))
#     new_ages.append(max(ages)-min(ages))
#     new_ages=tuple(new_ages)
#     return new_ages
# print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88])
#

# def difference_in_ages(ages):
#     return (min(ages) , max(ages) , max(ages) - min(ages))
#
# print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88])

# def square_sum(numbers):
#     return sum(a**2 for a in numbers)
#
# print(square_sum([0, 3, 4, 5]))

# def square_sum(numbers):
#     square=0
#     for i in numbers:
#         square += i*i
#     return square

# print(square_sum([0, 3, 4, 5]))

# def smash(words):
#     return " ".join(words)
#
# words = ['hello', 'world', 'this', 'is', 'great']
# print(smash(words))

#the-stealth-warrior
def to_camel_case(text):
    a= text.split(" ")
    new_text =[]
    for x in range(len(a)):
        new_text.append(x)
    return "".join(new_text)

text = input("Matnni kiriting: ")
print(to_camel_case(text))
