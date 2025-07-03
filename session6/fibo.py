def fibonacci(n):
    if n<= 1:
        return n
    else: 
        
        return fibonacci(n-1)+ fibonacci(n-2)
           
fbo = int(input("No of Nums for fibo: "))
for i in range (0,fbo):
    print(fibonacci(i),end= " ")

