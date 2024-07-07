from collections import deque


def bfs(graph, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0, 1)])  # (x, y, distance)
    visited[0][0] = 1

    while queue:
        x, y, dist = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]

            if 0 <= row < n and 0 <= col < m and visited[row][col] == 0 and graph[row][col] == 1:
                visited[row][col] = 1
                queue.append((row, col, dist + 1))

    return -1  # 목적지에 도달할 수 없는 경우


n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]

for _ in range(n):
    line = input()
    graph.append([int(char) for char in line])

min_answer = bfs(graph, visited)

print(min_answer)
