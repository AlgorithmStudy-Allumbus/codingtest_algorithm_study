import sys
from collections import deque

input = sys.stdin.readline

# 1. 상과 왕 초기 위치
s_r, s_c = map(int, input().split())  # 상의 위치
k_r, k_c = map(int, input().split())  # 왕의 위치

# 장기판 (10x9)
grid = [[0 for _ in range(9)] for _ in range(10)]
visited = [[False for _ in range(9)] for _ in range(10)]

# 8가지 이동 경로
directions = [
    # 상
    ((-1, 0), (-1, 1), (-1, 1)),  # 오른쪽 위
    ((-1, 0), (-1, -1), (-1, -1)),  # 왼쪽 위
    # 하
    ((1, 0), (1, 1), (1, 1)),  # 오른쪽 아래
    ((1, 0), (1, -1), (1, -1)),  # 왼쪽 아래
    # 좌
    ((0, -1), (-1, -1), (-1, -1)),  # 왼쪽 위
    ((0, -1), (1, -1), (1, -1)),  # 왼쪽 아래
    # 우
    ((0, 1), (-1, 1), (-1, 1)),  # 오른쪽 위
    ((0, 1), (1, 1), (1, 1))  # 오른쪽 아래
]


def bfs():
    queue = deque([(s_r, s_c)])  # 상 위치부터 시작

    while queue:
        r, c = queue.popleft()

        # 왕에게 도달한 경우
        if (r, c) == (k_r, k_c):
            return grid[r][c]

        for d1, d2, d3 in directions:
            nr1, nc1 = r + d1[0], c + d1[1]
            nr2, nc2 = nr1 + d2[0], nc1 + d2[1]
            nr3, nc3 = nr2 + d3[0], nc2 + d3[1]

            if (0 <= nr3 < 10 and 0 <= nc3 < 9) and not visited[nr3][nc3]:
                if (nr1, nc1) == (k_r, k_c) or (nr2, nc2) == (k_r, k_c):
                    # 경로에 왕이 있다면 못 감
                    continue

                visited[nr3][nc3] = True
                grid[nr3][nc3] += grid[r][c] + 1
                queue.append((nr3, nc3))

    return -1  # 도달 불가


print(bfs())