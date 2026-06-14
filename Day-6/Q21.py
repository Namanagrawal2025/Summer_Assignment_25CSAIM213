
n = int(input())
if n == 0:
    print(0)
else:
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(b)
