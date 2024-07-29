import sys
from collections import deque
input = sys.stdin.readline

# 목표지점까지의 거리 구하기
def find_distance_to_goal(n, m, grid):
    # 거리배열(모든 지점에 대한 거리를 저장)
    distances = [[-1 for _ in range(m)] for _ in range(n)]

    # 목표지점 찾기
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:     # 목표지점의 위치 저장하고, 0으로 설정
                target_x = i
                target_y = j
                distances[i][j] = 0
            if grid[i][j] == 0:     # 땅이 아닌 곳이므로 0으로 설정
                distances[i][j] = 0

    queue = deque([(target_x, target_y)])           # 큐 초기화
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 방향 리스트

    # BFS 탐색
    while queue:
        x, y = queue.popleft()      # 현재지점 pop
        for dx, dy in directions:
            nx, ny = x + dx, y + dy # 현재 지점에서 상하좌우 인접한 지점
            # 인접한 지점이 지도의 범위 안에 있고, 갈 수 있는 땅(값이 1)이며, 아직 방문하지 않은 지점이라면:
            if (0 <= nx < n and 0 <= ny < m) and grid[nx][ny] == 1 and distances[nx][ny] == -1:
                    distances[nx][ny] = distances[x][y] + 1 # 인접한 지점의 거리를 현재 지점의 거리 + 1로 설정
                    queue.append((nx, ny))                  # 인접한 지점을 큐에 추가

    return distances

# 초기화
n, m = map(int, input().split())    # n: 세로, m: 가로
grid = []                           # 지도
for _ in range(n):
    line = list(map(int, input().split()))
    grid.append(line)

# 함수 호출
distances = find_distance_to_goal(n, m, grid)

# 정답 출력
for d in distances:
    print(" ".join(map(str, d))) # 공백을 구분하여 출력
