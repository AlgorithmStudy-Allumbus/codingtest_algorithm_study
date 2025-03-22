

n, k = map(int, input().split())

coins = []
dp = [[-1] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    coins.append(int(input()))

for i in range(1, n + 1):
    for j in range(1, k + 1):

        if i == 1:
            # 첫번째 열일때 나누어 떨어지면 몫을 나누어 떨어지지 않으면 -1을 저장한다.
            if j % coins[i-1] == 0:
                dp[i][j] = j // coins[i-1]
        else:

            if j <= coins[i-1]:
                # 현재 동전의 가치와 딱 나누어 떨어지는 경우
                if coins[i-1] == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                if dp[i][j - coins[i-1]] != -1 and dp[i - 1][j] != -1:
                    dp[i][j] = min(dp[i][j - coins[i-1]] + 1, dp[i - 1][j])
                elif dp[i][j - coins[i-1]] == -1 and dp[i - 1][j] == -1:
                    dp[i][j] = -1
                elif dp[i][j - coins[i-1]] == -1:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - coins[i-1]] + 1



print(dp[n][k])
