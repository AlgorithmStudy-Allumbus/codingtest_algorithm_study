import sys
from collections import deque

input = sys.stdin.readline
'''
내용 정리하면서 최적화한 코드
'''
# 1. 입력
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

# 사과 위치 입력
apples = set()
for _ in range(K):
    x, y = map(int, input().split())
    apples.add((x - 1, y - 1))  # 0-index로 변환

L = int(input()) # 방향 변환 횟수
turn_times = deque([]) # 방향 전환 정보 /  [(3, 'D'), (15, 'L'), (17, 'D')]
for _ in range(L):
    t, d = input().split()
    turn_times.append((int(t), d))

# 2. 초기화
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 방향 리스트 (우, 하, 좌, 상) # 방향 변환에 따라 인덱싱
snake = deque([(0, 0)]) # 뱀 초기 위치: 큐
current = 0 # 초기 방향. (오른쪽)
time = 0

# 3. 시뮬레이션
while True:
    time += 1

    # 3.1. 뱀 머리 이동
    head_X, head_Y = snake[-1]  # 머리 좌표
    dx, dy = directions[current] # 오른쪽 좌표
    new_head = (head_X + dx, head_Y + dy)

    # 3.2. 벽이나 자기 몸에 닿았다면 게임을 종료
    if not (0 <= new_head[0] < N and 0 <= new_head[1] < N) or new_head in snake:
        print(time) # 게임 종료
        break

    # 3.3. 사과 확인 하고 꼬리를 처리
    snake.append(new_head)  # 새로운 머리 추가

    # 사과 있는지 확인
    if new_head in apples:
        apples.remove(new_head)  # 사과 제거
    else:
        snake.popleft() # 꼬리 제거

    # 3.4. 방향 전환
    if turn_times and time == turn_times[0][0]:
        _, direction = turn_times.popleft()
        if direction == 'D':  # 오른쪽
            current = (current + 1) % 4
        elif direction == 'L':  # 왼쪽
            current = (current + 3) % 4

'''
# 문제 푸는 당시에 작성했던 코드
import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) # 보드 크기
K = int(input()) # 사과 개수
board = [[0] * N for _ in range(N)] # 보드 판

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 방향 리스트 (우, 하, 좌, 상) # 방향 변환에 따라 인덱싱
snake = deque([(0, 0)]) # 뱀 초기 위치: 큐
current = 0 # 현재 방향은 오른쪽
time = 0
direction_info = deque([]) # 방향 정보 /  [(3, 'D'), (15, 'L'), (17, 'D')]

# 사과 위치 입력, 배치
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

L = int(input()) # 방향 변환 횟수
for _ in range(L):
    t, d = map(str, input().split())
    direction_info.append((int(t), d))


while True:
    time += 1

    # 뱀 머리 이동
    head_X, head_Y = snake[-1]  # 머리 좌표
    dx, dy = directions[current] # 오른쪽 좌표
    new_head = (head_X + dx, head_Y + dy)

    # 벽이나 자기 몸에 닿았는지 판단한다.
    if (0 <= new_head[0] < N and 0 <= new_head[1] < N) and new_head not in snake:
        snake.append(new_head) # 새로운 머리 추가

        # 사과 있는지 확인
        # 있으면 꼬리 냅두고,
        if board[new_head[0]][new_head[1]] == 1:
            board[new_head[0]][new_head[1]] = 0 # 사과 먹음

        # 없으면 꼬리를 줄인다.
        else:
            snake.popleft()

        # 방향 바꾸기
        if direction_info and time == direction_info[0][0]:
            t, dir = direction_info.popleft()
            if dir == 'D': # 오른쪽
                current = (current + 1) % 4
            elif dir == 'L': # 왼쪽
                current = (current + 3) % 4

    else:
        # 게임 종료
        print(time)
        break
'''