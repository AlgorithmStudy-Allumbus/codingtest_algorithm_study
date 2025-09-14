"""
[BOJ]#1826.그림
https://www.acmicpc.net/problem/1926
# problem
- 그림은 1로 가로,세로(대각선x) 연결됨
- 그림 넓이 = 1의 개수 (0:여백)
-goal) 전체 nxm 도화지 속 (1) 그림 개수 (2)그림들 중 최대 넓이 
  *없으면 0 0 출력
# flow
1. 그림 개수 구하기 
  i. 전체 칸(i,j)을 기준점으로 BFS/DFS로 연결된 그래프 더미 찾기

2. 최대 그림 넓이
  - 그래프 탐색시 각 그래프에서 방문한 노드의 개수 확인&최대값 저장하기 
"""

import sys
from collections import deque
# 1. 입력 변수 - 전체 도화지 크기 / 도화지 속 그림 위치 정보
input = sys.stdin.readline
N,M = map(int, input().split())

canvas = [[0]*M for _ in range(N)]
for i in range(N):
  canvas[i] = list(map(int, input().split()))
# print(canvas)
# 그림 개수 /최대 그림 넓이 변수 선언
pic_cnt = 0 
pic_area = 0 

#2. 전체 도화지 칸을 탐색하며서 BFS로 그림들 연결하기
def bfs(start):
  # 해당 노드 1 의 개수, 방문한 노드 위치 정보 -> canvas 의 0으로 기입
  one_cnt = 0 # start 초기화
  q =deque([start])
  canvas[start[0]][start[1]] = 0  
  dy = [-1,1,0,0] # 상하좌우 이동 가능 
  dx = [0,0,-1,1]

  while q :
    cy,cx = q.popleft()
    one_cnt +=1  #그림 넓이 추가 
 
    for d in range(4):
      ny,nx= cy+dy[d], cx +dx[d]
 
      if 0<=ny<N and 0<= nx <M and canvas[ny][nx] == 1 : # 범위 내, 그림 범위임
        q.append([ny,nx])
        canvas[ny][nx]=0

  return one_cnt 

#3. 전체 칸을 BFS탐색 시작점으로 순회하기

for i in range(N) :
  for j in range(M):
    if canvas[i][j] == 1 : #그림이면,BFS 탐색 시작
      area=bfs([i,j])
      # 그림 최대 넓이 업데이트하기
      if area > 0 : # 그림이 존재하면, 그림 개수 +1 & 넓이 최대값 업데이트
        pic_cnt += 1 
        pic_area = max(pic_area,area)

print(pic_cnt)
print(pic_area)
