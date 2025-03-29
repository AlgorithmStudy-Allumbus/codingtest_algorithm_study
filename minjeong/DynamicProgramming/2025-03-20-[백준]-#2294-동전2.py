import sys
input = sys.stdin.readline

MAX_NUM = 100001
n, k = map(int, input().split())          # 동전 개수, 목표 가치 합
coins = [int(input()) for _ in range(n)]  # 동전의 가치 리스트
coins.sort()

# DP 선언
dp = [MAX_NUM] * (k+1)
dp[0] = 0

# DP 채우기
for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c]+1)

# 정답 출력
if dp[k] == MAX_NUM:
    print(-1)
else:
    print(dp[k])