n = int(input())

dp = [1, 1, 2, 3, 5, 8]

if n > 5:
    for i in range(6, n):
        dp.append(dp[i-1] + dp[i-2])

ans = (dp[n-1] * 2) + ((dp[n-1] + dp[n-2]) * 2)

if n == 1:
    ans = 4

print(ans)
