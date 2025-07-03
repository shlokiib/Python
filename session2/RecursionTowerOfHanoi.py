def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)


n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'C', 'B')
print(f"\nTotal moves required: {2**n - 1}")
