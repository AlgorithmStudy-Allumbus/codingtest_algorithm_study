from collections import deque

n, w, L = map(int, input().split())
cars = list(map(int, input().split()))

queue = deque()
for _ in range(w):
    queue.append(0)

time = 0
idx = 0
while idx < n:
    time += 1
    queue.popleft()

    if sum(queue) + cars[idx] <= L:
        queue.append(cars[idx])
        idx += 1
    else:
        queue.append(0)

while queue:
    time += 1
    queue.popleft()

print(time)
