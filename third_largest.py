arr = [12, 35, 1, 10, 34, 1]

n = len(arr)

if n < 3:
    print("The array should have at least three elements.")
else:
    largest = second_largest = third_largest = -float('inf')

    for i in range(n):
        if arr[i] > largest:
            third_largest = second_largest
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            third_largest = second_largest
            second_largest = arr[i]
        elif arr[i] > third_largest and arr[i] != second_largest and arr[i] != largest:
            third_largest = arr[i]

    if third_largest == -float('inf'):
        print("There is no third largest element.")
    else:
        print(f"The third largest element in the array is {third_largest}.")
