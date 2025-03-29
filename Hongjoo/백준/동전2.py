"""
https://www.acmicpc.net/problem/2294
# dp
- n개의 동전 조합으로 가치 합이 k 가 되는 경우
- 그 중 사용 동전 최소
- 메모리 제한 128MB
# 문제 
-dp[0] = 0 ,
j : 사용 가능한 coin 종류 
DP[k] =  min(dp이전[k] , "dp[k-c]+1 )
"""
import sys

n , k  = map(int, sys.stdin.readline().split())
coins = list()
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

coins.sort() 

# 2. dp 테이블 초기화
INF= int(1e9)
dp = [INF for _ in range(k+1)]
dp[0] = 0 
for c in coins :
    for j in range(c, k+1) :
        dp[j] = min(dp[j] , dp[j-c]+1)

#3. 출력 - 업데이트x 면 -1 출력
if dp[k] == INF : 
    print(-1)
else : 
    print(dp[k])
