import sys

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

inp = sys.stdin.readline

n = int(inp())

print(fib(n))