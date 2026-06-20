def find_maximum(num1, num2):
    if num1 > num2:
        return num1
    return num2
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

result = find_maximum(first_number, second_number)
print("The maximum number is:", result)
