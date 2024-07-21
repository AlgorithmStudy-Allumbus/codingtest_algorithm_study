import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    global k
    queue = deque([start])
    visited[start] = 0 # 시작 노드의 거리를 0으로 설정
    while queue:
        node = queue.popleft()
        for connected_node in graph[node]:                  # 해당 노드와 연결된 노드 순회
            if visited[connected_node] == -1:               # 방문하지 않은 노드일 경우
                queue.append(connected_node)                # 큐에 추가하고
                visited[connected_node] = visited[node] + 1 # 거리를 1 증가

                # 연결된 노드의 거리가 k와 같다면 answer 리스트에 추가
                if visited[connected_node] == k:
                    answer.append(connected_node)
    return answer

# 도시 개수 n, 도로 개수 m, 거리 정보 k, 출발도시 번호 x
n, m, k, x = map(int, input().strip().split())
visited = [-1 for _ in range(n + 1)] # 모든 노드를 -1로 초기화 (방문하지 않은 상태)
graph = [[] for _ in range(n + 1)]
answer = []

# 그래프 연결
for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)

# BFS 호출 -> 출발도시 번호 x로 시작
answer = bfs(x)
if not answer:
    print(-1)
else:
    answer.sort()
    for u in answer:
        print(u)