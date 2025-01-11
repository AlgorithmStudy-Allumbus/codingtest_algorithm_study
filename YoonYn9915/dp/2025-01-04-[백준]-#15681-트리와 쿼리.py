'''
1. 트리 정보 입력받기. 무방향 그래프이기 때문에 간선을 잇는 두 노드에 다 저장.
2. 부모 노드의 서브 트리의 수는 모든 자식 노드의 서브 트리 수의 합으로 분할 할 수 있다.
    즉 분할 & 정복 가능하며 그래프를 순회하며 각 정점에서 서브트리의 수를 메모이제이션 해야 한다.

'''

import sys

inp = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, R, Q = map(int, inp().split())

subtree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    first_node, second_node = map(int, inp().split())
    graph[first_node].append(second_node)
    graph[second_node].append(first_node)


# node_num: 현재 노드 번호
def count_subtree(graph, subtree, node_num):
    # 방문 체크
    subtree[node_num] = 1

    for child_node in graph[node_num]:
        if subtree[child_node] == 0:
            count_subtree(graph, subtree, child_node)
            subtree[node_num] += subtree[child_node]


count_subtree(graph, subtree, R)

for i in range(Q):
    node_num = int(inp())
    print(subtree[node_num])
