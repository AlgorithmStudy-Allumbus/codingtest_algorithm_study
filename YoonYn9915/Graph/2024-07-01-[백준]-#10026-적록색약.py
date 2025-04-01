from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, visited):
    border = 0
    queue = deque()

    # 영역 개수 계산
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 현재 칸을 아직 방문하지 않았다면 현재 칸부터 bfs 탐색 시작
            if visited[i][j] == 0:
                # 영역 개수 한 개 증가
                border += 1
                queue.append((i, j))

                while queue:
                    (x, y) = queue.popleft()
                    # 방문처리
                    visited[x][y] = 1

                    # 상하좌우 인접한 칸으로 이동
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        # 칸이 보드 밖으로 넘어가지 않았는지,인접한 칸이 같은 색인지,아직 방문하지 않았는지 확인
                        if (1 <= nx <= N and 1 <= ny <= N) and graph[x][y] == graph[nx][ny] and visited[nx][ny] == 0:
                            # 해당 칸 방문처리
                            queue.append((nx, ny))
                            visited[nx][ny] = 1

    return border


# 입력받기
N = int(input())
graph = [[0] * (N + 1)]
visited = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N):
    graph.append([0] + list(input()))

# 정상인이 보는 영역 개수 반환
num_of_normal = bfs(graph, visited)

# 적록색약이 보는 영역 개수 반환 적록색약은 R,G를 구분하지 못하므로 모든 R을 G로 변환
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[0] * (N + 1) for _ in range(N + 1)]
num_of_abnormal = bfs(graph, visited)

print(f"{num_of_normal} {num_of_abnormal}")
