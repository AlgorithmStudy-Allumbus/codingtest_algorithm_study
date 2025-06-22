import sys
from collections import deque
input = sys.stdin.readline

MAX = 100000
N, K = map(int, input().split())
visited = [-1] * (MAX + 1)

queue = deque()
queue.append(N)
visited[N] = 0

while queue:
    current = queue.popleft()

    # 순간이동 (0초) -> 큐 앞쪽에 넣기
    nx = current * 2
    if 0 <= nx <= MAX and visited[nx] == -1:
        visited[nx] = visited[current]
        queue.appendleft(nx)  # 핵심!

    # 걷는 경우 (+1, -1) -> 큐 뒤쪽에 넣기
    for nx in (current - 1, current + 1):
        if 0 <= nx <= MAX and visited[nx] == -1:
            visited[nx] = visited[current] + 1
            queue.append(nx)

print(visited[K])
