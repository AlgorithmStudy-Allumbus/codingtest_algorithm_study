'''
BOJ #1562. 계단수 (골드 1)
https://www.acmicpc.net/problem/1562
유형: 비트마스킹, DP
'''

N = int(input())
MOD = 1_000_000_000
BIT = 1 << 10

dp = [[[0] * BIT for _ in range(10)] for _ in range(N)]

for j in range(1, 10):
    dp[0][j][1 << j] = 1

for i in range(1, N):
    for j in range(10):
        for bit in range(BIT):
            nxt_bit = bit | 1 << j

            if 0 < j:
                dp[i][j][nxt_bit] += dp[i - 1][j - 1][bit]

            if j < 9:
                dp[i][j][nxt_bit] += dp[i - 1][j + 1][bit]

            dp[i][j][nxt_bit] %= MOD

cnt = 0
for j in range(10):
    cnt += dp[N - 1][j][BIT - 1]
    cnt %= MOD

print(cnt)