import sys
input = sys.stdin.readline

# 1️⃣ DP 배열 초기화
dp = [1] * 101  # 최대 N=100까지 미리 계산
for i in range(4, 101):  # P(4)부터 점화식 적용
    dp[i] = dp[i - 2] + dp[i - 3]

# 2️⃣ 테스트케이스 입력 처리
T = int(input())  # 테스트케이스 수
for _ in range(T):
    N = int(input())  # N 입력
    print(dp[N])  # 미리 계산된 DP에서 값 출력