import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

# 방향벡터
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(x, y):
    # 깊이 탐색을 하며 안전 영역 탐색
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and \
                not visited[nx][ny] and map[nx][ny] > h:
            dfs(nx, ny)


N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
max_height = 0

# 맵 내의 최대값 구하기
for m in map:
    max_height = max(max_height, max(m))

answer = 0

for h in range(0, max_height + 1): # 물이 잠기지 않는 상황을 고려하여 0부터 시작
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            # 아직 방문하지 않았고 h(높이) 이상인 지점이라면 DFS 탐색을 한다.
            if not visited[i][j] and map[i][j] > h:
                dfs(i, j)
                count += 1 # DFS 탐색을 마치면 하나의 안전 영역이므로 count

    answer = max(answer, count) # 안전영역 최대 개수 계산

print(answer)