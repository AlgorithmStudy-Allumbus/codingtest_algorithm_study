import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 설정 (10만)

# 1. 입력 받기
N = int(input())  # 마을 개수
people = [0] + list(map(int, input().split()))  # 각 마을 주민 수 (인덱스 맞추기 위해 0 추가)

# 2. 마을 연결 (트리 구성)
town = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    town[u].append(v)
    town[v].append(u)

# 3. DP 테이블 초기화 및 방문 리스트
dp = [[0, 0] for _ in range(N + 1)]  # dp[i][0]: 우수 마을 X, dp[i][1]: 우수 마을 O
visited = [False] * (N + 1)


# 4. DFS를 통한 서브트리 탐색 및 DP 계산
def dfs(current):
    visited[current] = True  # 현재 노드 방문 처리
    dp[current][1] += people[current]  # 현재 마을을 우수 마을로 선정한 경우 (자기 자신 포함)

    for child in town[current]:
        if not visited[child]:
            dfs(child)  # 자식 노드로 DFS 진행
            dp[current][1] += dp[child][0]  # 자식 노드가 우수 마을이 아닌 경우 주민 수 더하기
            dp[current][0] += max(dp[child][0], dp[child][1])  # 자식 노드에서 우수 마을이거나 아닌 경우 중 최대값 선택


# 5. DFS 호출 (루트 노드 1부터 시작)
dfs(1)

# 6. 결과 출력
print(max(dp[1][0], dp[1][1]))
