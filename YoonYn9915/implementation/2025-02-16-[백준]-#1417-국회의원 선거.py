import heapq

n = int(input())

hq = []
for i in range(n):
    votes = int(input())
    if i == 0:
        dasom_votes = votes
        continue

    heapq.heappush(hq, -votes)

bribe_count = 0
while hq:
    votes = -heapq.heappop(hq)
    if votes < dasom_votes:
        break

    dasom_votes += 1
    bribe_count += 1
    heapq.heappush(hq, -(votes - 1))

print(bribe_count)