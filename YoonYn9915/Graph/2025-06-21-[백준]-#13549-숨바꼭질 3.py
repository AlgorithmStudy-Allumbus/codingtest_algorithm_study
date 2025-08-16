import sys
from collections import deque

inp = sys.stdin.readline

N, K = map(int, inp().strip().split())
# 해당 위치로 도달한 최소 시간 저장
visited = [-1] * (100_000 + 1)
visited[N] = 0

# (위치, 시간) 형식
queue = deque()
queue.append((N, 0))

dx = [2, -1, 1]

min_time = -1

while queue:
    subin_loc, time = queue.popleft()

    # 수빈이가 동생에게 도달한 시간까지만 bfs탐색하고 그 후에 종료
    if min_time != -1 and min_time + 2 == time:
        break

    # 수빈이가 동생에게 도달한 시간체크
    if min_time == -1 and subin_loc == K:
        min_time = visited[subin_loc]

    # 수빈의 위치에서 3가지 이동
    for i in range(3):
        if i == 0:
            new_loc = subin_loc * dx[i]
        else:
            new_loc = subin_loc + dx[i]

        # 새 위치가 범위 안
        if 0 <= new_loc <= 100_000:
            # 새로 방문한 위치가 이전에 와보지 못했다면,
            if visited[new_loc] == -1:
                # 방문 시간 설정해주고 경로 초기화
                if i == 0:
                    visited[new_loc] = visited[subin_loc]
                    queue.append((new_loc, time))
                else:
                    visited[new_loc] = visited[subin_loc] + 1
                    queue.append((new_loc, time + 1))


print(visited[K])
