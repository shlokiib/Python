def GCD(a,b):

    # a = int(input("Enter the Number 1 : "))
    # b = int(input ("Enter the Number 2 : "))
    gcd=1 
    for i in range (1, min(a,b)+1):
        if a%i ==0 and b %i ==0 :
            gcd=i 
    
    print(f"The Greatest Common Devisor of the given Numbers is: {gcd}")   



a = int(input("Enter the Number 1 : "))
b = int(input ("Enter the Number 2 : "))
GCD(a,b)