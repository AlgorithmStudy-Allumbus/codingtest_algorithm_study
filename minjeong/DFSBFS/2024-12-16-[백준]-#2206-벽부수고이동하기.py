from collections import deque

# 입력 받기
N, M = map(int, input().split())
maps = []
for _ in range(N):
    temp = input().strip()
    maps.append(list(map(int, temp)))

# 방문 배열 초기화
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
# visited[x][y][0] = 벽을 뚫지 않고 온 최단 경로
# visited[x][y][1] = 벽을 1회 뚫고 온 최단 경로

# BFS 탐색 방향 (상, 우, 하, 좌)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# BFS 큐 초기화
queue = deque([(0, 0, 0)])

# BFS 시작
while queue:
    x, y, wall = queue.popleft()

    # 목표 지점 도달 시 최단 거리 출력
    if x == N - 1 and y == M - 1:  # 목표지점에 도달했다면
        print(visited[x][y][wall])
        exit(0)

    # 네 방향 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 맵 범위를 벗어난 경우 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 벽이고 벽 파괴를 아직 안 쓴 경우, 벽 부수기 가능. 값을 업데이트하고 큐에 추가
        if maps[nx][ny] == 1 and wall == 0:
            visited[nx][ny][1] = visited[x][y][0] + 1
            queue.append((nx, ny, 1))
        # 벽이 아니고, 아직 방문하지 않았을 경우에는 이동 가능하므로 큐에 추가
        elif maps[nx][ny] == 0 and visited[nx][ny][wall] == 0:
            visited[nx][ny][wall] = visited[x][y][wall] + 1
            queue.append((nx, ny, wall))

# 도달하지 못한 경우 -1 출력
print(-1)