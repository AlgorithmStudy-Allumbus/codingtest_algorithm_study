"""
BOJ #12851. 숨바꼭질2 (골드4)
https://www.acmicpc.net/problem/12851
유형: Graph, BFS
"""

"""
풀이1
"""
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
                dist[nx] = dist[x] + 1 # 현재 걸린 시간 +1 초
                ways[nx] = ways[x] # 이전 위치에서 오는 방법의 수 가져오기
                queue.append(nx)
            # 이미 방문했지만, 같은 시간에 다시 도달한 경우
            elif dist[nx] == dist[x] + 1:
                ways[nx] += ways[x] # 기존 방법 수 + 새로운 경로 수

print(dist[K])
print(ways[K])

"""
풀이2
"""
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque()
queue.append(N)
way = [0] * 100001  # 최대 크기
cnt, result = 0, 0
while queue:
   a = queue.popleft()
   temp = way[a]
   if a == K:  # 둘이 만났을 때
       result = temp  # 결과
       cnt += 1  # 방문 횟수 +1
       continue

   for i in [a - 1, a + 1, a * 2]:
       if 0 <= i < 100001 and (way[i] == 0 or way[i] == way[a] + 1):  # 범위 안에있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
           way[i] = way[a] + 1
           queue.append(i)
print(result)
print(cnt)

"""
풀이3
"""
from sys import stdin

input = stdin.readline
from collections import deque

# 수빈 위치, 동생 위치
N, K = map(int, input().split())

MAX_SIZE = 100001

que = deque()
que.append(N)
visited = [-1] * MAX_SIZE
visited[N] = 0
cnt = 0

while que:
   # 현 위치
   current = que.popleft()
   # 도착
   if current == K:
       cnt += 1
   # 이동
   for next in [current * 2, current + 1, current - 1]:
       # 범위 내
       if 0 <= next < MAX_SIZE:
           # 첫방문 혹은 방문 시간이 같은 경우가 이미 있음(가장 빠른 시간 방법의 수를 위해)
           if visited[next] == -1 or visited[next] >= visited[current] + 1:
               visited[next] = visited[current] + 1
               que.append(next)

print(visited[K])
print(cnt)

"""
풀이4
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
if N == K:
    print(0)
    print(1)
    sys.exit()

MAX = 100_000
visited = [False] * (MAX + 1)
visited[N] = True

q = deque([N])
time = 0
ans = 0
found = False

while q and not found:
    time += 1
    level_size = len(q)
    # 이번 레벨에서 새로 방문할 노드들 기록 (방문 표시는 레벨 끝에)
    next_level = []

    for _ in range(level_size):
        x = q.popleft()
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX:
                if nx == K:
                    # 동생 위치를 발견할 때마다 카운트
                    ans += 1
                    found = True
                # 아직 한 번도 다음 레벨에서 enqueue되지 않은 노드만
                elif not visited[nx]:
                    q.append(nx)
                    next_level.append(nx)

    # 이번 레벨의 탐색이 끝난 뒤, 새로 enqueue된 노드들에 한꺼번에 방문 표시
    for node in next_level:
        visited[node] = True

# 답 출력
print(time)
print(ans)

