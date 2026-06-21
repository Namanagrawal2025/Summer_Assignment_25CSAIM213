def count_even_and_odd():
    n = int(input())
    arr = [int(x) for x in input().split()][:n]
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = n - even_count
    print(even_count, odd_count)

count_even_and_odd()
