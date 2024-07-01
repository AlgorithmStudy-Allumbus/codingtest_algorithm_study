from collections import deque

# 지도(2차원 배열)에서 섬을 탐색하기 위한 bfs
def bfs(x, y):

    # 탐색범위가 현재 노드 기준 가로, 세로, 대각선이므로 총 8가지
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    queue.append((x, y))
    visited[x][y] = 1

    # queue가 존재하면
    while queue:

        # queue에서 pop해서
        x, y = queue.popleft()

        #가로, 세로 대각선에 있는 노드가 다음 세가지 조건을 만족하는지 검사
        # 탐색 조건
        # 1. 현재 노드가 배열의 인덱스 범위 안인지 0 <= row < h and 0 <= col < w
        # 2. 땅인지 (arr값이 1인지)
        # 3. 방문하지 않았는지
        for k in range(8):
            row = x + dx[k]
            col = y + dy[k]

            if 0 <= row < h and 0 <= col < w and arr[row][col] == 1 and visited[row][col] == 0:
                queue.append((row, col))
                visited[row][col] = 1


answer = deque()
queue = deque()

while True:
    w, h = map(int, input().split())
    if h == 0 and w == 0:
        break

    visited = [[0] * w for _ in range(h)]
    arr = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                ans += 1

    answer.append(ans)

for ans in answer:
    print(ans)
