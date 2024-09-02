import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

inp = sys.stdin.readline

n = int(inp())

print(factorial(n))