import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, n):
    queue = deque()
    queue.append((x, y)) # 시작점 추가
    visited[x][y] = True # 초기 방문 처리

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, jump_game[x][y]), (jump_game[x][y], 0)]: # 아래 (0, jump), 오른쪽 (jump, 0)
            nx, ny = x + dx, y + dy  # 현재 위치에서 칸 수만큼 이동
            # 맵 범위 안에 있고, 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if jump_game[nx][ny] == -1:  # 도착 지점에 도달하면
                    return True
                visited[nx][ny] = True
                queue.append((nx, ny))  # 다음 이동 지점 추가

    return False

# 입력 처리
n = int(input())
jump_game = []
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    temp = list(map(int, input().split()))
    jump_game.append(temp)

# BFS 탐색
if bfs(0, 0, n):
    print("HaruHaru")
else:
    print("Hing")