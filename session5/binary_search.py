def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the target: "))
print ( result = binary_search(arr, target))

