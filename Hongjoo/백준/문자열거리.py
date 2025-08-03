"""
## [백준] #1230. 문자열거리: DP / 골드1
> 문제 링크 : https://www.acmicpc.net/problem/1230
"""
import sys
input = sys.stdin.readline
# 0. 입력 변수 정의 및 초기화 하기
o = list(input())
l = list(input())
INF = 1000
if len(l) < len(o) :
  print(-1)
  exit()
#1. dp 정의
# dp[i][j][0] : de[i][j]로 O[:i] == L[:j]
dp = [[[0,0] for j in range(len(l)+1)] for i in range(len(o)+1)]
# 초기화
dp[0][0] = [0,INF]
for j in range(1,len(l)+1):
  dp[0][j][1] = 1 
  dp[0][j][0] = INF 
# for i in range(len(o)+1):
#   dp[i][0][0] = -1 

# #2. 점화식 
for i in range(len(o)) :
  for j in range(i+1):
    dp[i+1][j][0] = dp[i+1][j][1] = INF
  for j in range(i, len(l)):
    if o[i] == l[j] :
      dp[i+1][j+1][0] = min(dp[i][j][0] , dp[i][j][1])
    else : 
      dp[i+1][j+1][0] = INF 
    dp[i+1][j+1][1] = min(dp[i+1][j][0] +1 , dp[i+1][j][1])
#3. 출력
if min(dp[-1][-1][0],dp[-1][-1][1]) >= INF : 
  print(-1)
else :
  print(min(dp[-1][-1][0] , dp[-1][-1][1]))