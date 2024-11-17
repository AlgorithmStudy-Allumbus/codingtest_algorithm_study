# sys로 명령 수를 받은 뒤, deque를 통해 비어 있는 큐를 생성한다
# 명령 처리에 필요한 기능을 구현한 뒤, 입력된 명령 수인 a 만큼 for문을 통해 반복한다

import sys
from collections import deque

a = int(sys.stdin.readline())
deq = deque()
for _ in range(a):
    b = sys.stdin.readline().split()
    
    # deq에 추가
    if b[0] == 'push':
        deq.append(int(b[1]))
    # 가장 앞의 수 출력
    if b[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    # 큐에 든 정수 개수 출력
    if b[0] == 'size':
        print(len(deq))
    # 비었다면 0, 아니면 1
    if b[0] == 'empty':
        if deq:
            print('0')
        else:
            print('1')
    # 큐의 가장 앞 정수 출력, 정수가 없을 경우 -1 출력
    if b[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    # 큐의 가장 뒤 정수 출력, 없을 경우 -1 출력
    if b[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
