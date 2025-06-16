import sys
from collections import deque

input = sys.stdin.readline

MAX = 100000
N, K = map(int, input().split())
dist = [-1] * (MAX + 1)
ways = [0] * (MAX + 1)

queue = deque([N])
dist[N] = 0
ways[N] = 1

while queue:
    x = queue.popleft()

    for nx in (x - 1, x + 1, x * 2):
        # 범위 내
        if 0 <= nx <= MAX:
            # 아직 방문하지 않은 위치
            if dist[nx] == -1: 
                dist[nx] = dist[x] + 1  # 현재 걸린 시간 +1 초
                ways[nx] = ways[x]      # 이전 위치에서 오는 방법의 수 가져오기
                queue.append(nx)
            # 이미 방문했지만, 같은 시간에 다시 도달한 경우    
            elif dist[nx] == dist[x] + 1: 
                ways[nx] += ways[x]     # 기존 방법 수 + 새로운 경로 수

print(dist[K])
print(ways[K])