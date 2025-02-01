import sys
import heapq

input = sys.stdin.readline


def dijkstra(graph, start, n):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    distance[start] = 0  # 시작노드의 거리 0
    # 최소 힙(우선순위 큐)을 사용하여 (거리, 노드) 튜플을 저장
    queue = []
    heapq.heappush(queue, (0, start))  # (거리, 노드)

    while queue:
        dist, current = heapq.heappop(queue)
        # 만약 이미 처리된 노드라면 continue
        if distance[current] < dist:
            continue
        # 현재 노드와 인접한 모든 노드를 확인
        for next_node, cost in graph[current]:
            # 현재 노드를 거쳐서 인접 노드로 가는 새로운 거리
            new_dist = dist + cost
            # 만약 새로 계산한 거리가 기존의 거리보다 짧으면 업데이트하고, 큐에 추가한다.
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(queue, (new_dist, next_node))

    return distance


# 입력: 마을의 수 N, 도로의 수 M, 모이는 마을 X
N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    # u번 마을에서 v번 마을로 가는 도로
    graph[u].append((v, w))
    # 역방향 그래프: v번 마을에서 u번 마을로 가는 도로
    reverse_graph[v].append((u, w))

# 1. X번 마을에서 각 마을까지의 최단 경로 (파티 후 돌아가는 시간)을 구한다.
distance_from_X = dijkstra(graph, X, N)
# 2. 각 마을에서 X번 마을까지의 최단 경로 (파티 갈 때 걸리는 시간)을 구한다.
distance_to_X = dijkstra(reverse_graph, X, N)

# 각 학생의 왕복 시간 중 최댓값을 저장한다.
max_time = 0
for i in range(1, N + 1):
    # 왕복 시간 = (i번 마을에서 X까지 가는 시간) + (X에서 i번 마을까지 가는 시간)
    round_trip = distance_to_X[i] + distance_from_X[i]
    # 최댓값 갱신
    max_time = max(max_time, round_trip)

# 최댓값 출력
print(max_time)
