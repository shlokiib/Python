def evenOdd(x):
    if (x%2 == 0 ):
        print("Even ")
    else:
        print("Odd")
        
evenOdd(2)
evenOdd(9)

def myFun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

myFun(name='Alice',age=25, city="New York")

def myFunc(*argv):
    for arg in argv:
        print(arg)

myFunc('Hello','Welcome','to','Nagpur')