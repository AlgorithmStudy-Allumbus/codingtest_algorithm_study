import sys
import heapq
input = sys.stdin.readline

# 입력
N = int(input())    # 도시의 개수
M = int(input())    # 버스의 개수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append([end, weight])

# 우리가 구하고자 하는 구간의 출발지와 도착지 번호
goal_s, goal_e = map(int, input().split())

# 최단거리 테이블 초기화
distances = [float('inf')] * (N+1)
distances[goal_s] = 0
heap = []
heapq.heappush(heap, (goal_s, 0)) # 힙(heap)에 (시작노드, 가중치) 추가

while heap:
    current, dist = heapq.heappop(heap) # 최소힙

    if distances[current] >= dist:
        for node, weight in graph[current]:
            if dist + weight < distances[node]: # 지금 발견한 게 더 작으면
                distances[node] = dist + weight
                heapq.heappush(heap, (node, dist + weight))

print(distances[goal_e])