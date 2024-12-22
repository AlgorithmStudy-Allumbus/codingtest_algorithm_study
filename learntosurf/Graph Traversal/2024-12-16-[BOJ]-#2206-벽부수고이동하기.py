from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 상하좌우 방향 정의 
directions = [(-1,0), (0,1), (1,0), (0,-1)]

# BFS
def bfs():
    # 3차원 방문 배열: visited[x][y][벽 부숨 여부]
    # wall=0: 벽을 부수지 않고 도달한 경우 
    # wall=1: 벽을 한번 부수고 도달한 경우 
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque([(0,0,0)]) # (x, y, 벽 부순 여부)
    visited[0][0][0] = 1 # 시작점 방문처리 (벽을 부수지 않고)
    
    while queue:
        x, y, wall = queue.popleft()
    
        # 도착지에 도달한 경우 거리 반환 
        if x == N-1 and y == M-1: 
            return visited[x][y][wall]
        
        # 4가지 방향 탐색 
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵 범위 안에 있는 경우만 처리 
            if 0 <= nx < N and 0 <= ny < M:
                # 이동하려는 칸이 빈칸(0)이고, 방문하지 않은 경우 
                if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    queue.append((nx, ny, wall))
                    
                # 이동하려는 칸이 벽(1)이고, 아직 벽을 부순 적이 없는 경우 
                if graph[nx][ny] == 1 and wall == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    queue.append((nx, ny, 1))
    
    # BFS 종료 후에도 도달하지 못한 경우 
    return -1 

print(bfs())