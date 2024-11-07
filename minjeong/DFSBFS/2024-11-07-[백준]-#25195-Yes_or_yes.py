import sys
sys.setrecursionlimit(10**6) # 재귀 한도

input = sys.stdin.readline

def dfs(current):
    if not visited[current]:
        if current not in gomgom: # 해당 노드에 팬클럽 곰곰이가 없다면, 방문 표시
            visited[current] = True
        else:
            # 시작부터 곰곰이 있기 때문에 True가 나올 수가 없기에 False 반환
            return False

    if not graph[current]:  # 더이상 탐색할 노드가 없다면, 팬클럽을 만나지 않아도 되기 때문에 True 반환
        return True

    for node in graph[current]:
        if not visited[node]:
            visited[node] = True
            if node not in gomgom: # 인접 노드에 팬클럽이 없다면, 재귀호출
                if dfs(node): # 팬클럽을 만나지 않고 도착할 수 있는 경우 True 반환
                    return True
            visited[node] = False # 다른 경로를 탐색하기 위해 방문취소

    return False

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) # u에서 v로의 단방향 간선 추가

# 팬클럽 곰곰이 정보
s = int(input())                            # 곰곰이가가 존재하는 정점의 개수 s
gomgom = list(map(int, input().split()))    # 공곰이가 존재하는 정점의 번호 목록

# 1번 정점에서 dfs 탐색 시작
if dfs(1):  # 팬클럽 곰곰이를 만나지 않고 이동할 수 있는 경우
    print("yes")
else: # 어떻게 이동하는 곰곰이를 만나게 되는 경우
    print("Yes")