def calculator():
    print('+')
    print('-')
    print('*')
    print('/')
    print('%')
    print('**')
    operation = input("Select an operator:n")
    print("Enter two numbers")
    number_1 = int(input())
    number_2 = int(input())

    if operation == '+': # To add two numbers
        print(number_1 + number_2)
    elif operation == '-': # To subtract two numbers
        print(number_1 - number_2)
    elif operation == '*': # To multiply two numbers
        print(number_1 * number_2)
    elif operation == '/': # To divide two numbers
        print(number_1 / number_2)
    elif operation == '%': # To remainder two numbers
        print(number_1 % number_2)
    elif operation == '**': # To num1 exponent num2
        print(number_1 ** number_2)
    else:
        print('Invalid Input')

calculator()

calculator()