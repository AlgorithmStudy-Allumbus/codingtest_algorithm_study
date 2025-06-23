"""
https://www.acmicpc.net/problem/13549

[BOJ] 숨바꼭질3/골드5/
#promblem 
- 이동 방법[t, x] -> [t+1 , x-1] ,[t+1 , x+1] # 걷기/ ``[t , 2*x]`` 
#flow : BFS (최단 시간 x , 최단 동작 횟수) or DFS
1. node= [현 위치 x , 현 시간 t]
2.이웃한 node - x+1 , x-1 , 2*x
  (if , nx = 2*x -> t else :걷기 -> t+1)
IDEA
- 같은 level -> 이동(걷기+ 순간이동) 횟수 동일함
- 궁극적으로 최단 시간 = 최단 경로 , 순간이동을 가장 많이 해야함 (순간이동 우선순위가 높음)
=> 2*x -> x-1, x+1 순으로 다음 node 탐색하기
-> 중복되지만 순간이동으로 도달한 경우 vs 걸어서 도달한 경우를 비교할 때, 
"""

import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001
N , K  = map(int,  input().split())
visited = [MAX] * (MAX+1) # 방문 여부
# 2. BFS로 N-> K 의 모든 경로 찾기
q = deque([N])
visited[N]= 0 

while q : 
  cx= q.popleft()
  ct = visited[cx] 
  if cx == K: 
     break
  for nx in (2*cx , cx-1 , cx+1 ) :
    if 0 <= nx < MAX and visited[nx] >= MAX : # nx 의 제한 조건
      # 시간 업데이트 
      if nx == 2*cx : 
          visited[nx] = visited[cx]
      else : 
          visited[nx] = visited[cx] +1
      q.append(nx)
print(visited[K])
