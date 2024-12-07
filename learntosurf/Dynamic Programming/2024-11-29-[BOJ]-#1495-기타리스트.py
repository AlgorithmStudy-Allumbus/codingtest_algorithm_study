import sys
input = sys.stdin.readline

N,S,M = map(int,input().split())
V = list(map(int,input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1 # 시작 볼륨을 설정 

for i in range(1, N+1): # 각 곡에 대해
    for j in range(M+1): # 가능한 볼륨에 대해
        if dp[i-1][j] != 0: # 이전 곡에서 해당 볼륨이 가능하다면
            if 0 <= j + V[i-1] <= M: # 볼륨을 올릴 수 있다면
                dp[i][j + V[i-1]] = 1
            if 0 <= j - V[i-1] <= M: # 볼륨을 낮출 수 있다면
                 dp[i][j-V[i-1]] = 1
volume = -1
for i in range(M, -1, -1): # 최대 볼륨부터 탐색
    if dp[N][i] == 1: # 가능한 볼륨을 찾으면 
        volume = i
        break
    
print(volume)