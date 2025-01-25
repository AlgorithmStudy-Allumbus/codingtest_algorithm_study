from collections import deque


def topology_sort(graph, inDegree):
    queue = deque()
    # 위상정렬 결과를 담을 리스트
    result = []

    # 진입차수가 0인 정점을 큐에 추가
    for num in range(len(inDegree)):
        if inDegree[num] == 0:
            queue.append(num + 1)

    while queue:
        now = queue.popleft()
        result.append(now)

        # 진입차수 업데이트
        for vertex in graph[now - 1]:
            inDegree[vertex - 1] -= 1
            # 진입차수가 0인 정점을 큐에 추가
            if inDegree[vertex - 1] == 0:
                queue.append(vertex)

    return result


# 정점, 간선의 개수
N, M = map(int, input().split())

# 진입차수
inDegree = [0] * N
# 그래프
graph = [[] for _ in range(N)]

for i in range(M):
    first, second = map(int, input().split())
    # 그래프 변경
    graph[first - 1].append(second)
    # 진입차수 증가
    inDegree[second - 1] += 1

result = topology_sort(graph, inDegree)
for ans in result:
    print(ans, end=" ")
