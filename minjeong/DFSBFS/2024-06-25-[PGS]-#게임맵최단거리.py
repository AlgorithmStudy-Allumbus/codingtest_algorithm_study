from collections import deque

def bfs(maps, x, y, n, m, visited):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 좌,우,하,상
            nx, ny = x + dx, y + dy
            
            # maps 범위 안에 있어야 하고, 벽이 아니어야 하고(값이 1이어야 하고), 아직 방문하지 않았다면 탐색
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))

                maps[nx][ny] = maps[x][y] + 1 # 값을 +1 
                
    # 이때 우측 하단의 상,좌,우의 값이 0이면 경로가 이어질 수 없다.
    # 목적지에 도달하지 못할 경우엔 -1 반환
    if maps[n-1][m-1] == 1:  
        return -1
    else:  # 도달했을 경우 최단 거리 반환
        return maps[n-1][m-1] 
    
def solution(maps):
    n, m = len(maps), len(maps[0])  # maps의 행과 열의 크기
    visited = [[False] * m for _ in range(n)] # 방문여부 리스트
    visited[0][0] = True  # 시작 지점 방문 표시

    # bfs 탐색 시작
    answer = bfs(maps, 0, 0, n, m, visited)
    return answer
