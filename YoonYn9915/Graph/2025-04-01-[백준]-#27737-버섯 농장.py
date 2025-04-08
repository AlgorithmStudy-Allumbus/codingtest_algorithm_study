'''


농부 해강이는 N X N칸으로 이루어진 나무판에서 버섯 농사를 짓는다. 나무판은 버섯이 자랄 수 있는 칸과 없는 칸으로 이루어져 있다.


각 버섯 포자는 포자가 심어진 칸을 포함해 최대 K개의 연결된 (버섯이 자랄 수 있는) 칸에 버섯을 자라게 한다.
이때 연결된 칸은 상하좌우로 적어도 한 변을 공유하는 칸들의 집합이라고 정의한다.

또한 한 칸에 버섯 포자를 여러 개 겹쳐서 심을 수 있으며, 만약 x개의 버섯 포자를 겹쳐 심으면 포자가 심어진 칸을 포함해 최대
x X K개의 연결된 (버섯이 자랄 수 있는) 칸에 버섯이 자란다.


해강이는 버섯 포자를 심을 때 최소 개수로만 심으려고 한다.
해강이가 농사가 가능할지 판단하고, 농사가 가능하다면 남은 버섯 포자의 개수를 출력하시오.
버섯 포자를 하나라도 사용하고 버섯이 자랄 수 있는 모든 칸에 버섯이 전부 자랐을 때 농사가 가능하다고 정의한다.

1. N X N 칸에서 버섯을 심어야 함. 이때 심은 버섯은 상하좌우 최대 K칸으로 확산.
(버섯을 심은 칸을 시작으로 BFS 탐색 진행하면 해당 칸으로부터 버섯을 심을 수 있는 인접한 칸이 몇개인지 알수 있음)

2. 2차원 배열을 순회하며 칸이 0이고 아직 방문하지 않았다면 거기서부터 BFS 탐색 시작.
3. BFS 탐색으로 해당 칸으로부터 상하좌우 인접한 0(버섯 농사 가능 칸)이 몇 개인지 파악후 K개로 나누면 해당 구역에 몇개의 버섯 포자가 필요한지 계산 가능
4. 2-3을 반복하며 모든 버섯 농사 가능 구역을 세며 총 몇개의 버섯 포자가 필요한지 계산
5. 필요한 버섯 포자 개수가 M보다 크면 남은 버섯 개수를 출력 그렇지 않다면 IMPOSSIBLE 출력.
5-1. 이떄 버섯 포자를 하나도 사용하지 않아도 IMPOSSIBLE 출력

'''

from collections import deque


def bfs(i, j, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()

    # 시작점 방문처리
    queue.append((i, j))
    visited[i][j] = 1

    # 시작점(x,y)으로부터 인접한 버섯 농사 가능 칸의 개수 (시작점 포함)
    num = 1

    while queue:
        x, y = queue.popleft()

        # 상하좌우 인접한 칸에 버섯 농사 가능한지 보기
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 그래프 범위에 있는지, 버섯 농사가 가능한지, 아직 방문하지 않았는지 확인
            if (0 <= nx <= N - 1 and 0 <= ny <= N - 1) and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                # 방문처리
                queue.append((nx, ny))
                visited[nx][ny] = 1
                # 버섯 농사 가능한 칸의 개수 증가
                num += 1

    # 해당 구역에 필요한 버섯 포자 개수 반환
    if num % K == 0:
        return num // K
    else:
        return (num // K) + 1


# 입력받기
N, M, K = map(int, input().split())

# 나무판 배열
graph = []
# 나무판 방문 배열
visited = [[0] * N for _ in range(N)]

mushroom_count = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        # 나무판이 버섯을 심을 수 있고, 아직 방문하지 않았으면
        if graph[i][j] == 0 and visited[i][j] == 0:
            mushroom_count += bfs(i, j, visited)

if mushroom_count == 0 or mushroom_count > M:
    print("IMPOSSIBLE")
else:
    print(f"POSSIBLE\n{M - mushroom_count}")
