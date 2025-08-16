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