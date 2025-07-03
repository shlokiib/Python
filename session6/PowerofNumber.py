def sum_nos(a,pow):
    if a == 0:
        return 1
    if pow <=0:
        return 1
    result = a * sum_nos(a,pow-1) 
    return result
a = int(input("enter number "))
pow = int(input("enter power "))
print(sum_nos(a,pow))