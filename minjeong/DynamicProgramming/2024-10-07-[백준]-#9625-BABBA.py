import sys
input = sys.stdin.readline

K = int(input())
dp = [[0, 0] for _ in range(K+1)]  # 각 리스트가 독립적으로 생성되도록 수정
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, K+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]  # A 개수
    dp[i][1] = dp[i-1][1] + dp[i-2][1]  # B 개수

print(dp[K][0], dp[K][1])