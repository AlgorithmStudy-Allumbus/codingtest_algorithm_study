num = int(input())
a = []

for i in range(num):
    b = int(input())
    
    if b == 0:
        a.pop()
    else:
        a.append(b)
print(sum(a))
