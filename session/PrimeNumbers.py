def prime_nos():
    n = int(input("Enter a number: "))
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                print(f"{i} is not a prime")
                break
        else:
            print(f"{i} is a prime")

prime_nos()
