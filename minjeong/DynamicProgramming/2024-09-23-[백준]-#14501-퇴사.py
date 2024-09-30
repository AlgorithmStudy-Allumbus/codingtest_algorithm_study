import sys
input = sys.stdin.readline

# 초기화
N = int(input())    # 남은 날짜
t = [0] * (N+1)     # 걸리는 기간 리스트
p = [0] * (N+1)     # 상담 금액 리스트
dp = [0] * (N+1)    # DP
for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())

# DP 채우기
for i in range(1, N+1):
    time, pay = t[i], p[i]
    day = i + time - 1
    dp[i] = max(dp[i], dp[i-1])
    if day <= N:
        dp[day] = max(dp[day], dp[i - 1] + pay)
print(dp[-1])