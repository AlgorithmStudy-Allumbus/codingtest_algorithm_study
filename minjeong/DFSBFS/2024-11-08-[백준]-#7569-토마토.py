import sys
from collections import deque

input = sys.stdin.readline

# 상자의 가로 m, 세로 n, 높이 h
m, n, h = map(int, input().split())
tomatoes = []

for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(n)]
    tomatoes.append(layer)


# 상하좌우앞뒤 방향
directions = [(0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)] # 상하좌우앞뒤

def bfs():
    queue = deque() # (층, 행, 열, 일수)

    # 초기 익은 토마토 위치 큐에 추가
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if tomatoes[z][x][y] == 1:
                    queue.append((z, x, y, 0))  # (층, 행, 열, 일수)

    max_day = 0  # 익는 데 걸린 최대 일수 추적

    while queue:
        z, x, y, day = queue.popleft()
        max_day = max(max_day, day)  # 가장 오래 걸린 일수 갱신

        for dz, dx, dy in directions:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if tomatoes[nz][nx][ny] == 0:  # 익지 않은 토마토일 때
                    tomatoes[nz][nx][ny] = 1
                    queue.append((nz, nx, ny, day + 1))  # 익는 데 하루 추가


    return max_day

def all_ripe():
    # 모든 토마토가 익었는지 확인
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatoes[i][j][k] == 0:
                    return False
    return True

# 초기 상태 확인
if all_ripe():
    print(0)
    exit(0)
else:
    days = bfs()

    # 모든 토마토가 익었는지 다시 확인
    if all_ripe():
        print(days)
    else:
        print(-1)

