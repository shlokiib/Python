import sys

# Set a dangerously high recursion limit
sys.setrecursionlimit(10**6)

def overflow(n=1):
    print(f"Recursing at depth: {n}")
    overflow(n + 1)

overflow()
