from collections import deque

# 2차원 배열을 이용한 bfs 구현
def bfs(x, y):

    # 2차원 배열에서 현재 노드의 상하좌우를 검사하기 위한 dx와 dy
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    # queue를 이용한 bfs 그래프 탐색
    queue.append((x, y))
    visited[x][y] = 1


    while queue:
        (x, y) = queue.popleft()

        # queue에서 pop한 현재 노드를 기준으로 상하좌우 탐색
        for k in range(4):
            row = x + dx[k]
            col = y + dy[k]

            # 탐색 조건
            # 1. 현재 노드가 배열의 인덱스 범위 안인지 0 <= x < n and 0 <= y < n
            # 2. 같은 색인지
            # 3. 방문하지 않았는지
            if 0 <= row < n and 0 <= col < n:
                if arr[x][y] == arr[row][col] and visited[row][col] == 0:
                    queue.append((row, col))
                    visited[row][col] = 1


# 초기값 세팅
n = int(input())
visited = [[0] * n for _ in range(n)]
arr = [list(input()) for _ in range(n)]
queue = deque()

# 적록색약이 아닌 경우의 답
answerForNormal = 0

# 적록색약인 경우의 답
answerForColorBlindness = 0


# 적록색약이 아닌 경우
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            answerForNormal += 1


# 적록색약인 경우 R과 G는 같으므로

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            answerForColorBlindness += 1

print(answerForNormal, answerForColorBlindness)
