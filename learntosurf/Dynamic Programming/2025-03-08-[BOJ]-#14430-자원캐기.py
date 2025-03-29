import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = grid[0][0]

def max_resources(N, M, grid):
    # 첫 번째 행 채우기
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # 첫 번째 열 채우기
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # DP 테이블 채우기
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[N-1][M-1]

print(max_resources(N, M, grid))
