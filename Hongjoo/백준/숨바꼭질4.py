import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 100001
# answer = [] 
#[1] 최단 시간 찾기 
visited = [[MAX, MAX] for _ in range(MAX+1)]# level 기입

t= 0
next_node = [N]
q = deque([N])
visited[N] = [t,N] # 도착 시간 , 이전 node 위치 확인

#(예외처리) 출발지 = 도착지 같은 경우
if K != N : 
  while q :
    t+=1
    next_node = len(q)
    for i in range(next_node) : # 현재 level의 node개수만큼 반복
      cx = q.popleft()
      # print(f"cx {cx} , {next_node}")
      # 만약 목적 달성시 , 끝
      for nx in [cx -1 , cx+1 , cx*2]:
        if 0<= nx <= MAX and visited[nx][0]>= MAX : 
          q.append(nx)
          visited[nx] = [t, cx]   
    # 현재 q -> 다음 level 의 노드만 남아있는 상태
    # 만약 K을 도달한 경우-> 최단 시간 저장
    if visited[K][0]< MAX : 
      break
print(t)
#[2] 역추적 - 최단 시간 경우 , 경로 추적
re_visited = [K]
pt = K
while pt != N : 
  _ , pt =visited[pt]
  re_visited.append(pt)

print(" ".join(map(str,list(reversed(re_visited)))))

