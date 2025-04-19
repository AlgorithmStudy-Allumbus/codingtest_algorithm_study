"""
https://www.acmicpc.net/problem/17271

# 유형 :DP 
- 총 N 초 싸우는 동안  가능한 스킬 조합의 수
- A 는 1초 , B는 M 초 준비시간
- 시전중에 다른 스킬 사용 불가 & 스킬을 안쓰는 시간은 없음



"""
#
import sys; input = sys.stdin.readline
MOD = 1000000007

N, M = map(int, input().split())

# i초 때 가능한 경우의 수는 두 가지가 있다.
# i-1초까지 스킬 쓴 상태에서 A 스킬 사용
# i >= M일 때, i-M초까지 스킬 쓴 상태에서 B 스킬 사용
# dp(i) = dp(i-1) + dp(i-M)

dp = [1] * (N + 1)
for i in range(M, N + 1): # M초 미만일 땐 dp[i] = dp[i-1]이기 때문에 무조건 1이다.
    dp[i] = (dp[i - 1] + dp[i - M]) % MOD

print(dp[N])