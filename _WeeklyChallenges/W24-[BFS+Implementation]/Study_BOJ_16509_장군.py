"""
BOJ #16509. 장군 (골드 5)
https://www.acmicpc.net/problem/16509
유형: BFS + Implementation
"""

from collections import deque

# 입력 받기
R1, C1 = map(int, input().split())  # 상의 시작 위치
R2, C2 = map(int, input().split())  # 왕의 위치

# 방문 여부를 -1로 초기화 (10행 x 9열)
visited = [[-1] * 9 for _ in range(10)]
visited[R1][C1] = 0  # 시작 위치는 0으로 표시

# 상의 8가지 이동 방향 및 그에 따른 경유 좌표 정의
# 각각: 경유1, 경유2, 최종 목적지 (총 3단계 이동)
paths = [
    [(-1, 0), (-2, -1), (-3, -2)],
    [(-1, 0), (-2, 1), (-3, 2)],
    [(1, 0), (2, -1), (3, -2)],
    [(1, 0), (2, 1), (3, 2)],
    [(0, -1), (-1, -2), (-2, -3)],
    [(0, -1), (1, -2), (2, -3)],
    [(0, 1), (-1, 2), (-2, 3)],
    [(0, 1), (1, 2), (2, 3)],
]

# 이동 경로에 왕이 있는지 확인
def check(x, y, i):
    for dx, dy in paths[i][:2]:  # 경유지 두 곳만 확인
        mx, my = x + dx, y + dy
        if mx == R2 and my == C2:
            return False
    return True

# BFS로 최소 이동 횟수 찾기
def bfs():
    queue = deque([(R1, C1)])

    while queue:
        x, y = queue.popleft()

        # 왕의 위치에 도달한 경우
        if x == R2 and y == C2:
            print(visited[x][y])
            return

        for i in range(8):
            nx = x + paths[i][2][0]
            ny = y + paths[i][2][1]

            # 범위 안이고, 방문하지 않았으며, 경로에 왕이 없다면
            if 0 <= nx < 10 and 0 <= ny < 9 and visited[nx][ny] == -1 and check(x, y, i):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    # 도달할 수 없는 경우
    print(-1)

bfs()