import sys
input = sys.stdin.readline

t = int(input()) #테스트케이스의 수
dp = [1] * 101
for __ in range(t): # 테스트케이스 수만큼 반복
    p_n = int(input()) # 테스트케이스 입력
    for i in range(4, p_n+1): #4부터 시작
        dp[i] = dp[i-3] + dp[i-2] # 점화식
    print(dp[p_n])
    