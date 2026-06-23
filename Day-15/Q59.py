n = int(input())
arr = [int(x) for x in input().split()]
k = int(input())

k = k % n
result = arr[-k:] + arr[:-k]

print(*result)
