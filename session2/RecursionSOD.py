def SOD(n):
    if n== 0:
        return 0
    return n%10 + SOD(n//10)

print (SOD(1234))