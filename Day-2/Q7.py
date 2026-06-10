# python program to find product of digits
num = int(input("Enter a number: "))

product = 1
temp = num
if temp == 0:
    product = 0
while temp > 0:
    rem = temp % 10
    product = product * rem
    temp = temp // 10

print("Product of digits is:", product)
