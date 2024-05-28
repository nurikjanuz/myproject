def my_calculator (num1, num2, math_operator='+'):
    if math_operator=='+':
        print(num1 + num2)
    elif math_operator=='-':
        print(num1 - num2)
    elif math_operator=='*':
        print(num1 * num2)
    elif math_operator=='/':
        if num2!=0:
            print(num1 / num2)
        else:
            print("0ga bo'lish mumkin emas!")
    else:
        print("Kechirasiz, men ushbu amalni bajara olmayman")

def password_checker(count_password):
    if count_password>=8:
        print("Parolingiz talablarga javob beradi!")
    else:
        print("Parolingiz 8ta belgidan kam")