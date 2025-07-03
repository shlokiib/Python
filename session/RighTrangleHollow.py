def spaces(n):
    return " " * n

n = int(input("Enter height: "))

for i in range(1, n + 1):
    line = spaces(n - i) 

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n:
            line += "*"
        else:
            line += " "

    print(line)
