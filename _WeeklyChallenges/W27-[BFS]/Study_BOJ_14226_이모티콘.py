from collections import deque
import sys

S = int(sys.stdin.readline().strip())

# visited[screen][clipboard]
visited = [[-1] * (S + 1) for _ in range(S + 1)]

queue = deque()
queue.append((1, 0))  # 화면: 1, 클립보드: 0
visited[1][0] = 0

while queue:
    screen, clipboard = queue.popleft()

    # 목표 이모티콘 수에 도달하면 종료
    if screen == S:
        print(visited[screen][clipboard])
        break

    # 1. 복사 (화면 -> 클립보드)
    if visited[screen][screen] == -1:
        visited[screen][screen] = visited[screen][clipboard] + 1
        queue.append((screen, screen))

    # 2. 붙여넣기 (클립보드 -> 화면)
    if clipboard != 0 and screen + clipboard <= S and visited[screen + clipboard][clipboard] == -1:
        visited[screen + clipboard][clipboard] = visited[screen][clipboard] + 1
        queue.append((screen + clipboard, clipboard))

    # 3. 삭제 (화면 -1)
    if screen - 1 >= 0 and visited[screen - 1][clipboard] == -1:
        visited[screen - 1][clipboard] = visited[screen][clipboard] + 1
        queue.append((screen - 1, clipboard))
