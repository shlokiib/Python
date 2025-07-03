n=int(input("Ener Number: "))
temp=n
i=0
power= len(str(n))
while n>0:
    rev=n%10
    i += rev**power
    n= n//10
if temp == i:
    print("armstorms number !!!!!!!!") 
else:
    print("nahh")