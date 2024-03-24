a = int(input())
sts = list(map(int, input().split())) 
stack = []
target = 1

for st in sts:
    stack.append(st)
    while stack and stack[-1] == target:
        stack.pop()
        target +=1

if stack: 
    print('Sad') 
else:
    print('Nice')
