import sys
input = sys.stdin.readline

n = int(input()) # 수 입력 받기
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())
dp = [0] * (n+1) #dp 리스트 초기화

for i in range(1, n+1):
    time = t[i]
    pay = p[i]
    day = i + time - 1
    dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값
    if day <= n:
        dp[day] = max(dp[day], dp[i-1]+pay)

print(max(dp))