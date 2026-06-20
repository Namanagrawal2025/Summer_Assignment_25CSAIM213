def is_perfect_number(number):
    if number <= 1:
        return False
    divisors_sum = sum(i for i in range(1, (number // 2) + 1) if number % i == 0)
    return divisors_sum == number
print(is_perfect_number(6))
