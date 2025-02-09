import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewels = []
for _ in range(N):
    heapq.heappush(jewels, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jewels)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jewels:
        break
print(answer)
