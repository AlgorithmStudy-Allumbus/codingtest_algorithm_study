"""
BOJ #1238. 파티 (골드3)
https://www.acmicpc.net/problem/1238
유형: Dijkstra
"""

import sys
import heapq
# 1. 인접 리스트 field 만들기 (단방향)
input = sys.stdin.readline
INF = int(1e9) #1<=Time<=100
N , M , start_town = map(int , input().split()) # 시작 note 
# 각 road (edge)와 Time  정복가 담김 리스트 만들기 
field = [[] for _ in range(N+1) ] # idx : 1~ N+1
#무한으로 최단 거리 테이블 초기화 
to_X_distance = [ [INF for _ in range(N+1)] for k in range(N+1)]

# 1-2. 모든 road 및  time 정보 받기 
for m in range(M) :
    start , end , time = map(int, input().split())
    field[start].append((end, time))


# 다익스트라
def dijkstra(start , distance ) :
    q = [] # 우선순위 큐 
    #1. 시작 노드에 대해 최단경로 = 0 , 큐 삽입(시간 = 0 , 노드)
    heapq.heappush(q , (0,start)) 
    distance[start] = 0 
    #2. q가 비어 있기 전까지
    while q :
        # 가장 최단 거리 짧은 노드에 대한 정보 추출
        time , now  = heapq.heappop(q) # A -> now(중간)
        # 현재 노드가 이미 처리 = 방문 여부 확인 
        if distance[now] < time :
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인 
        for near_road  , near_time in field[now] :
            duration = near_time + time #  A -> now -> B
            #기존 방법 보다  현재 노드 경유해서 갈때 시간이 적게 걸릴때 
            # 큐 삽입 & 최단거리 테이블 업데이트
            if duration < distance[near_road] :
                distance[near_road] = duration # 업데이트
                heapq.heappush(q , (duration , near_road)) # 큐에 넣기

    return distance

# 1. N-1 번 다익스트라 수행 -> 2차원 최단 거리 리스트 만듦 
for i in range(1,N+1) :
    to_X_distance[i] = dijkstra(i,to_X_distance[i] )

#2.  각 마을별 왕복 최단 시간 계산 :{twon -> x} + {x-> town} 
result = [0 for _ in range(N+1)]
for town in range(1,N+1):
    result[town] = to_X_distance[town][start_town] + to_X_distance[start_town][town] 

print(max(result))