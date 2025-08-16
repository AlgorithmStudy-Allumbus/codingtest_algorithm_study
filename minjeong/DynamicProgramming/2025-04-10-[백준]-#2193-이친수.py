import sys
input = sys.stdin.readline

'''
이친수:
- 0과 1로 이루어진 수
- 0으로 시작하지 않음
- 1이 두 번 연속으로 나타나지 않음

N이 주어질 때, N자리 이친수의 개수 구하기
'''

N = int(input())
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
