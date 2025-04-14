'''
BOJ #10844. 쉬운 계단수 (실버1)
https://www.acmicpc.net/problem/10844
유형: DP
'''

n = int(input())

Mod = 1000000000
# 1. 초기화
# dp [총 길이 i ][마지막 자리수가 j] = 인 개수
dp = [[0]*10 for _ in range(n+1)]
dp[1][0] = 0 
for j in range(1,10):
    dp[1][j]= 1

# 2 점화식 N>=2
for i in range(2,n+1):
    for j in range(10):
        if j== 0 : 
            dp[i][j] = dp[i-1][j+1]    
        elif j==9:
            dp[i][j] = dp[i-1][j-1]
        else : 
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%Mod)