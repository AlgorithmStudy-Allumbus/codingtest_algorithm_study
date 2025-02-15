import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, n):
    D = [INF] * (n+1)
    D[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)
    
    while q:
        dist, now = heapq.heappop(q)  # 최단 거리 노드 꺼내기
        
        if D[now] < dist:  # 이미 처리된 노드라면 무시
            continue
        
        for val, next_node in graph[now]:  # 현재 노드와 연결된 노드 탐색
            cost = dist + val
            if cost < D[next_node]:  # 더 짧은 경로 발견 시
                D[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                
    return D

# 입력 처리
N, M, X = map(int, input().split())
graph = defaultdict(list)
reverse_graph = defaultdict(list)

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((time, end))  # 단방향 도로
    reverse_graph[end].append((time, start))  # X에서 출발하는 경우 대비

# X에서 모든 마을까지의 최단 거리 계산 (X -> 모든 마을)
to_X = dijkstra(X, graph, N)

# 모든 마을에서 X까지의 최단 거리 계산 (모든 마을 -> X) -> 역방향 그래프 사용
from_X = dijkstra(X, reverse_graph, N)

# 왕복 시간 계산
max_time = 0
for i in range(1, N+1):
    if i == X:
        continue  # X에서 출발하는 학생은 제외
    max_time = max(max_time, to_X[i] + from_X[i])

print(max_time)
