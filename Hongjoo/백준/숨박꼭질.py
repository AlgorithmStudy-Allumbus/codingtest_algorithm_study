import sys
from collections import deque
input = sys.stdin.readline
MAX = 100000
# 1. N, K 입력변수 입력 받기
N ,K = map(int, input().split())
# 2. N과 K 가 같을 때 , 예외처리
if N == K : 
  print(0)
  exit()

# 3. BFS 로 K까지 도달하는데 최단 거리 출력하기
q = deque([N])
visited = [False] * (MAX + 1)
visited[N] = True
lv = 1 
#[1] while 을 최단거리(level) 만큼 반복
while q:
  level_size = len(q) 
  next_lv = []
  #[2] 현 lv 의 노드만 BFS 탐색 & 다음 lv 후보군 노드을 enqueue
  for _ in range(level_size) :
    cx = q.popleft()
    for nx in (cx-1 , cx+1 ,2*cx) : 
      if 0 <= nx <= MAX:
        if nx == K :  # 목적지 도착
          print(lv)
          exit()
        # 첫 방문 
        if not visited[nx] : 
          q.append(nx)
          next_lv.append(nx)
  # print(f"##{lv}= {level_size} => {next_lv}")
  lv +=1
  for x in next_lv :
    visited[x] = True