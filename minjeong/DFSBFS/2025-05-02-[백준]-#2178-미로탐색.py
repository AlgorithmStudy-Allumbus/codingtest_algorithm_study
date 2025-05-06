import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

def bfs(x, y):
    # 방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이면 무시
            if graph[nx][ny] == 0:
                continue

            # 이동 가능한 칸이면 거리 갱신 후 방문 처리
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

print(bfs(0, 0))
