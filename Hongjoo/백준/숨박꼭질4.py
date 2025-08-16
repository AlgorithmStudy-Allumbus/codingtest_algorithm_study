import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 100000
# answer = [] 
#[1] 최단 시간 찾기 
visited = [MAX]* (MAX+1) # level 기입
t= 0 
next_node = [N]
q = deque([N])
visited[N] = t
while q :
  t+=1 
  next_node = len(q)
  for i in range(next_node) : # 현재 level의 node개수만큼 반복
    cx = q.popleft()
    # 만약 목적 달성시 , 끝
    for nx in [cx -1 , cx+1 , cx*2]:
      if 0<= nx <= MAX and visited[nx]>= MAX : 
        q.append(nx)
        visited[nx] = t   
  # 현재 q -> 다음 level 의 노드만 남아있는 상태
  # 만약 K을 도달한 경우-> 최단 시간 저장
  if visited[K] <MAX : 
    # answer.append(t)
    break

#[2]역추적K-> N - backtracking , DFS
re_visited = []
stack = deque([[K,t]])
while stack : 
  cx, ct = stack.pop()
  if cx not in re_visited : 
    re_visited.append(cx)
    if cx == N : 
      break
    if cx %2==0 : #짝수면
      ad_li = [cx-1,cx+1 , cx//2]
    else : 
      ad_li = [cx-1, cx+1]
    # print("##",ad_li , type(ad_li))
    for nx in ad_li :
      if 0<=nx <=MAX and nx not in re_visited and visited[nx] == ct-1: 
        stack.append([nx,ct-1]) 
print(t)
print(" ".join(map(str,list(reversed(re_visited)))))

