import sys
sys.setrecursionlimit(10000) #재귀 limit 설정(파이썬 최대 깊이 늘리는 모듈 이용)

# 1. DFS 함수
def dfs(u):
    visited[u] = True   # 방문표시
    for v in graph[u]:  # 연결되어 있는 리스트 내 요소들도 방문 표시
        if visited[v] == False:
            visited[v] = True
            dfs(v)      # 연결되어 있는 요소의 연결된 요소도 dfs로 탐색

# 2. 입력 및 초기화
input = sys.stdin.readline
N, M = map(int, input().strip().split()) # N: 정점의 개수, M: 간선의 개수
graph = [[] for _ in range(N+1)]        # 그래프 초기화
visited = [False] * (N+1)               # 방문여부 리스트 초기화

# 3. 그래프 만들기
for _ in range(M):
    u, v = map(int, input().strip().split()) # 양 끝점 u,v
    graph[u].append(v)
    graph[v].append(u)


# 4. 연결 요소 개수 찾기
cnt = 0
for i in range(1, N+1):
    if visited[i] == False:     
        cnt += 1    # 첫 방문시에만 cnt에 +1
        dfs(i)    

# 5. 정답 출력
print(cnt)