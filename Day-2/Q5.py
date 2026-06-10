num = int(input("Enter any number: "))
sum_digits = 0
temp = num  
while temp > 0:
    rem = temp % 10          
    sum_digits = sum_digits + rem  
    temp = temp // 10         
print("The sum of digits of", num, "is:", sum_digits)
