import sys
from collections import deque
input = sys.stdin.readline
MAX = 100000
N , K  = map(int,  input().split())
visited = [MAX] * (MAX+1) # 방문 여부
# 2. BFS로 N-> K 의 모든 경로 찾기
t=0 
q = deque([N , t])
visited[N]= 0 


while q : 
  cx= q.popleft()
  ct =visited[cx]
  for nx in (cx-1 , cx+1 , 2*cx) :
    if 0 <= nx < MAX :
      # 시간 업데이트 
      if nx == 2*cx :
        nt = ct 
      else :
        nt = ct+1
      
      if visited[nx] >= MAX  : # 처음 도달
        q.append(nx)
        visited[nx] = nt
      else : # 중복& 최단 거리일때
        if nt < visited[nx] :
          visited[nx] = nt
          q.append(nx)
print(visited[K])