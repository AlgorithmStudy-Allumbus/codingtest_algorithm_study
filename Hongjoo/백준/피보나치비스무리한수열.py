"""
#피보나치 비스무리한수열 / 실버 5
https://www.acmicpc.net/problem/14495
- 조건 : 1< n <=116

# 문제 유형 : DP
1. 입력
2. dp 생성
dp[1<idx <=n] = [1,1,1...f(n)]
-초기화 : dp[1]=dp[2]=dp[3] = 1 

3. 점화식 
f(n) = f(n-1) + f(n-3)
- dp에 저장하기
- dp에 있으면 호출, 없으면 계산 & dp에 업데이트 
"""
#1. 입력 변수 저장
N = int(input())
#2. dp 생성 & 초기화
dp = [ 0 for _ in range(116+1)]


#3. 점화식 
for i in range(0,N+1) :
  if i in [0,1,2,3] :
    dp[i] = 1
  elif dp[i] == 0 : # i>=4, dp에 없으면 -> 업데이트
   
    dp[i] = dp[i-1] + dp[i-3]

print(dp[N])