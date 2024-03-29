import sys
input = sys.stdin.readline

n = int(input())
wine = [0] * n
for i in range(n):
    wine[i] = int(input())

dp = [0] * n
dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]

# n이 1보다 클 때만 두 번째 포도주부터 로직 실행
for i in range(2, n):
    # 현재 포도주를 마시지 않는 경우, 현재 포도주와 이전 포도주를 마시는 경우,
    # 그리고 이전 포도주를 마시지 않고 현재 포도주를 마시는 경우를 고려
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[-1])
