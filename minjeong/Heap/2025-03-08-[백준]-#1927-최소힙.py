import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    n -= 1
    if num == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)