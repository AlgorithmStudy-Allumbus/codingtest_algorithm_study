'''
BOJ #2206.벽 부수고 이동하기 (골드3)
https://www.acmicpc.net/problem/2206
유형: BFS,구현
'''

import sys
from collections import deque
# 1. 입력 그래프
N , M = map(int,sys.stdin.readline().split())
graph = []
for n in range(N) : 
  graph.append(list(map(int, input())))

#방문 여부 & 시작노드로 부터 최단 경로 거리 ,벽 부순 횟수(3차원) 
visited = [[[0]*2 for _ in range(M)] for k in range(N)]

#상하좌우 -> 인접 노드
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 2. bfs 최단 거리
def bfs():
  #초기 노드 queue 에 추가 , 방문 등록
  dq = deque()
  dq.append((0,0,0))
  visited[0][0][0] = 1 
  
  while dq : 
    x,y,wall = dq.popleft()
    # 목적지(N,M) 도착한 경우,이동 횟수 출력
    if x == N-1 and y == M -1 : 
      return visited[x][y][wall]
    
    for i in range(4):#상하좌우로 다음 이동할 칸의 위치
      xx = x+ dx[i] ; yy = y+ dy[i]
      # (1)다음 이동할 곳이 graph 밖에 있는 경우 
      if xx<0 or xx>= N or yy <0 or yy>= M:
        continue
      # (2) 다음 이동할 곳이 벽이고, 한번도 벽 안 뚤었을때
      if graph[xx][yy] == 1 and wall == 0 : # and not visited[xx][yy][1]
        visited[xx][yy][1] = visited[x][y][0]+1
        dq.append((xx,yy,1))
      
      #(3)다음 이동할 곳이 벽이 아니고,한번도 방문 하지 않은 곳
      elif graph[xx][yy] == 0 and visited[xx][yy][wall] == 0 : # 그냥 감
        visited[xx][yy][wall] = visited[x][y][wall] +1
        dq.append((xx,yy,wall))
      
  return -1 #BFS 종료될떄 까지 도착점에 도달하지 못하면 -1 출력하기

print(bfs())


