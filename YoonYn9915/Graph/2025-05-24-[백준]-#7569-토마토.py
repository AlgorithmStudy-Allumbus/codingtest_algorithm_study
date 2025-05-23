'''
요구조건
1. 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.


2. 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

1. 아이디어
- 익은 토마토의 인접한 곳으로 그래프 탐색을 해야 하므로 bfs 사용.
- 모든 토마토가 최소 몇 일에 익었는지 알기 위해서 토마토가 익은 일수를 저장해야 하므로 visited 배열에 저장.

2. 시간복잡도
- BFS의 시간복잡도는 O(V+E) V는 최대 1,000,000, E는 최대 6,000,000. 1초 안에 가능

3. 구현
3-1. 입력받기
3-2. 초기 모든 토마토가 1 혹은 -1인지 확인.
3-3. bfs 실행
3-4. 모두 1이 아닌데 bfs가 끝나면 -1 반환, 모두 1이면 visited 배열 중 가장 큰 값(최소 일수) 출력.

'''

from collections import deque
import sys

inp = sys.stdin.readline

# 가로, 세로, 높이
N, M, H = map(int, inp().strip().split())

arr = []
visited = [[[-1] * N for _ in range(M)] for _ in range(H)]

# 입력받기
for _ in range(H):
    temp = []
    for _ in range(M):
        temp.append(list(map(int, inp().strip().split())))
    arr.append(temp)

flag = False
# 초기 익은 토마토들을 저장하는 배열
tomatoes = []

# 초기 모든 토마토가 1 혹은 -1인지 확인.
for i in range(H):
    for j in range(M):
        for k in range(N):
            if arr[i][j][k] == 0:
                flag = True
                break
        if flag:
            break
    if flag:
        break

# 초기 1인 토마토 저장
for i in range(H):
    for j in range(M):
        for k in range(N):
            if arr[i][j][k] == 1:
                tomatoes.append((i, j, k))
                visited[i][j][k] = 0


def bfs(arr, visited, tomatoes):
    # 먼저 익은 토마토들로 큐 초기화
    queue = deque(tomatoes)

    # 상 하 좌 우 위 아래
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    # bfs 탐색
    while queue:
        (z, y, x) = queue.popleft()
        for idx in range(6):
            # 인접 칸으로 이동
            new_z = z + dz[idx]
            new_y = y + dy[idx]
            new_x = x + dx[idx]

            # 조건 확인(1. 인접칸의 인덱스가 범위 안인지, 2. 인접칸이 안익은 토마토인지, 3. 인접칸이 방문한적 없는지)
            if (0 <= new_x < N and 0 <= new_y < M and 0 <= new_z < H) and (arr[new_z][new_y][new_x] == 0) and \
                    (visited[new_z][new_y][new_x] == -1):
                # 방문처리
                queue.append((new_z, new_y, new_x))
                arr[new_z][new_y][new_x] = 1
                visited[new_z][new_y][new_x] = visited[z][y][x] + 1

    # bfs가 끝났을 때, arr 배열에 0이 하나라도 있으면 -1 출력, 그렇지 않으면 visited 배열 요소 중 가장 큰 값 출력
    if any(item == 0 for depth in arr for row in depth for item in row):
        print(-1)
    else:
        print(max(item for depth in visited for row in depth for item in row))


if flag:
    bfs(arr, visited, tomatoes)
else:
    print(0)
