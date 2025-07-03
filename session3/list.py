my_list = [1,2,3,4,5]



print(my_list[-2:-5:-  1])
00
squares =[x**2 for x in range (1,10)]
print(squares)

matrix =[[1,2],[3,4],[5,6]]
flattened = [num for row in matrix for num in row]
print(flattened)

lables = ["Even" if x %2 == 0 else "Odd" for x in range (0,6)]
print(lables)       

def square(x):
    return x*x
squares1= [square(x) for x in range (1,6)]
print(squares1)

str = "Welcome to RBU"
print(str[::-1])
