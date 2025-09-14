"""
[BOJ]#9251.LCS / DP /Gold5/ 2025.09.09
https://www.acmicpc.net/problem/9251
#####

"""
import sys
input = sys.stdin.readline
# 1. 입력 변수 - a 문자열 / b문자열
a = list(input())[:-1]
b= list(input())[:-1]
# LCS 행렬 0 초기화
lcs = [[0]*(len(b)+1) for _ in range(len(a)+1)]

#2. LCS (Longest Common Subsequence) 점화식
"""
i. a[i] VS b[j] 문자 비교하기
  (1) SAME(=) -> dp[i][j] = 위쪽 대각선 +1 
  (2) DIFF(!=) -> dp[i][j] = MAX(왼쪽 , 위쪽)

ii. 최종 LCS = dp[-1][-1]
"""
for i in range(1,len(a)+1) :
  for j in range(1, len(b)+1) :
    if a[i-1] == b[j-1]:
      lcs[i][j] = lcs[i-1][j-1] + 1
    else :
      lcs[i][j] = max(lcs[i-1][j] , lcs[i][j-1])

# print(lcs)
print(lcs[-1][-1])