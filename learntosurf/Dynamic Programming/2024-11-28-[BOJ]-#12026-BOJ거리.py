import sys 
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
blocks = input().split()

dp = [INF] * N
dp[0] = 0 # 1번 블록에서 출발 

for i in range(1, N): # 목표 블록 (1번 블록 이후부터 N번까지)
    for j in range(i): # 이전 블록들 (0번부터 i-1번까지 탐색)
        if blocks[j] == 'B' and blocks[i] != 'O':
            continue
        elif blocks[j] == 'O' and blocks[i] != 'J':
            continue
        elif blocks[j] == 'J' and blocks[i] != 'B':
            continue
        dp[i] = min(dp[i], dp[j] + (i-j)**2)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])