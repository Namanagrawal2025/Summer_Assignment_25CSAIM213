n = int(input())
arr = [int(x) for x in input().split()]

start = 0
end = n - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(*arr)
