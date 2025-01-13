import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
A, B = map(int, input().split())

# 큐 초기화
queue = deque([A])
cnt = 1 # 연산 횟수

while queue:
    # 현재 큐에서 모든 값을 탐색
    for _ in range(len(queue)):
        current = queue.popleft()

        # 현재 값이 B와 같으면 결과 출력 후 종료
        if current == B:
            print(cnt)
            exit()

        # 다음 값을 큐에 추가 (B를 초과하지 않는 경우만)
        if current * 2 <= B:
            queue.append(current * 2)
        if int(str(current)+"1") <= B:
            queue.append(int(str(current)+"1"))

    # 연산 횟수 증가
    cnt += 1

# 큐가 비었다면 -1 출력
print(-1)