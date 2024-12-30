import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 설정(10만)

# 1. 입력 처리
N, R, Q = map(int, input().split())  # 정점 수, 루트 번호, 쿼리 수
graph = [[] for _ in range(N + 1)]  # 트리 그래프

# 2. 트리 정보 입력
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 3. 서브트리 크기 기록 배열
size = [0] * (N + 1)

# 4. DFS를 이용한 서브트리 크기 계산
def countSubtreeNodes(current):
    size[current] = 1  # 자기 자신 포함
    for node in graph[current]:
        if size[node] == 0:  # 아직 방문하지 않은 경우
            countSubtreeNodes(node)
            size[current] += size[node]  # 자식 서브트리 크기 추가

# 5. 루트에서 시작해 서브트리 크기 계산
countSubtreeNodes(R)

# 6. 쿼리 처리
for _ in range(Q):
    U = int(input())
    print(size[U])