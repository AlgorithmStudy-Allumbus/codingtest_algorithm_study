def dfs(x, y):
    # 배추밭의 범위를 벗어나면 종료
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    # 배추가 없거나 이미 방문한 경우 종료
    if graph[y][x] == 0:
        return

    # 현재 배추 방문 처리
    graph[y][x] = 0

    # 상, 하, 좌, 우로 재귀 호출
    dfs(x + 1, y)  
    dfs(x - 1, y)  
    dfs(x, y + 1)  
    dfs(x, y - 1)  

T = int(input())
 
for _ in range(T):
    M, N, K = map(int, input().split())
    # NxM 행렬 
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())  # 배추 위치 (x: 가로, y: 세로)
        graph[y][x] = 1  # (y,x) 위치에 배추 표시
    
    count = 0 # 배추흰지렁이 수 (군집 개수)
    
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1: # 배추가 있고 방문하지 않았다면
                dfs(x, y) # DFS 호출 
                count += 1 # 군집 개수 증가 
    
    print(count)