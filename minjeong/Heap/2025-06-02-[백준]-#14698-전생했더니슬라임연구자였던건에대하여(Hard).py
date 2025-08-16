import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    total = 1
    N = int(input())
    heap = list(map(int, input().split()))
    if N == 1:
        print(1)
        continue

    heapq.heapify(heap)

    while len(heap) > 1:
        energy = heapq.heappop(heap) * heapq.heappop(heap)
        total *= energy
        heapq.heappush(heap, energy)

    print(total % 1000000007)