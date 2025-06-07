import sys
import heapq
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
answer = 0
heapq.heapify(cards)

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    answer += a + b
    heapq.heappush(cards, a+b)

print(answer)