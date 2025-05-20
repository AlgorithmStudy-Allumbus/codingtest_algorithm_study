import sys
from collections import deque
input = sys.stdin.readline

# 1. 입력 처리
M, N = map(int, input().split())                            # 가로 칸 수, 세로 칸 수
box = [list(map(int, input().split())) for _ in range(N)]   # 토마토

# 2. 초기 설정
queue = deque([])                               # 큐
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 방향벡터
day = 0                                         # 정답이 담길 변수

# 3. 큐에 초기 익은 토마토 위치 저장
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

# 4. BFS 탐색
while queue:
    # 처음 토마토 꺼내기
    x, y = queue.popleft()

    # 처음 토마토의 인접한 토마토 찾기
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 범위 내에 있고, 토마토가 익지 않은 경우
        if (0 <= nx < N and 0 <= ny < M) and (box[nx][ny] == 0):
            # 익히고 1 더해주며 횟수 세기
            # 여기서 나온 제일 큰 값이 정답이 된다.
            box[nx][ny] += box[x][y] + 1  # 일수 누적
            queue.append((nx, ny))


# 5. 정답 구하기
for row in box:
    for tomato in row:
        # 모두 탐색했지만 토마토가 모두 익지 않았다면 -1 출력
        if tomato == 0:
            print(-1)
            exit()

    # 다 익혔다면 최댓값이 정답
    day = max(day, max(row))

# 6. 정답 출력
print(day - 1) # 처음에 1로 익은 토마토를 표현했으니 1을 빼준다.