
from collections import deque

def bfs(places, i, j, k):
    queue = deque()
    queue.append((j, k, 0))  # row, col, dist
    visited = [[False] * 5 for _ in range(5)]
    visited[j][k] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        row, col, dist = queue.popleft()

        if dist != 0 and places[i][row][col] == 'P':
            return 1

        if dist == 2:
            continue

        for d in range(4):
            nr = row + dx[d]
            nc = col + dy[d]

            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                if places[i][nr][nc] != 'X':
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

    return 0


def solution(places):
    answer = []

    for i in range(5):  # 5 rooms
        violated = False
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    if bfs(places, i, j, k):
                        violated = True
                        break
            if violated:
                break
        answer.append(0 if violated else 1)

    return answer


