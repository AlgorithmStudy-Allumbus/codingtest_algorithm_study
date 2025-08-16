import sys
from collections import deque
input = sys.stdin.readline

# 방향 벡터: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 0  # 방문 처리
    house_count = 1  # 단지 내 집 수

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우 탐색
            nx, ny = x + dx[i], y + dy[i]

            # 좌표가 유효한지 확인
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
                house_count += 1
    return house_count

# 입력
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

result = []

# 모든 좌표 순회하며 BFS 수행
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

# 결과 출력
result.sort()
print(len(result))
for count in result:
    print(count)
