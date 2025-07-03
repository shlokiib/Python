def pow2two(n:int):
    temp = 0
    
    if n%2 == 1:
        return False
    if n==2:
        return True
    else:
        n = n //2 
        temp +=1
        return pow2two(n)
         
    

result = pow2two(int(input("enter the number")))

print(result)