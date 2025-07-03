def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    return merge(left, right)

def merge(lhs, rhs):
    result = []
    i = j = 0

    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:
            result.append(lhs[i])
            i += 1
        else:
            result.append(rhs[j])
            j += 1

    
    result.extend(lhs[i:])
    result.extend(rhs[j:])
    
    return result


arr = [12, 65, 98, 62, 88, 1]
print(mergesort(arr))
