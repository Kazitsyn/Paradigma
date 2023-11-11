def binary_search(x, arr):
    if len(arr) == 0:
        return 0
    if x == arr[0]:
        return 1
    if x < arr[0]:
        return binary_search(x, arr[:len(arr)//2])
    if x > arr[0]:
        return binary_search(x, arr[len(arr)//2:])
    return 0

result = binary_search(3, [1, 2, 3, 4, 5])
print(result) # Output: 1