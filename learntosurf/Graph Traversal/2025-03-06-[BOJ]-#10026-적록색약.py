import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]

# 방향 벡터 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color, visited, grid):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_regions(grid, is_color_blind):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  # 방문하지 않은 경우 BFS 탐색 시작
                count += 1
                color = grid[i][j]

                # 적록색약 모드라면 R과 G를 동일하게 처리
                if is_color_blind and color in "RG":
                    bfs(i, j, "R", visited, grid)
                else:
                    bfs(i, j, color, visited, grid)
    
    return count

# 적록색약이 아닌 경우
normal_count = count_regions(grid, is_color_blind=False)

# 적록색약인 경우 (R과 G를 동일하게 처리한 grid 생성)
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

color_blind_count = count_regions(grid, is_color_blind=True)

print(normal_count, color_blind_count)