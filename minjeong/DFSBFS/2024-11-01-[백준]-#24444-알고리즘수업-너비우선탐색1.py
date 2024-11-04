import sys
from collections import deque
input = sys.stdin.readline

# BFS 탐색 함수
def bfs(r):
    global order
    queue = deque([r]) # 큐
    visited[r] = order

    while queue: # 큐가 빌 때까지 반복
        u = queue.popleft()
        for v in sorted(graph[u]): # 정점 번호를 오름차순으로 방문
            if visited[v] == 0:
                order += 1          # 방문 표시 업데이트
                visited[v] = order  # 방문순서로 방문 표시
                queue.append(v)


# 초기화
n, m, r = map(int, input().split()) # 정점의 수 n, 간선의 수 m, 시작 정점 r
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
order = 1

# 그래프 연결
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS 탐색
bfs(r) # 시작정점부터 시작

# 해당노드를 몇 번째로 방문했는지 출력
for i in range(1, n+1):
    print(visited[i])