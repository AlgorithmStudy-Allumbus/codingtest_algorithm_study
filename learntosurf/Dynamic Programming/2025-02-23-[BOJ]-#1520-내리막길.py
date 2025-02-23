import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 도착점에 도달하면 경로 1개 반환
    if x == M - 1 and y == N - 1:
        return 1
    
    # 이미 방문한 적이 있다면 저장된 경로 개수 반환
    if dp[x][y] != -1:
        return dp[x][y]

    # 현재 위치에서 가능한 경로 개수 계산
    dp[x][y] = 0  # 초기화
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] < graph[x][y]:  # 내리막길 조건
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

# 입력 처리
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

# DP 배열 (-1로 초기화)
dp = [[-1] * N for _ in range(M)]

H = dfs(0, 0)
print(H)