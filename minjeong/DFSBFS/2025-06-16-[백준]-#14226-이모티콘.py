import sys
from collections import deque
input = sys.stdin.readline

# 1. 입력 및 초기화
S = int(input())
MAX = 1001

# visited[screen][clipboard] = 해당 상태까지 걸린 시간
visited = [[-1] * MAX for _ in range(MAX)]
visited[1][0] = 0

queue = deque([(1, 0)]) # 화면 임티 개수, 클립보드 임티 개수

# 2. BFS 탐색
while queue:
    screen, clip = queue.popleft()

    # 3. 목표 달성 시 종료
    if screen == S:
        print(visited[screen][clip])
        break

    for i in range(3):
        if i == 0:      # 복사 (화면 → 클립보드)
            new_screen, new_clipboard = screen, screen
        elif i == 1:    # 붙여넣기 (클립보드 → 화면)
            new_screen, new_clipboard = screen + clip, clip
        else:           # 삭제 (화면 - 1)
            new_screen, new_clipboard = screen - 1, clip

        if new_screen >= MAX or new_screen < 0 \
                or new_clipboard >= MAX or new_clipboard < 0 \
                or visited[new_screen][new_clipboard] != -1:
            continue

        visited[new_screen][new_clipboard] = visited[screen][clip] + 1
        queue.append((new_screen, new_clipboard))
