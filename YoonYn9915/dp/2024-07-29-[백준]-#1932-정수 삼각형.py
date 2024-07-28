import sys

n = int(sys.stdin.readline().strip())

arr = [[0] * n for _ in range(n)]
ans = [[0] * n for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))

ans[0][0] = arr[0][0]

for j in range(n-1):
    for k in range(j+1):
        for f in range(2):
            if ans[j+1][k] == 0:
                ans[j+1][k+f] = ans[j][k]+arr[j+1][k+f]
            else:
                ans[j+1][k+f] = max(ans[j+1][k+f], ans[j][k]+arr[j+1][k+f])


max_value = max(ans[n-1])
print(max_value)