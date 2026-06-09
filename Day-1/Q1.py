def sum_natural_numbers_formula(n):
    if n < 1:
        return 0 
    return n * (n + 1) // 2

# Example
N = 10
result = sum_natural_numbers_formula(N)
print(f"The sum of the first {N} natural numbers is: {result}")