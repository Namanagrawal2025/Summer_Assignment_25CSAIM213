def find_factorial(num):
    if num < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
user_number = int(input("Enter a positive integer for factorial: "))

result = find_factorial(user_number)
print("The factorial is:", result)
