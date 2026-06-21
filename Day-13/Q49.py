def input_and_display_array():
    n = int(input())
    arr = [int(x) for x in input().split()][:n]
    print(*arr)

input_and_display_array()
