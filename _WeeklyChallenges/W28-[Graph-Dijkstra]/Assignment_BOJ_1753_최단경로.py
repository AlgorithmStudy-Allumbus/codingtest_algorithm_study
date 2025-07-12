"""
BOJ #1753. 최단경로 (골드4)
https://www.acmicpc.net/problem/1753
유형: Dijkstra , Graph
"""
import sys
import heapq
input = sys.stdin.readline
INF = 1e12
V , E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E) : 
    a,b , c =map(int, input().split())
    graph[a].append((b,c))

distance = [INF]*(V+1)
# 다익스트라 함수 
def dijkstra(start) :
    q = []
    distance[start]=0 
    heapq.heappush(q,(0,start))
    while q : 
        # 2.경유지 뽑기 
        dist , now = heapq.heappop(q)
        # 3-1. 이미 처리한 경유지인 경우 -> 무시
        if distance[now] < dist : 
            continue
        #3-2. 현재 경유지에서 바로 갈 수 있는 노드 처리
        for t in graph[now]:
            cost = dist + t[1] # 경유지를 거친 start - t[0] 의 거리
            if cost < distance[t[0]] :  # 경유지 cost 가 더 작으면 업데이트 
                distance[t[0]] = cost 
                heapq.heappush(q, (cost , t[0]))
#4. 출력
dijkstra(start)
for node in range(1 , V+1) : 
    print("INF"if distance[node] >= INF else distance[node]  )

