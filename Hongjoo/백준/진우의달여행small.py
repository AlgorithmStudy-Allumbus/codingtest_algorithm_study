"""
https://www.acmicpc.net/problem/17484

# 문제
- N x M 행렬
1. 이동 방향 - 최하 , 하 , 우하
2. 2번 연속 동일 방향 선택 불가
3. 반드시 달 도착
goal )  최소 연료 


"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * m for _ in range(n)] for _ in range(3)]		# 3차원배열 DP
ans = sys.maxsize											# 임의의 큰 값

for z in range(3):
    for y in range(m):
        dp[z][0][y] = board[0][y]							# 초기 DP 초기화

for x in range(1, n):
    for y in range(m):
        if y == 0:		
        	# 가장 첫 번째 열인 경우
        	# 대각선 왼쪽 방향(dp[0])의 경우, 바로 위에서 아래 방향으로 진행하는 값만 받을 수 있음
            # 아래 방향(dp[1])의 경우, 오른쪽 위에서 왼쪽 아래 방향으로 진행하는 값만 받을 수 있음
            # 대각선 오른쪽 방향(dp[2])의 경우, 오른쪽 위에서 대각선 왼쪽 진행하는 값과 바로 위에서 아래 방향으로 진행하는 값만 받을 수 있음
            # dp[0][x][y] = dp[1][x - 1][y]
            dp[1][x][y] = dp[0][x - 1][y + 1]
            dp[2][x][y] = min(dp[0][x - 1][y + 1], dp[1][x - 1][y])
        elif y == m - 1:
        	# 가장 마지막 열인 경우
            # 대각선 왼쪽 방향(dp[0])의 경우, 바로 위에서 아래 방향으로 진행하는 값과 왼쪽 위에서 대각선 오른쪽 방향으로 진행하는 값만 받을 수 있음
            # 아래 방향(dp[1])의 경우, 왼쪽 위에서 오른쪽 아래 방향으로 진행하는 값만 받을 수 있음
            # 대각선 오른쪽 방향(dp[2])의 경우, 바로 위에서 아래 방향으로 진행하는 값만 받을 수 있음
            dp[0][x][y] = min(dp[1][x - 1][y], dp[2][x - 1][y - 1])
            dp[1][x][y] = dp[2][x - 1][y - 1]
            # dp[2][x][y] = dp[1][x - 1][y]
        else:
        	# 중간 열인 경우
            # 대각선 왼쪽 방향(dp[0])의 경우, 바로 위에서 아래 방향으로 진행하는 값과 왼쪽 위에서 대각선 오른쪽 방향으로 진행하는 값만 받을 수 있음
            # 아래 방향(dp[1])의 경우, 오른쪽 위에서 대각선 왼쪽 방향으로 진행하는 값과 왼쪽 위에서 대각선 오른쪽 방향으로 진행하는 값만 받을 수 있음
            # 대각선 오른쪽 방향(dp[2])의 경우, 오른쪽 위에서 대각선 왼쪽 방향으로 진행하는 값과 바로 위에서 아래 방향으로 진행하는 값만 받을 수 있음
            dp[0][x][y] = min(dp[1][x - 1][y], dp[2][x - 1][y - 1])
            dp[1][x][y] = min(dp[0][x - 1][y + 1], dp[2][x - 1][y - 1])
            dp[2][x][y] = min(dp[0][x - 1][y + 1], dp[1][x - 1][y])

        for z in range(3):	# 원래 자신의 좌표값 더함
            dp[z][x][y] += board[x][y]

for z in range(3):			# 3차원 배열 중 마지막 행의 최솟값을 찾음
    ans = min(ans, min(dp[z][-1]))

print(ans)