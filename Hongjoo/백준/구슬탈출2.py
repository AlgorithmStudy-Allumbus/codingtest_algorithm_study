from collections import deque
import sys
"""
1. 초기화
- R,B 의 위치 좌표
- 방문 등록
2. queue
3. 4방위 
-> 파란 구술 구멍 -> 실패
-> 빨간 구술 구멍 -> 성공 
-> 둘이 같은 위치=> 
"""

n, m = map(int, sys.stdin.readline().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = []

# 우,좌,하,상
dx = [1 ,-1 , 0 ,0] 
dy = [0,0,-1,1]

def get_RB_position(): # Red , Blue  
    rx ,ry, bx , by = 0 , 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R" :
                rx , ry = i, j
            elif board[i][j] == "B":
                bx , by = i , j
            
    return rx ,ry, bx , by 

def move(x,y, dx , dy) :
    # 벽 또는 구멍까지 이동 
    # dx ,dy : 방향 
    shift_cnt = 0 
    while board[x + dx][y+dy] != "#" and board[x][y] != "O":
        x += dx
        y+= dy
        shift_cnt +=1
    
    return x ,y, shift_cnt


def bfs() :
    #1. 초기화
    rx , ry , bx , by = get_RB_position()
    queue = deque()
    queue.append((rx,ry, bx , by, 1)) # red 좌표 , blue 좌표 , 횟수
    visited.append((rx,ry , bx,by))

    while queue :
        rx,ry,bx,by,result= queue.popleft()
        # 10회 초과해도 안나오면 -1 반환
        if result > 10 : 
            
            break 
        
        for i in range(4): # 
            crx , cry , r_shift = move(rx ,ry , dx[i], dy[i])
            cbx , cby , b_shift = move(bx ,by, dx[i], dy[i])

            # 만약 파란공이 구멍에 들어가면 실패
            if board[cbx][cby] == "O" :
                continue
            # 만약 빨간 공이 구멍에 들어가면 성공
            if board[crx][cry] == "O" :
                print(result)
                return 0
            # 만약 두 공이 겹치면 -> 더 많이 이동한 공이 더 전에 있음
            if cbx == crx and cry == cby : 
                if r_shift > b_shift : # red 가 더 멀리 있음
                    crx -=dx[i]
                    cry -= dy[i]
                else :
                    cbx -=dx[i]
                    cby -= dy[i]
            # 처음 도착한 칸인 경우
            if (crx , cry , cbx, cby) not in visited : 
                visited.append((crx , cry , cbx, cby))
                queue.append((crx , cry , cbx, cby , result +1))
    print(-1)

bfs()

