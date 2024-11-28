import sys 
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
blocks = input().split()

dp = [INF] * N
dp[0] = 0 # 1번 블록에서 출발 

for i in range(1, N):
    for j in range(i):
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