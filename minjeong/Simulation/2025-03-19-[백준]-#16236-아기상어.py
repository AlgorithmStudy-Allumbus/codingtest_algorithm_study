import sys
from collections import deque
input = sys.stdin.readline

def bfs(sx, sy, shark_size):
    # 방문 배열과 거리 기록
    visited = [[-1]*n for _ in range(n)]
    visited[sx][sy] = 0
    queue = deque([(sx, sy)])
    fishes = [] # 먹을 수 있는 물고기 후보들

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 새로운 좌표가 공간 내에 있고 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 이동 가능한 칸: 빈 칸이거나, 물고기가 있어도 크기가 shark_size 이하인 경우
                if space[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    # 먹을 수 있는 물고기: 값이 0이 아니고 아기 상어 크기보다 작은 경우
                    if 0 < space[nx][ny] < shark_size:
                        fishes.append((visited[nx][ny], nx, ny))
                    queue.append((nx, ny))
    if not fishes:
        return None     # 먹을 수 있는 물고기가 없음

    # 문제 조건대로 정렬: 거리, 행, 열, 순
    fishes.sort(key=lambda x: (x[0], x[1], x[2]))
    return fishes[0]    # 가장 적합한 물고기


n = int(input())    # 공간의 크기
space = []          # 공간의 상태
for _ in range(n):
    space.append(list(map(int, input().split())))


# 아기상어 위치 구하기
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            sx, sy = i, j
space[sx][sy] = 0   # 아기 상어의 시작 위치는 빈 칸(0)으로 처리

# 초기 설정
shark_size = 2  # 아기 상어 초기 크기
eaten = 0       # 먹은 물고기 수
time = 0        # 전체 소요시간
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# 시뮬레이션 수행
while True:
    result = bfs(sx, sy, shark_size)
    if result is None:  # 먹을 수 있는 물고기가 없으면 종료
        break

    dist, fx, fy = result   # 먹을 수 있는 물고기의 거리와 위치
    time += dist        # 이동 시간 추가
    sx, sy = fx, fy     # 아기 상어 위치 이동
    space[sx][sy] = 0   # 물고기를 먹었으므로 해당 칸을 빈 칸으로 만들기
    eaten += 1# 먹은 물고기 수

    # 먹은 물고기 수가 현재 아기 상어 크기와 같으면 크기를 1 증가
    if eaten == shark_size:
        shark_size += 1
        eaten = 0

print(time)
