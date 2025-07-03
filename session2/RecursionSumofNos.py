def sum_of_natural_nos(n):
    if n==0:
        return 0
    else:
        return n + sum_of_natural_nos(n-1)

result = sum_of_natural_nos(5)
print (result) 