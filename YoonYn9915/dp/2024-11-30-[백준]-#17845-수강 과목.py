N, K = map(int, input().split())
arr = [0]
dp = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(K):
    importance, time = map(int, input().split())
    arr.append([importance, time])

for i in range(K+1):
    for j in range(N+1):
        if i == 0 or j == 0:
            continue

        importance, time = arr[i]
        if time > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(importance + dp[i - 1][j - time], dp[i - 1][j])

print(dp[K][N])
