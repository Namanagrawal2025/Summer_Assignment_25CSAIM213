num = int(input("Enter a number: "))
temp = num
sum_factorial = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum_factorial += fact
    temp //= 10
if sum_factorial == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")
