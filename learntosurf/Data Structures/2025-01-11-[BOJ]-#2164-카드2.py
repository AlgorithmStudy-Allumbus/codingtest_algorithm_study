import sys
input = sys.stdin.read

N = int(input())
L = list(range(1,N+1))

while (len(L)>1):
    L.pop(0)
    temp = L.pop(0)
    L.append(temp)

print(L.pop(0))