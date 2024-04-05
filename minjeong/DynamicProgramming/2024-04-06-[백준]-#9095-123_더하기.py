import sys
input = sys.stdin.readline
dp = [1] * 12
dp[2] = 2
t = int(input())
for _ in range(t):
    n = int(input())    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])