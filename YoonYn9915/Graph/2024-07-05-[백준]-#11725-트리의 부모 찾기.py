from collections import deque, defaultdict

def bfs(graph, start_node, n, answer):
    queue = deque([start_node])
    visited = [False] * n
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()

        for next_node in graph[current_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                answer[next_node] = current_node

    return answer

# 입력값 받기
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]

# 그래프 초기화 (인접 리스트 사용)
graph = defaultdict(list)

for edge in edges:
    node1, node2 = edge
    graph[node1 - 1].append(node2 - 1)
    graph[node2 - 1].append(node1 - 1)

# 정답 배열 초기화
answer = [0] * n

# BFS 실행 (0번 노드를 루트로 설정)
answer = bfs(graph, 0, n, answer)

# 결과 출력 (루트 노드를 제외한 노드들의 부모 노드를 출력)
for parent in answer[1:]:
    print(parent + 1)
