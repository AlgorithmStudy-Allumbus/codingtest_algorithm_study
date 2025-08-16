"""
# [BOJ] 숩박꼭질 / 골드 4
https://www.acmicpc.net/problem/12851

-문제 
goa) 수빈 -> 동생 위치까지 도달하는데 최단"시간" &  경우의 수 (미친?)
# 조건
i. 수빈의 위치 N , 동생 K (1차원)
2. 이동 방법 (현 위치:x ) => 3가지
    (1) 걷기 : x-1 , x+1 
    (2) 순간이동 :  2*x
- 유형: BFS
field[x] = [[걸리는 시간,경우의 수]] 

5 17   
"""
import sys 
from collections import deque
N , K = map(int, sys.stdin.readline().split())
INF = 1000001
field = [[INF,0]]*INF# field[x] = 최단 시간
# BFS 특 : 먼저 방문한 경우가 최단 시간임
q = deque([N])
field[N] = [0,1] # 최단시간 , 경우의 수 

while q : 
   x  = q.popleft() # 현 위치
   ct , cn =field[x] # 현 위치에서 최단 시간 , 경우의 수
#    if field[K][0] < ct : # 종료 조건 : 
#       break 
   for nx in [x-1 , x+1 , 2*x]:
      if 0<= nx < INF:
        #[1] 첫 방문인 경우 : field[nx][1] == 0 -> 최단 시간 업데이트 & q 에 넣기 
        if field[nx][1] == 0 : 
            field[nx] = [ct +1 ,cn]
            q.append(nx) # 위치 업데이트
            # print(f"update {nx} => field[nx] : {field[nx]}")
        #[2] 중복 방문인 경우(최단 시간이 같을때)-> field[x][1]누적 경로의 수 추가
        elif field[nx][0] == ct +1  : 
            field[nx][1] += cn 
            # print(f"## duplicate :{nx} - {field[nx]}")
        # 최단 시간이 더 큼 -> 암 것도 없음

print(field[K][0])
print(field[K][1])
         
