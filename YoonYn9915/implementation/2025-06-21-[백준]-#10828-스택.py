import sys
input = sys.stdin.readline

N = int(input())

stack = []
def query():
    Q = input().split()
    if Q[0] == "push":
        stack.append(int(Q[1]))
    elif Q[0] == "pop":
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif Q[0] == "size":
        print(len(stack))
    elif Q[0] == "empty":
        if len(stack):
            print(0)
        else:
            print(1)
    elif Q[0] == "top":
        if len(stack):
            print(stack[-1])
        else:
            print(-1)

for _ in range(N):
    query()