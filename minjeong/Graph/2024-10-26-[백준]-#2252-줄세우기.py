import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 학생 수, 학생순서
graph = [[] for _ in range(n + 1)] # 학생 순서 그래프
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (n + 1)

# 비교(간선) 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    # a 보다 큰 노드로 b 추가
    graph[a].append(b)
    # b의 진입차수 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 키 순서대로 정렬
    q = deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입. 즉 가장 작은 학생
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()