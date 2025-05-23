'''
요구조건

1. 토마토는 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.
2. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익게 된다.(인접한 곳은 왼쪽, 오른쪽, 앞, 뒤를 의미한다)
3. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다. 모든 토마토가 익을 수 없다면 -1을 출력한다.

1. 아이디어
- 그래프를 탐색하여 최소 일수를 알아야 하므로 BFS
- 각 토마토가 익는 일수는 인접한 토마토가 익은 일수 + 1이므로 visited 배열을 사용해 토마토가 익는 일 저장

2. 시간복잡도
- 2 ≤ M,N ≤ 1,000
- BFS의 시간복잡도는 O(V+E) V는 최대 1,000,000, E는 최대 4,000,000. 1초 안에 가능

3. 구현
1. 입력받기
2. 초기 모든 토마토가 1이거나 -1인지 확인하기
3. bfs로 토마토 익히기 시뮬레이션
4. 모두 1이 아닌데 bfs가 끝나면 -1 반환, 모두 1이면 visited 배열 중 가장 큰 값(최소 일수) 출력.
'''

import sys
from collections import deque

inp = sys.stdin.readline

M, N = map(int, inp().split())

arr = []
visited = [[-1] * M for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, inp().split())))


def find_tomato(arr, visited):
    tomatoes = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                tomatoes.append((i, j))
                visited[i][j] = 0
    return tomatoes


def bfs(arr, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 초기 설정
    queue = deque(find_tomato(arr, visited))

    # BFS
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            # 상자 안이고, 0이고, 아직 방문하지 않았다면
            if 0 <= new_x < N and 0 <= new_y < M and arr[new_x][new_y] == 0 and visited[new_x][new_y] == -1:
                # 1로 바꾸고 방문처리하고 queue에 넣는다
                arr[new_x][new_y] = 1
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y))

    def check_tomatoes(arr):
        for i in range(N):
            for j in range(M):
                if arr[i][j] not in [-1, 1]:
                    return True
        return False

    # BFS가 끝난 후에 모두 1이 아니면 -1 반환, 모두 1이면 visited 중 가장 큰 값 찾기
    if check_tomatoes(arr):
        print(-1)
    else:
        print(max(map(max, visited)))

flag = False

# 초기에 모든 토마토가 1이거나 -1인지 확인하기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = True
            break

if flag:
    bfs(arr, visited)
else:
    print(0)


