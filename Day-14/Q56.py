n = int(input())
arr = [int(x) for x in input().split()]

printed = set()
for i in range(n):
    if arr[i] in printed:
        continue
    is_duplicate = False
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            is_duplicate = True
            break
    if is_duplicate:
        print(arr[i])
        printed.add(arr[i])
