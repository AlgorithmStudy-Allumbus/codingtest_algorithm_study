'''
1. 아이디어
- 상이 왕에게 도달할 수 있는 최소 횟수를 구하기 위해 장기판을 그래프로 놓고 상이 갈 수 있는 위치를 bfs로 탐색한다.

2. 시간복잡도
- BFS 시간복잡도 O(V + E), V는 10 * 9 , E는 최대 4 * 10 * 9.

3. 구현
3.1 입력받기
3.2 상의 초기 위치에서부터 8가지 방향으로 나아가며 bfs 실행.
3.3 이동 경로에 왕이 있으면 이동 불가
3.4 bfs가 끝나기 전에 왕의 위치에 도달하면 이동횟수 출력, 도달하지 못하면 -1 출력
'''

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