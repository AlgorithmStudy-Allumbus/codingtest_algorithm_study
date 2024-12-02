from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 정점의 개수, 간선의 개수 
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부 리스트 초기화 
visited = [False] * (N + 1)

# 연결 요소 개수 
connected_components = 0 

def bfs(graph, start):
    queue = deque([start])  # 시작 정점을 큐에 추가
    visited[start] = True  # 시작 정점을 방문 처리
    while queue:
        current = queue.popleft()  # 큐에서 정점 꺼내기
        for neighbor in graph[current]:  # 현재 정점의 모든 이웃에 대해 반복
            if not visited[neighbor]:  # 방문하지 않은 경우만 처리
                visited[neighbor] = True  # 방문 처리
                queue.append(neighbor)  # 큐에 추가

for i in range(1, N+1):
    if not visited[i]: # 방문하지 않은 정점에서 BFS 수행
        bfs(graph, i)
        connected_components += 1

print(connected_components)