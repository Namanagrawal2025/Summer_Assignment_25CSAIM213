n = int(input())
arr = [int(x) for x in input().split()]
target = int(input())

index = -1
for i in range(n):
    if arr[i] == target:
        index = i
        break

print(index)
