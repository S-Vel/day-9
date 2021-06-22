def Fib(n):
   
    if n < 0:
        print("Incorrect input")
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fib(n-1) + Fib(n-2)

print(Fib(11))

def Fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    if n<0:
        print("Incorrect Input")
    elif n == 1 or n == 2:
        print('1')
    else :
         while count < n:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1

Fibonacci(12)