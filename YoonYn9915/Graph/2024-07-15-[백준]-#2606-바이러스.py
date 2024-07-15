from collections import defaultdict
from collections import deque


def bfs(graph, visited):
    queue = deque()

    queue.append(1)
    visited[1] = 1
    answer = 0

    while queue:
        num = queue.popleft()
        for neighbor in graph[num]:
            if visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = 1
                answer += 1

    print(answer)


numOfComputer = int(input())
numOfConnection = int(input())

graph = defaultdict(list)
visited = [0] * (numOfComputer + 1)

for _ in range(numOfConnection):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

bfs(graph, visited)
