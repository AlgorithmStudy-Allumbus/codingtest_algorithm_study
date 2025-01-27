import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
N = int(input())  # 카드의 개수
queue = deque(range(1, N + 1))  # 1부터 N까지 큐 생성
answer = []  # 버린 카드를 저장할 리스트

# 큐에서 카드 처리
while len(queue) > 1:
    answer.append(queue.popleft())  # 맨 앞의 카드를 버린다
    queue.append(queue.popleft())  # 그다음 카드를 맨 뒤로 옮긴다

# 마지막 남은 카드 추가
answer.append(queue.popleft())

# 출력
print(' '.join(map(str, answer)))  # 버린 카드와 마지막 남은 카드 출력
