arr = [7, 1, 5, 3, 6, 4]
buy = arr[0]
max_profit = 0

for i in range(1, len(arr)):
    if buy > arr[i]:
        buy = arr[i]
    elif arr[i] - buy > max_profit:
        max_profit = arr[i] - buy
print(max_profit)
        