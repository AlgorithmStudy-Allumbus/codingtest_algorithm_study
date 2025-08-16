""""
실버1
https://www.acmicpc.net/problem/2468
# 조건 : 
(1) 물에 잠기지 않은 구역 위치 구하기
(2) 안 잠긴 구역들의 군집 개수 찾기 
- 상하좌우로 연결된 구역 = 1 군집
# 유형: 노드 탐색 ->  BFS/DFS
연결된 노드들이 이루는 군집 개수 구하는 문제 


"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
field = [] 
limit_list= set()
limit_list.add(0) 
# 1. 물에 잠김, 생존 구역으로 구분한 field 만들기
for i in range(n):
  tmp = list(map(int,input().split()))
  for j in range(n) :
    # limit_list 수집하기 = 노드의 높이 값 종류
    limit_list.add(tmp[j])
  field.append(tmp)
# print(f"field - {limit_list}")


# 종류별 limit에 따라 지대 높이가 limit 이하일 경우 침수되는 지역, 생존 지역 명시
# board :  생존 여부 + 방문 여부 확인 flag 역할
def init_board(limit) :
  # 각 limit 별로 침수되는 지역을 확인하기
  board = [[0 for _ in range(n)] for k in range(n)  ]
  saved_point = []
  # 침수 지역 맵 업데이트하기
  for i in range(n):
    for k in range(n):
      if field[i][k] <= limit : # 침수 지역
        board[i][k] =-1
      else : 
         # 생존 지역
        saved_point.append([i,k])
  return board,saved_point

# 2. 생존 구역들의 군집 개수 구하기 
#상하좌우
dy =[-1,1,0,0 ]
dx = [0,0,-1,1]
def bfs(sy,sx , field): 
  # (1)시작점 정의
  q = deque()
  q.append([sy,sx])
  field[sy][sx] = 1 # 방문 등록
  # (2)인접한 노드 
  while q  : 
    cy,cx =q.popleft()
    for dw in range(4):
      ny,nx = cy + dy[dw] , cx +dx[dw] 
      # 2-1 필드 범위에서 벗어나는지 확인
      # 2-2방문 여부 확인
      if 0<= ny < n and 0<= nx < n and field[ny][nx] == 0 : # 방문 안했으면 업데이트
        q.append([ny,nx])
        field[ny][nx] = 1 
    
  return 0 
# main 함수 
max_cnt = 0 
for limit in limit_list :  #limit 을 1개씩 조합해봄 
  board,saved_point = init_board(limit)
  # print(f"##{limit} : {saved_point}")
  cnt = 0 
  # 생존 구역에서 확인 
  for y,x in saved_point :
    if board[y][x] == 0 :#방문 안했으면 -> bfs 탐색 진행
      bfs(y,x, board)
      cnt +=1 

  max_cnt = max(max_cnt , cnt)
print(max_cnt)