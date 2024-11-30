'''
BOJ #17845. 수강과목 (골드5)
https://www.acmicpc.net/problem/17845
유형: DP, 배낭문제
'''
import sys
input = sys.stdin.readline

n, k = list(map(int, input().rstrip().split())) # n은 최대 공부 시간, k는 과목 수
info = [0] + [list(map(int, input().rstrip().split())) for _ in range(k)]
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1): # i는 현재 고른 과목 수
    for j in range(1, n + 1): # j는 최대 시간
        if j < info[i][1]: # 시간이 넘친다면
            dp[i][j] = dp[i - 1][j] # 해당 과목은 제외
        else: # 시간이 넘치지 않는다면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - info[i][1]] + info[i][0]) # 해당 과목 제외한거 vs 해당 과목 중요도 + (해당 과목 제외) 해당 과목의 시간을 뺀 중요도

print(dp[k][n])
