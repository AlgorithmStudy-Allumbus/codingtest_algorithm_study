import sys 
input = sys.stdin.readline

S1 = list(input().strip())
S2 = list(input().strip()) 
n, m = len(S1), len(S2)

dp = [[0] * (m+1) for _ in range(n+1)]

max_len = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        # 문자열 S1과 S2의 현재 위치의 문자를 비교
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 # 이전 공통 부분 문자열에 현재 문자를 추가하여 길이를 연장 
            max_len = max(max_len, dp[i][j])
        else:
            dp[i][j] = 0 # 다르면 공통 부분 문자열이 끊어짐 

print(max_len)
