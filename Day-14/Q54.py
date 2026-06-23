n = int(input())
arr = [int(x) for x in input().split()]
target = int(input())

count = 0
for x in arr:
    if x == target:
        count += 1

print(count)
