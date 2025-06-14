import sys
from collections import deque
input = sys.stdin.readline

MAX = 100000
N, K = map(int, input().split())

visited = [0] * (MAX+1)
queue = deque([N])

while queue:
    current = queue.popleft()
    if current == K:
        break
    for nx in (current + 1, current - 1, current * 2):
        if 0 <= nx <= MAX and not visited[nx]:
            visited[nx] = visited[current] + 1
            queue.append(nx)

print(visited[K])