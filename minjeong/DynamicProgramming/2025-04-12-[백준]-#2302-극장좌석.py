import sys
input = sys.stdin.readline

# 1. 입력
N = int(input())  # 좌석의 개수
M = int(input())  # 고정석의 개수
vip_list = [int(input()) for _ in range(M)]  # VIP 고정석 번호 리스트

# 2. DP 초기화
dp = [0] * (N + 1)
dp[0], dp[1] = 1, 1

# 3. 피보나치 수열 기반 DP 채우기
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

# 4. 좌석 구간별 계산
answer = 1
prev = 0  # 이전 VIP 좌석 번호

for vip in vip_list:
    section = vip - prev - 1  # VIP 좌석 전까지 자유 좌석 구간 길이
    answer *= dp[section]     # 그 구간에서 가능한 배치 수 곱하기
    prev = vip                # 현재 VIP를 기준으로 다음 구간 나눌 준비

# 5. 마지막 구간 처리 (VIP 이후 남은 좌석이 있는 경우)
section = N - prev
answer *= dp[section]

print(answer)