


arr=[12,13,45,78,98,65,32,65,45,65,98,12,45,6]
target = int(input("Enter Your Target "))
found = False
for i in range (0,len(arr)):
    if arr[i] == target :
        print(f"Target found at index {i}")
        found = True
if found != True:
    print ("Target not found")
            