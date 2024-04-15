from collections import deque
import sys
input = sys.stdin.readline


a = int(input())
sec1 = list(map(int, input().split()))
sec2 = list(map(int, input().split()))
b = int(input())
sec3 = list(map(int, input().split()))


queue = deque([])
for i in range(a):
  if sec1[i] == 0:
    queue.appendleft(sec2[i])
else:
  if queue == []:
    print(*sec3)
    sys.exit()


for i in range(b):
  queue.append(sec3[i])
  print(queue.popleft(), end = " ")
