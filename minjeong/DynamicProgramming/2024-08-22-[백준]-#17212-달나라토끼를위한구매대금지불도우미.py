import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

# 1부터 7까지 최소 동전 개수 초기화
dp[1:8] = [1, 1, 2, 2, 1, 2, 1]

for i in range(8, N+1):
    dp[i] = min(dp[i-1]+1, dp[i-2]+1, dp[i-5]+1, dp[i-7]+1)

print(dp[N])