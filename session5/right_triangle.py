# for i in range (0,6,1):
#     print(" * "*i)
    

rows = 5 
for i in range(1, rows + 1):
       spaces = rows - i
       stars = 2 * i - 1
       print(" " * spaces + "*" * stars)
       