"""
[BOJ]평범한 배낭_2트/09.14.2025
https://www.acmicpc.net/problem/12865
"""

import sys
input  =sys.stdin.readline
#1. 입력 변수 - 물품 총 개수 / 제한 무게 / 물건별 무게 w, 가치 v
N , K = map(int,input().split()) 
items = [[] for _ in range(N+1)]
for i in range(1,N+1):
  items[i] = list(map(int, input().split()))
# print(items)
#2. DP : 0-1 Knapsack 문제
# DP[k][i]: 최대 K kg 제한을 가진 가방안에 0~ i번쨰 item 까지 탐색 후 최대 가치
#(물건 w > 배낭 무게 k) dp[k][i] = dp[k][i-1] #물건i는 못 넣음
#(물건 w <= 배낭 무게 k) dp[k][i] = max(item[v] + dp[k-w][i-1],dp[k][i-1]) # 물건i를 넣거나(배낭 K-item 무게 만큼의 최대값 + 물건 i 넣기) , 안넣거나

dp = [[0]*(N+1) for _ in range(K+1)]
for k in range(1,K+1) :
  for i in range(1, N+1):
    if items[i][0] <= k : 
      dp[k][i] = max(dp[k-items[i][0]][i-1] + items[i][1],dp[k][i-1] )
    else :
      dp[k][i] =dp[k][i-1]

# print(dp)
#3. dp[-1][-1] = 최종 배낭 K kg에서 최대 가치 출력
print(dp[-1][-1])