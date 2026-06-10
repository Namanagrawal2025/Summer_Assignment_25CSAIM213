num = int(input("Enter a number: "))
rev_num = 0
temp = num
while temp > 0:
    remainder = temp % 10
    rev_num = (rev_num * 10) + remainder
    temp = temp // 10
print("Reverse of the number is:", rev_num)