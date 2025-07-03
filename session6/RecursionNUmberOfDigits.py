def NOD(n):
    if n== 0:
        return 0
    result=  1 + NOD(n//10)
    return result

num = int(input("enter NUmber: "))
print (NOD(num))