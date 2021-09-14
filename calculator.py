# homework 1
a = int(input())
operator = input()
b = int(input())
if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    if b == 0:
        print("Universe error: do not divide by zero!")
    else:
        print(a/b)
else:
    print("Oops, your math is too high for this script=)")