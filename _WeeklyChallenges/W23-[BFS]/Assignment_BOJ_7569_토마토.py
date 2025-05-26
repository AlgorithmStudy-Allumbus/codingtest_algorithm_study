"""
BOJ #7569. 토마토 (3차원) (골드5)
https://www.acmicpc.net/problem/7569
유형: Graph, BFS
"""

"""
풀이1
"""
import sys
from collections import deque
input = sys.stdin.readline

# 1. 입력 처리
M, N, H = map(int, input().split()) # 가로, 세로, 높이
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 2. 초기 변수 설정
queue = deque([])
directions = [(-1, 0, 0), (0, 1, 0), (1, 0, 0), (0, -1, 0),
              (0, 0, 1), (0, 0, -1)]    # 위-오른쪽-아래-왼쪽-앞-뒤
day = 0                                 # 정답으로 반환할 변수

# 3. 초기 익은 토마토를 큐에 추가하기
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

# 4. BFS 탐색
while queue:
    z, y, x = queue.popleft()

    for dx, dy, dz in directions:
        nx, ny, nz = x + dx, y + dy, z + dz
        # 범위 내에 있고 아직 안 익은 토마토라면
        if (0 <= nx < M and 0 <= ny < N and 0 <= nz < H) and (box[nz][ny][nx] == 0):
            box[nz][ny][nx] += box[z][y][x] + 1  # 익은 날짜 누적 갱신
            queue.append((nz, ny, nx))

# 5. 정답 구하기
for height in box:
    for row in height:
        for tomato in row:
            # 안 익은 토마토가 남아있는지 여부 확인
            if tomato == 0:
                print(-1)
                exit()
        # 익는데 걸린 최대 일수 추적
        day = max(day, max(row))

# 6. 정답 출력
print(day - 1)


"""
풀이2
"""
import sys
from collections import deque

input = sys.stdin.readline

# 상자의 가로 m, 세로 n, 높이 h
m, n, h = map(int, input().split())
tomatoes = []

for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(n)]
    tomatoes.append(layer)

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

'''
1: 익은 토마토
0: 익지 않은 토마토
-1: 토마토가 없음
'''
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

