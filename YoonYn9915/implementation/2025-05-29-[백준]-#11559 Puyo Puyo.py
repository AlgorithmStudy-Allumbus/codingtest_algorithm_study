from collections import deque
from sys import stdin
input = stdin.readline

EMPTY = '.'
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def delete_block():
    for x, y in blocks:
        board[x][y] = EMPTY


def update_board():
    for y in range(6):
        for t in range(10, -1, -1):
            for x in range(11, t, -1):
                if board[x][y] == EMPTY and board[t][y] != EMPTY:
                    board[x][y], board[t][y] = board[t][y], EMPTY


def is_in_area(x, y):
    return 0 <= x < 12 and 0 <= y < 6


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    same_blocks = [(x, y)]
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_in_area(nx, ny) and not visited[nx][ny] and board[x][y] == board[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                same_blocks.append((nx, ny))
    return same_blocks



board = [[*input().rstrip()] for _ in range(12)]
flag = True
res = 0
while flag:
    flag = False
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != EMPTY and not visited[i][j]:
                blocks = bfs(i, j)
                if len(blocks) >= 4:
                    flag = True
                    delete_block()
    if flag:
        update_board()
        res += 1
print(res)