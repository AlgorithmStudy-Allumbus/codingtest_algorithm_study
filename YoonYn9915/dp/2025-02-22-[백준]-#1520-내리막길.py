import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
n, m = map(int, input().split())
graph = []

moves = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

visited = [[-1] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    # Base Case
    if x == n - 1 and y == m - 1:
        return 1

    # 이미 방문한 곳일 때
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for move in moves:
        nx, ny = x + move[0], y + move[1]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[x][y] > graph[nx][ny]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]


print(dfs(0, 0))