num = int(input("Enter a number: "))
n = num
largest_factor = 1
while n % 2 == 0:
    largest_factor = 2
    n //= 2
factor = 3
while factor * factor <= n:
    while n % factor == 0:
        largest_factor = factor
        n //= factor
    factor += 2
if n > 2:
    largest_factor = n

print("The largest prime factor of", num, "is:", largest_factor)
