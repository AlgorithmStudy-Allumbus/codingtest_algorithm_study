import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    answer = []  # 시작 도시에서 최단거리 k인 모든 도시 번호를 저장할 리스트
    visited[start] = 0  # 시작 노드 방문 표시 (시작노드는 거리 0)

    while queue:
        current = queue.popleft()

        # 현재 노드와 연결된 노드 탐색
        for node in graph[current]:
            if visited[node] == -1:  # 아직 방문하지 않았다면 방문 처리하고 큐에 추가
                visited[node] = visited[current] + 1  # 현재 노드의 거리 + 1
                queue.append(node)

                # 연결된 노드의 거리가 k와 같을 경우 answer에 추가
                if visited[node] == k:
                    answer.append(node)
    return answer


# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발도시 번호 x
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 그래프
visited = [-1] * (n + 1)

# 그래프 연결
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 출발도시 번호 x부터 BFS 탐색
answer = bfs(x)
if answer:
    for ans in sorted(answer):
        print(ans)
else:
    print(-1)  # 최단거리 k인 도시가 하나도 존재하지 않으면 -1 출력