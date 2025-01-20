"""
백준 #20542. 받아쓰기/DP /골드5
https://www.acmicpc.net/problem/20542

(1) 문자가 같음 -> 대각선 = 현위치
(2) 다른 문자
  min (왼쪽[add] , 대각선[edit] , 위) +1
"""
import sys
N , M = map(int, sys.stdin.readline().split())
predict =list(*map(str,sys.stdin.readline().split()))
gt = list(*map(str,sys.stdin.readline().split()))
print(predict , gt)
# predict -> gt
dp = [[0 for _ in range(len(gt)+1)] for k in range(len(predict)+1)]
dp[0] = list(range(len(gt)+1))
print(dp)
for i in range(1,len(predict)+1):
  for j in range(len(gt)+1) :
    # 초기화
    if j==0 : 
      dp[i][j] = dp[i-1][j]+ 1 # 위 +1
      continue
    
    # dp 채우기 
    if predict[i] == gt[j]:
      dp[i][j] = dp[i-1][j-1]
      print(f"samep { dp}")
    else :
      dp[i][j] = 1 + min(dp[i-1][j-1] , dp[i][j-1] , dp[i-1][j])
    
print(dp)