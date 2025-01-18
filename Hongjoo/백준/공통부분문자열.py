"""
https://www.acmicpc.net/problem/5582
# 유형 : dp , LCS(longest common sequence)
LCSubstring 특징
1. 무조건 "연속된" 공통 문자열 -> 한번이라도 다르면 dp =0로 초기화,
LCS(subsequence)
- 부분수열은 연속된 값이 아님 -> 최대 공통부분수열은 계속 유지됨
조건
- 한글자씩 비교함
(1) x[j] == y[i] 같으면 -> dp[i][j] = max(대각선 +1 , 위) => dp
(2) 다르면 ->0 ()

"""
import sys
x = list(sys.stdin.readline())[:-1]
y= list(sys.stdin.readline())[:-1]
dp = [[0 for _ in range(len(y))] for j in range(len(x))]

#2. Dp , LCS(longest-common-sequence)

for i in range(len(x)) :
  for j in range(len(y)) :

    if i== 0 or j== 0 : 
      if x[i] == y[j] : # 예외 처리 
        dp[i][j] =1
      continue    
    if x[i] == y[j] : 
      dp[i][j] =dp[i-1][j-1] +1 
    else : 
      dp[i][j] = 0 #dp[i-1][j]

#3. answer이 꼭 뒤로 오지 않음
answer = 0 
for i in range(len(x)):
  print(dp[i])
  answer = max(max(dp[i]),answer)

print(answer)