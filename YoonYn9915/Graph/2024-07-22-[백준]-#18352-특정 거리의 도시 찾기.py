from collections import deque
import sys

f = sys.stdin.readline

def bfs(visited, graph,k,x):
        visited[x] = 0
        queue = deque([x])
        answer = []

        while queue:
            current_city = queue.popleft()
            for next_city in graph[current_city]:
                if visited[next_city] == -1:
                    queue.append(next_city)
                    visited[next_city] = visited[current_city] + 1
                    if visited[next_city] == k:
                        answer.append(next_city)

        if not answer:
            print(-1)
        else:
            answer.sort()
            for ans in answer:
                print(ans)


n,m,k,x = map(int, f().split())

graph = [[] for _ in range(n+1)]


for i in range(m):
    a,b = map(int, f().split())
    graph[a].append(b)

visited = [-1] * (n+1)

bfs(visited, graph,k,x)