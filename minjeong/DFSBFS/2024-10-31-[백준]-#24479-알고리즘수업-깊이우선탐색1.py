import sys
sys.setrecursionlimit(10**6) # 최대 재귀한도 깊이
input = sys.stdin.readline

# DFS 함수
def dfs(v):
    global order
    visited[v] = order  # 방문하면 순서 넣기
    order += 1          # 다음 순서로 넘어가기
    for u in sorted(graph[v]): # 오름차순으로 인접노드 방문하기 위해 정렬
        if visited[u] == 0: # 방문 안 한 노드면 dfs탐색
            dfs(u)

# 초기화
n, m, r = map(int, input().split()) # 정점의 수 N,  간선의 수 M, 시작 정점 R
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) # 방문 순서 저장. 0이면 방문 X
order = 1 # 방문 순서

# m개의 간선 정보를 입력받아 그래프로 연결하기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 이거 안 씀

# DFS 탐색
dfs(r) # 시작정점 r부터 탐색 시작

# 해당노드를 몇 번째로 방문했는지 출력
for i in range(1, n+1):
    print(visited[i])