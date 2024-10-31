import sys
sys.setrecursionlimit(10**6) # 이거 안 넣음
input = sys.stdin.readline

# DFS 함수
def dfs(v):
    global order
    visited[v] = order
    # print(visited)
    order += 1
    # 정점번호를 오름차순으로 방문
    for u in sorted(graph[v]):
        if visited[u] == 0: # 이거 visited == 0으로 했음
            dfs(u)
    return

# 초기화
n, m, r = map(int, input().split()) # 정점의 수 N,  간선의 수 M, 시작 정점 R
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
order = 1 # 방문 순서
# 그래프 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 이거 안 씀

# DFS 탐색
dfs(r) # 시작정점 r부터 탐색 시작

for i in range(1, n+1):
    print(visited[i])