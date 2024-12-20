import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())

# DP 배열 초기화
dp = [0] * (n+1)
dp[1] = 1

# 초기값 설정
if n >= 2:
    dp[2] = 3

# 점화식을 이용해 계산
for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

# 결과 출력
print(dp[n])
