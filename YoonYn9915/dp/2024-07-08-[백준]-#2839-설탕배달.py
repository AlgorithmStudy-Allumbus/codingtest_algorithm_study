n = int(input())

dp = [-1 for _ in range(5001)]
dp[3] = 1
dp[5] = 1

if n <= 5:
    print(dp[n])
else:
    for i in range(6, n + 1):
        a, b = dp[i], dp[i]

        if dp[i - 5] != -1:
            a = dp[i - 5]
        if dp[i - 3] != -1:
            b = dp[i - 3]

        if a > 0 and b > 0:
            dp[i] = min(a + 1, b + 1)
        elif a > 0 and b < 0:
            dp[i] = a + 1
        elif a < 0 and b > 0:
            dp[i] = b + 1
        else:
            dp[i] = -1

    print(dp[n])