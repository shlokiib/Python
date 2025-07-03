def binary_search(arr):
    start = 0
    end = len(arr) - 1
    target = int(input("Enter the target: "))
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

