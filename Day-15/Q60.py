n = int(input())
arr = [int(x) for x in input().split()]

insert_pos = 0

for i in range(n):
    if arr[i] != 0:
        arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
        insert_pos += 1

print(*arr)
