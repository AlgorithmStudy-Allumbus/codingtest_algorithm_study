"""
https://www.acmicpc.net/problem/7576
# BFS, DFS
(1) filed 값 중 1인 값 찾기
(2) 상하좌우로 -1 빼고 확산 
(3) flag로 해당 이잔 turn에서 확산 유무를 판단 -> 안되면 turn 종료

"""
# 입력 
import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int, input().split())

field = [list(map(int,input().split())) for _ in range(M) ]
# print(field) 
dy = [-1,1,0,0]
dx = [-0,0,-1,1]
# BFS


lv = 0 
burn = []
q = deque()
for m in range(M) :
        for n in range(N) :
            # print(m , n)
            if field[m][n] == 1: 
                # 안 익은 토마토 익히기 
                q.append([m,n])
                
while q :
    # 각 turn 마다 토마도 전염시키기

    # print(f"{t}턴 - {m}{n}")
    #[2] 익은 토마토 확산시키기
    # t+= 1
    y,x = q.popleft()
    for d in range(4):
        ny = y + dy[d] ; nx = x + dx[d]
        if 0<= ny <M and 0 <= nx < N and field[ny][nx] == 0:
            field[ny][nx] = field[y][x] +1
            q.append([ny,nx])
        
max_num = 0 
for i in range(M) :
    for j in range(N):
        if field[i][j]== 0 : 
            print(-1)
            exit()
        max_num = max(max_num , field[i][j])
print(max_num-1)

    #             burn.append([n,m])
    # q = deque()
    # for sy,sx in burn : 
    #     q.append([sy,sx])
    #     while q : 
            