# 내 풀이
N, X = map(int, input().split())
A = input()

for i in map(int, A.split()):
    if i < X:
        print(i, end=' ')
