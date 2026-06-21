def find_sum_and_average():
    n = int(input())
    arr = [int(x) for x in input().split()][:n]
    total_sum = sum(arr)
    average = total_sum / n
    print(total_sum, average)

find_sum_and_average()
