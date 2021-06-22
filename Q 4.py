num = int(input("Enter a number: "))
sum1 = 0
temp1 = num
while temp1 > 0:
    digit1 = temp1 % 10
    sum1 += digit1**3
    temp1 //= 10
if num == sum1:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")