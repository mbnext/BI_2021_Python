# homework 1
a = int(input("Введите первое число:"))
operator = input("Введите знак операции:")
b = int(input("Введите второе число:"))
if operator == "+":
    print("Результат: ", a+b)
elif operator == "-":
    print("Результат: ", a-b)
elif operator == "*":
    print("Результат: ", a*b)
elif operator == "/":
    if b == 0:
        print("Universe error: do not divide by zero!")
    else:
        print("Результат: ", a/b)
else:
    print("Oops, your math is too high for this script=)")