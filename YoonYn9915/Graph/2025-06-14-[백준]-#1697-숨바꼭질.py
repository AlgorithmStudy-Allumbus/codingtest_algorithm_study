import sys
from collections import deque

inp = sys.stdin.readline

N, K = map(int, inp().strip().split())
# 해당 위치로 도달한 최소 시간 저장
visited = [-1] * (100_000 + 1)
visited[N] = 0

# (위치, 시간) 형식
queue = deque()
queue.append(N)

dx = [-1, 1, 2]

while queue:
    loc = queue.popleft()

    # 수빈이가 동생에게 도착했다면 종료
    if loc == K:
        print(visited[loc])
        break

    # 수빈의 위치에서 3가지 이동
    for i in range(3):
        if i == 2:
            new_loc = loc * dx[i]
        else:
            new_loc = loc + dx[i]

        # 새 위치가 범위 안이고 아직 방문하지 않았다면
        if 0 <= new_loc <= 100_000 and visited[new_loc] == -1:
            queue.append(new_loc)
            visited[new_loc] = visited[loc] + 1


