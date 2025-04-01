from collections import deque
def solution(maps):
    n,m = len(maps) ,len(maps[0])# y길이 # x 길이 
    
    # 이동 범위 - 하,우,상,좌
    dx = [0,1 , 0,-1]
    dy = [1 , 0 , -1 , 0]
    queue = deque([(0,0)])
    visited = [[False for _ in range(m)] for k in range(n)]
    visited[0][0] = True
    #2. BFS
    while queue :
        # 현위치 
        curr_y , curr_x = queue.popleft()
        
        # 통로 확인 - 벽or 바운더리 밖이면 x 
        for i in range(4):
            next_y = curr_y + dy[i]
            next_x = curr_x + dx[i]
            # target 도착 확인 
            if next_y == n-1 and next_x == m-1 and maps[next_y][next_x] == 1:
                visited[next_y][next_x] = True
                maps[next_y][next_x] = maps[curr_y][curr_x] +1
                break
            # 바운더리 안에 있음 * 길인 경우 + 방문 등록 x 
            if 0<=next_y< n and 0<= next_x < m :
                if maps[next_y][next_x] == 1 and not visited[next_y][next_x]:
                    maps[next_y][next_x] = maps[curr_y][curr_x] +1 
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = True

          
    # 3. 최단 거리 출력
    # print(answer_list)
    if not visited[n-1][m-1]:
        return -1 
    # answer = min(answer_list)
    answer= maps[-1][-1]
    # print(answer)
    return answer