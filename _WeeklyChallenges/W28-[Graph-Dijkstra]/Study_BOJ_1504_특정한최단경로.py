"""
BOJ #1504. 특정한 최단경로 (골드4)
https://www.acmicpc.net/problem/1504
유형: Dijkstra , Graph
"""
import sys
import heapq
from collections import deque

INF = 1e9
input = sys.stdin.readline
answer = -1 
# 0. 입력 변수 
N ,E = map(int, input().split())
graph =[[] for _ in range(N+1)] #인접리스트 초기화
for i in range(E) :
  a, b , cost = map(int, input().split())
  graph[a].append([b , cost ]) ; graph[b].append([a, cost])
v1 ,v2 = map(int, input().split())

#1. 다익스트라 초기 설정 - 시작점
start =1 ; target = N

#2. 다익스트라 함수 정의
def dikstra(start) : 
  # 최단 거리 테이블 초기화
  distance =[INF]*(N+1)
  q = []
  heapq.heappush(q, (0,start))
  distance[start] = 0 
  #[2] 경유지 선택
  while q :
    dist , now  = heapq.heappop(q)
    #3-1 현재 노드가 이미 업데이트 완료되면 무시
    if distance[now] <dist :
      continue
    #3-2. 현재 노드와 인접한 노드 확인 , 방문 
    for i in graph[now] :
      cost = dist + i[1]
      # 4. 현재 노드 now을 경유해서 , 다른 노드(i)로 이동하는 거리가 더 짧은 경우
      if cost <distance[i[0]] :
        distance[i[0]] = cost # 업데이트
        heapq.heappush(q , (cost ,i[0])) 
  return distance

# 3. v1,v2 지나는 1- > N 의 최단 거리 고르기
s_distance = dikstra(start)
e_distance = dikstra(target) # 양방향
s_v1 = s_distance[v1]
s_v2 = s_distance[v2]
v1_e = e_distance[v1]
v2_e = e_distance[v2]
v1_v2 = dikstra(v1)[v2] # v1 - v2 거리(공통)

answer =min(s_v1 + v2_e , s_v2+v1_e ) + v1_v2
if answer >= INF : 
  print(-1)
else : 
  print(answer)


