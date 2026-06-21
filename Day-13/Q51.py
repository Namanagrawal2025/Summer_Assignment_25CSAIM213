def find_largest_and_smallest():
    n = int(input())
    arr = [int(x) for x in input().split()][:n]
    smallest = min(arr)
    largest = max(arr)
    print(smallest, largest)

find_largest_and_smallest()
