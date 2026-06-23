n = int(input())
arr = [int(x) for x in input().split()]

largest = float('-inf')
second_largest = float('-inf')

for x in arr:
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest and x != largest:
        second_largest = x

if second_largest == float('-inf'):
    print("No second largest element")
else:
    print(second_largest)
