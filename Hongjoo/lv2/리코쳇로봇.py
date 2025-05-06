"""
#문제 다 읽고 수도 코드 짜자
- goal) 시작 R => 목표 G 까지 최소 이동 수 구하기(도달 못하면 -1 )
- 상하좌우로 "장애물, 가장자리"에 부딫칠 떄까지 이동 = 1회 이동 => 외곽& 장애물 = field[-1]
- board 는 text로 주어짐 => 2차원 배열로 변환 
# flow - BFS : 최단 거리
- 이동 방법
"""
from collections import deque
INF = 1e9
def solution(board):
    answer = 0
    #1. 필드 board 정보를 2차원 배열로 변환(장애물 -1/ 없음 0 )
    N , M = len(board) , len(board[0])
    field = [[INF]*M for _ in range(N)]
    
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == "R":
                start = [i,j]
            elif board[i][j] == "G":
                target = [i,j]
            elif board[i][j] == "D":
                field[i][j] = -1
                # print("break",field[i][j])
    #2. 탐색 
    # print(start , target ,field)
    #상하좌우
    dy = [-1, 1, 0,0] 
    dx = [0,0,-1,1]
    def move_node(d, start): # 이동 방향 ,출발점
        ny , nx = start ; flag = False # flag : 최소 이동 여부(Y/N)
        while 0<= ny + dy[d]< N and 0<= nx+dx[d] < M and field[ny + dy[d]][nx+dx[d]] >= 0 : # 장애물, 가장자리x 
            ny += dy[d] ; nx += dx[d]
            flag = True
        return ny ,nx , flag
    # 시작점 초기화
    q= deque([start])
    field[start[0]][start[1]] = 0 
    cnt = 0 
    while q : 
        cy,cx = q.popleft()
        if [cy,cx] == target : #(옵션)효율성
            break
        for di in range(4):
            cnt += 1 
            ny,nx,f = move_node(di, [cy,cx])
            if f and field[ny][nx] == INF : # 해당 [ny,nx] 에 처음 도착(방문x) & 해당 지점에 이동 가능할 경우 
                field[ny][nx] = min(field[ny][nx], field[cy][cx]+1)
                # min은 필요 없음(BFS로 가장먼저 field에 입력 된 턴수가 최소 이동수 )
                # field안에 최소 이동 턴수 기록
                q.append([ny,nx])

    #3. 출력
    answer=field[target[0]][target[1]]
    # target지점 값에 업데이트가 없음 -> 도달 못함 : -1 / 최소 이동 턴수
    if answer >= INF : 
        answer = -1
    return answer