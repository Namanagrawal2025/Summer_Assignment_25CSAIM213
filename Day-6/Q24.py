x = float(input())
n = int(input())
r = 1
p = abs(n)
while p > 0:
    if p % 2 == 1:
        r *= x
    x *= x
    p //= 2
if n < 0:
    print(1 / r)
else:
    print(r)
