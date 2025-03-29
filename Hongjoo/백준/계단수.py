"""
https://www.acmicpc.net/problem/1562
"""
N = int(input())
MOD = 1e9
# dp[N번째 수][마지막 수][방문한 수 bitmasking(0~1023)]
dp = [[[0]*1024 for _ in range(10)] for _ in range(N+1)]
 
for i in range(1, 10):
    dp[1][i][1<<i] = 1
 
# n = N번째 수
for n in range(2, N+1):
    # i = 마지막 방문 숫자가 i
    for i in range(10):
        # 0~9까지 모든 수를 방문해야 한다는 조건이 있으므로, 방문 여부를 bitmasking을 통해 저장해야 함.
        for bit in range(1024):
            if i == 0:
                dp[n][i][bit | (1<<i)] += dp[n-1][i+1][bit]
            elif i == 9:
                dp[n][i][bit | (1<<i)] += dp[n-1][i-1][bit]
            else:
                dp[n][i][bit | (1<<i)] += dp[n-1][i-1][bit] + dp[n-1][i+1][bit]
            
            dp[n][i][bit | (1<<i)] %= MOD
    
res = 0
for i in range(10):
    res += dp[N][i][2**10-1]
 
print(int(res%MOD))