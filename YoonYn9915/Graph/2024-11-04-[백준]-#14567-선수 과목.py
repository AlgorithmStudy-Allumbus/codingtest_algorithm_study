from collections import deque

def topology_sort(graph, inDegree):
    queue = deque()

    result = [-1] * (N+1)


    # 진입차수가 0인 정점을 queue에 추가
    for i in range(1, N+1):
        if inDegree[i] == 0:
            queue.append(i)
            result[i] = 1


    while queue:
        now = queue.popleft()

        for vertex in graph[now]:
            inDegree[vertex] -= 1
            if inDegree[vertex] == 0:
                queue.append(vertex)
                result[vertex] = result[now] + 1

    return result



# 입력값 받기
N, M = map(int, input().split())

# 과목 개수만큼 이차원 리스트 만들기
graph = [ [] for _ in range(N+1)]

# 진입차수 리스트
inDegree = [0] * (N+1)
result = [] * (N+1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

result = topology_sort(graph, inDegree)
for i in range(1,N+1):
    print(result[i], end=" ")
