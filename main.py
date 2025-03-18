operator=input("enter your operator + - * /:")

num1=float(input('enter your 1st number'))
num2=float(input('enter your 2st number'))



if operator=="+" :
    result = num1 + num2
    print(result)
elif operator=="-" :
    result = num1 - num2
    print(result)
elif operator == "*" :
    result = num1 * num2
    print(result)
elif operator == "/" :
    result = num1 / num2
    print(result)

else:
    print('enter valid operator')

