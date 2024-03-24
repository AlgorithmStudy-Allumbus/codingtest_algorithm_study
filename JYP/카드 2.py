# 마지막 남은 카드 번호 구하는 문제
# 가장 먼저 카드의 개수를 불러온 뒤, deque함수를 이용해 빈 큐를 생성한다
import sys
from collections import deque

a = int(sys.stdin.readline())
deq = deque()

# 이후, for문을 통해 1부터 a까지의 수(카드 번호)를 큐에 넣는다
for i in range(a):
    deq.append(i+1)
# while문을 통해 deq가 1이 될 때까지 가장 위 차드를 버리고, 제일 위 카드를 가장 아래로 옮긴다
while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())
    
print(deq.pop())
