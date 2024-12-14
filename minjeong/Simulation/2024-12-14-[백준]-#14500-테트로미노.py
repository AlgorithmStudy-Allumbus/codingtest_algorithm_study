n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최댓값 저장 변수
max_value = 0


# DFS 탐색 (ㅗ 모양 제외)
def dfs(x, y, count, total):
    global max_value
    # 테트로미노 4칸 채웠을 경우
    if count == 4:
        max_value = max(max_value, total)
        return

    # 상하좌우 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 내에 있고, 방문하지 않은 경우
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, total + graph[nx][ny])
            visited[nx][ny] = False  # 백트래킹


# ㅗ 모양 탐색
def check_t_shape(x, y):
    global max_value
    # 중심 기준 4방향 중 3개를 선택 (ㅗ, ㅜ, ㅏ, ㅓ)
    for i in range(4):
        total = graph[x][y]
        for j in range(3):  # 현재 제외한 3방향 탐색
            k = (i + j) % 4
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                total += graph[nx][ny]
            else:  # 범위를 벗어나면 ㅗ 모양이 성립하지 않음
                break
        else:  # 모든 3방향 탐색이 유효한 경우
            max_value = max(max_value, total)


# 모든 좌표에서 테트로미노 탐색
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])  # DFS 시작
        visited[i][j] = False
        check_t_shape(i, j)  # ㅗ 모양 탐색

# 결과 출력
print(max_value)
