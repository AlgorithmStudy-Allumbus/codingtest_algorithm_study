from collections import defaultdict, deque

N, M, V = map(int, input().split())

# 인접리스트로 그래프 표현 
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    graph[node].sort() # 정점 번호가 작은 순서대로 탐색하기 위해 정렬 

def dfs(graph, start, visited): # visited 리스트를 재귀 호출 간에 공유해야 하므로, 함수 인자로 전달 
    visited.append(start) # 현재 정점을 방문
    for neighbor in graph[start]:
        if neighbor not in visited: # 방문하지 않은 정점만 탐색 
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = [] # 방문 순서 
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited: # 방문하지 않은 경우 
            visited.append(node)
            queue.extend(graph[node]) # 이웃 정점 추가 
    return visited

dfs_result = dfs(graph, V, [])
bfs_result = bfs(graph, V)

print(*dfs_result)
print(*bfs_result)