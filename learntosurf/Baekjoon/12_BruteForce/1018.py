# 다른 풀이 
m, n = map(int, input().split())
plate = []
count = []

for _ in range(m):
    plate.append(input())

for a in range(m-7):
    for b in range(n-7):
        W = 0
        B = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if plate[i][j] != 'W':
                        W += 1
                    if plate[i][j] != 'B':
                        B += 1
                else:
                    if plate[i][j] != 'B':
                        W += 1
                    if plate[i][j] != 'W':
                        B += 1
        count.append(min(W, B))

print(min(count))
