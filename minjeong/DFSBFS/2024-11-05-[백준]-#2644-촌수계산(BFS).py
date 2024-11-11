# 2644-촌수계산. BFS 풀이
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())                    # 전체 사람 수
a, b = map(int, input().split())    # 촌수 계산할 두 사람의 번호
m = int(input())                    # 부모-자식 관계의 개수
graph = [[] for _ in range(n + 1)]  # 그래프 초기화
visited = [False for _ in range(n + 1)]  # 방문 여부 초기화
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start, end):
    queue = deque([(start, 0)]) # (노드, 거리) 형태로 초기화
    visited[start] = True       # 시작 노드 방문 표시

    while queue:
        v, dist = queue.popleft()

        # 목표 노드에 도달 시 거리 반환
        if v == end:
            return dist

        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))  # 거리 1 증가하여 큐에 추가

    return -1  # 연결되지 않았을 경우 -1 반환


print(bfs(a, b))