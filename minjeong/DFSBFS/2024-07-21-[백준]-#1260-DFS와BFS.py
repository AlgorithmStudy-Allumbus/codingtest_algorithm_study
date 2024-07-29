import sys
from collections import deque
sys.setrecursionlimit(10**5) # 최대 재귀한도 깊이
input = sys.stdin.readline

# dfs 함수 정의
def dfs(start):
    print(start, end=' ')   # 해당 값을 출력한다.
    dfs_visited[start] = 1  # 해당 값을 방문처리한다.
    for u in sorted(graph[start]):  # 해당 값과 연결되어 있고, 방문하지 않았다면 재귀 탐색한다.
        if not dfs_visited[u]:
            dfs(u)

# bfs 함수 정의
def bfs(start):
    queue = deque([start])

    while queue:            # 큐가 빌 때까지 계속 반복
        u = queue.popleft() # 첫번째 값을 꺼낸다.
        if not bfs_visited[u]: # 해당 값을 방문하지 않았다면
            print(u, end=' ')  # 값을 출력한다.
            bfs_visited[u] = 1 # 방문 표시를 해준다.
        for v in sorted(graph[u]):  # 해당 값과 연결되어 있고, 방문하지 않았다면 큐에 추가한다.
            if not bfs_visited[v]:
                queue.append(v)

# 정점, 간선, 시작할 정점 초기화
n, m, v = map(int, input().strip().split()) # n: 정점 개수 / m: 간선 개수 / v: 시작 번호
dfs_visited = [0] * (n + 1)                 # DFS 방문 기록
bfs_visited = [0] * (n + 1)                 # BFS 방문 기록
graph = [[] for _ in range(n + 1)]          # 그래프 초기화

# 그래프 연결
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v)  # DFS 함수 호출
print() # 줄바꿈
bfs(v)  # BFS 함수 호출