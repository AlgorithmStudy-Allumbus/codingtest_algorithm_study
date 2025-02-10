K = int(input())
stack = []
for i in range(K):
    num = int(input())
    stack.append(num)
    if num == 0:
        stack.pop()
        stack.pop()

print(sum(stack))