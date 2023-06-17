first = input("Enter your First number: ")
opp = input("What you want to perform '+ - * /': ")
second = input("Enter your second number: ")
first = int(first)
second = int(second)
if opp == '+':
    print(first + second)
elif opp == '-':
    print(first - second)
elif opp == '*':
    print(first * second)
elif opp == '/':
    print(first / second)
elif opp == '%':
    print(first % second)
else : print("Invalid")
