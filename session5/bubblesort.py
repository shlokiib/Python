
def bubblesort(arr):   
    l = len(arr)
    for i in range (0,l):
        for j in range (0,l-i-1):
            if arr[j+1]<=arr[j]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr
 
arr = [7,18,45,99,10,4]
sorted_arr = bubblesort(arr)    
print(sorted_arr)

    