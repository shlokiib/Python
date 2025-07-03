def CountZeros(n):

    if n == 0:
        return 1
    if n < 10:
        return 0
    return (n % 10 == 0) + CountZeros(n // 10)

result = CountZeros(int(input("Enter a number: ")))
print(result)