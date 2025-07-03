rows = int(input("Enter size for box: "))
spaces = rows

for i in range(1, rows + 1):
       
       if i==1 or i== rows:
           print("* " * rows)
       else:
           print("*"+" "* spaces+"*")   
       
           