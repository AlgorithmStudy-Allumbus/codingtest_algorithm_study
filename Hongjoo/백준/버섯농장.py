import math
import sys
from collections import deque

def bfs(y_1 , x_1 , visited) :
  # 초기 위치 방문
  queue = deque()
  queue.append((y_1,x_1))
  visited[y_1][x_1] = True
  count = 0  # 방문할 node 개수 
  # 큐 시작
  while queue :
    y,x  =queue.popleft()
    count+=1 
    for k in range(4):
      next_y, next_x = y + dy[k] , x + dx[k]
      # 필드 범위 포함 확인 & 방문 확인 &이동 가능 지역(0)
      if 0<=next_y<N and 0<=next_x<N :
        if not visited[next_y][next_x] and not field[next_y][next_x] :
          queue.append((next_y, next_x))
          visited[next_y][next_x] = True
  return count


input =sys.stdin.readline
N , M , K = map(int, input().split()) # field 범위, 씨앗 개수, 확산량
X = M
# 1. field 와 방문 등록 받기
field = [[0 for _ in range(N)] for k in range(N)]
visited = [[False for _ in range(N)] for k in range(N)]
for i in range(N) :
  field[i]=list(map(int, input().split()))
# 상하좌우
dy = [-1,1,0,0]
dx = [0,0, -1,1]

#2. bfs

for i in range(N):
  for j in range(N):
    #포자 가능 지역 + 방문 안 한곳
    if field[i][j] == 0 and not visited[i][j]:
      cur_node = bfs( i, j , visited)
      # 사용할 씨앗 청구하기
      X = X - math.ceil(cur_node/K)
      if X < 0 : #씨앗이 음수 남았으면 -> 불가능
        print("IMPOSSIBLE")
        exit()
# 3. 마무리 출력
if X == M : # 필드 자체가 농사 불가 -> 1개도 사용 못함
  print("IMPOSSIBLE")
  exit()
elif X >= 0 : # 씨앗 남음
  print("POSSIBLE")
  print(X)