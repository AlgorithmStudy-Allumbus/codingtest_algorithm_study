import sys
from collections import deque

input = sys.stdin.readline

# 총 층수 F, 현재 층 S, 목표 층 G, 위 버튼 U, 아래 버튼 D
F, S, G, U, D = map(int, input().split())


def bfs():
    if S == G:  # 강호가 이미 도착해있다면 0번 클릭
        return 0

    visited = [False for _ in range(F + 1)]
    queue = deque([(S, 1)])  # (현재 층, 버튼 클릭 횟수)
    visited[S] = True

    while queue:
        x, cnt = queue.popleft()

        # 위로 이동
        nx = x + U
        if nx <= F and not visited[nx]:
            if nx == G:  # 목표층 도착
                return cnt
            queue.append((nx, cnt + 1))
            visited[nx] = True  # 방문여부 표시 꼭 넣어주기

        # 아래로 이동
        nx = x - D
        if nx > 0 and not visited[nx]:
            if nx == G:  # 목표층 도착
                return cnt
            queue.append((nx, cnt + 1))
            visited[nx] = True

        # 목표층에 도달하지 못한 경우
    return -1


# BFS 탐색
answer = bfs()
if answer == -1:
    print("use the stairs")
else:
    print(answer)