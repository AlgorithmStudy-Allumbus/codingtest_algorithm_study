import sys
input = sys.stdin.readline

def dfs(start, cnt):
    global chonsu
    if start == y:
        chonsu = cnt
        return

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


n = int(input()) # 전체 사람 개수
x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n + 1)]
chonsu = -1 # 정답으로 반환할 촌수

m = int(input()) # 부모 자식들간의 관계 개수
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[x] = True
dfs(x, 0)
print(chonsu)
