import sys
sys.setrecursionlimit(10**6) # 최대 재귀한도 깊이
input = sys.stdin.readline

# DFS 함수
def dfs(v):
    global order
    visited[v] = order  # 방문하면 순서 넣기
    order += 1          # 다음 순서로 넘어가기
    
    for u in sorted(graph[v], reverse=True): # 내림차순으로 인접노드 방문하기 위해 정렬
        if visited[u] == 0: # 방문 안 한 노드면 dfs탐색
            dfs(u)


# 초기화
n, m, r = map(int, input().strip().split()) # n: 정점의 수, m: 간선의 수, r: 시작 정점
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
order = 1

# 그래프 연결
for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

# 해당노드를 몇 번째로 방문했는지 출력
for i in range(1, len(visited)):
    print(visited[i])