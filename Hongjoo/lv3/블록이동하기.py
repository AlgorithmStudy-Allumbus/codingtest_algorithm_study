"""
"""
from collections import deque
def solution(board):
    N = len(board)
    #방향벡터 - "좌","상",하,우, (row, column) = (y,x)
    # 상하좌우
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    answer = 0
    
    #외벽 생성 & (idx : 1~N)
    nboard = [[1] * (N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N) :
            nboard[i+1][j+1] = board[i][j]
    
    #위치 : (y,x, 로봇 방향, 이동횟수)
    # 위치값 기준 -행, 열이 더 큰값으로 변경
    queue = deque([(1,1),(1,2), 0]) #  BFS : L, R , 거리
    visited = set([(1,1),(1,2)]) #  방문 여부 -> L,R 둘다
    print("#",visited,queue)
    while queue :
        s1,s2, dis = queue.popleft() # L,R,현거리
        # NxN목적지 도착
        if s1 == (N,N) or s2 == (N,N):
            return dis
        tmp = [] # 가능한 경우의 수
        # 상하좌우 방향으로 이동
        for d in range(4) : # [L2,R1]
            s1_r = s1[0] + dx[d]
            s1_c = s1[1] + dx[d]
            s2_r = s2[0] + dx[d]
            s2_c = s2[1] + dx[d]
            if nboard[s1_r][s1_c] == 0 and nboard[s1_r][s1_c] :
                tmp.append( ((s1_r,s1_c),(s2_r,s2_c)) ) # new position 
        #가로 -> 세로 
        if s1[0] == s2[0] : # 가로 
            # 위로 회전 or  아래로 회전
            # s2 : NN과 가장 가까운 점
            for i in [1,-1] :
                if nboard[s1[0]+i][s1[1]] == 0 and nboard[s2[0]+i][s2[1]] == 0:
                    tmp.append( (s1, (s1[0] + i, s1[1]) )) # s1중심 
                    tmp.append( (s2, (s2[0] + i ,s2[1]) )) # s2 중심
        else : # 세로 -> 가로
            #오른쪽 회전 , 왼쪽 회전
            for i in [1,-1] :
                if nboard[s1[0],s2[0]+i] == 0 and nboard[s1[0],s2[0]+i] == 0:
                    tmp.append(((s1[0],s1[1]+i), s1))
                    tmp.append(((s2[0] ,s2[1] +i) ,s2))
        
        for pset in tmp : # 이웃한 좌표들 중 
            if pset not in visied : #없으면 
                queue.append((pset , dis+1))
                visited.add(pset)
