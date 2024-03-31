from collections import deque
import sys

n = int(sys.stdin.readline())
deque = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for i in range(n):
	x = deque.popleft()
	print(x[0], end=' ')
	if x[1] > 0:
		deque.rotate(-(x[1] - 1))
	else:
		deque.rotate(-x[1])
