import sys
input = sys.stdin.readline

# 1. 입력
N = int(input())
MOD = 10**9


# 2. DP 정의
# dp[n][last_digit][bitmask]
# n: 숫자 길이, last_digit: 마지막 자리 숫자, bitmask: 지금까지 어떤 숫자들이 나왔는지 (비트마스크)
# 범위 - n: 입력값, last_digit: 0~9, bitmask: 0~1023
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]

# 3. 초기상태 설정
# 길이가 1일 때, 0을 제외하고 1~9로 시작할 수 있음
for i in range(1, 10):
    dp[1][i][1 << i] = 1

# 4. 점화식대로 DP 채우기
# n: N번째 수
for n in range(2, N+1):
		# last_digit: 마지막 자리 숫자
    for last_digit in range(10):
        # 0~9까지 모든 수를 방문해야 한다는 조건이 있으므로 방문여부를 비트마스킹을 통해 저장
        for mask in range(1024):
            if last_digit == 0:
                dp[n][last_digit][mask | (1 << last_digit)] += dp[n - 1][last_digit + 1][mask]
            elif last_digit == 9:
                dp[n][last_digit][mask | (1 << last_digit)] += dp[n - 1][last_digit - 1][mask]
            else:
                dp[n][last_digit][mask | (1 << last_digit)] += (
                        dp[n - 1][last_digit - 1][mask] + dp[n - 1][last_digit + 1][mask]
                )
            dp[n][last_digit][mask | (1 << last_digit)] %= MOD

# 5. 정답 계산 및 출력
answer = 0
for i in range(10):
    # N자리 수 중에서 i로 끝나는 수 중 0부터 9까지 다 있는 수를 누적해서 더하기
    answer += dp[N][i][1023]

print(answer % MOD)
