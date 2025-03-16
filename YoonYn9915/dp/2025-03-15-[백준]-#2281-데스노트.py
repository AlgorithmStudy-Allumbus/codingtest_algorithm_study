import sys
input = sys.stdin.readline

n, m = map(int, input().split())

names = [int(input()) for _ in range(n)]
dp = [[-1]*(m+1) for _ in range(n)]
dp[0][names[0]] = 0

for r in range(n-1):
    for c in range(1, m+1):
        if dp[r][c] != -1:
            if c+1+names[r+1] <= m:
                dp[r+1][c+names[r+1]+1] = dp[r][c]
            if dp[r+1][names[r+1]] != -1:
                dp[r+1][names[r+1]] = min(dp[r+1][names[r+1]], dp[r][c] + (m-c)**2)
            else:
                dp[r+1][names[r+1]] = dp[r][c] + (m-c)**2

answer = 1000000000
for i in range(1, m+1):
    if dp[n-1][i] != -1:
        answer = min(answer, dp[n-1][i])
print(answer)