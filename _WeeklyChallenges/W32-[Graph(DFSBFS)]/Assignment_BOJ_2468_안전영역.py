"""
BOJ #2468. 안전 영역 (실버2)
https://www.acmicpc.net/problem/2468
유형: Graph, DFS, BFS
"""

"""
DFS 풀이
"""
import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(x, y):
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and \
                not visited[nx][ny] and map[nx][ny] > h:
            dfs(nx, ny)


N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
max_height = 0

# 맵 내의 최대값 구하기
for m in map:
    max_height = max(max_height, max(m))

answer = 0

for h in range(0, max_height + 1): # 물이 잠기지 않는 상황을 고려하여 0부터 시작한다.
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and map[i][j] > h:
                dfs(i, j)
                count += 1

    answer = max(answer, count)

print(answer)

"""
BFS 풀이
"""
from collections import deque

n = int(input())
graph = []
maxNum = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


result = 0
for i in range(maxNum):
    visited = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)