import sys
from collections import deque
input = sys.stdin.readline

FIELD_X = 12
FIELD_Y = 6

# 1. 입력
field = [list(input().strip()) for _ in range(FIELD_X)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
combo = 0

# 상하좌우로 동일한 블록을 탐색해 해당 좌표들을 가진 리스트 반환
def bfs(x, y):
    queue = deque([(x, y)])
    color = field[x][y]
    visited[x][y] = True
    same_blocks = [(x, y)] # 같은 블록의 좌표 리스트

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < FIELD_X and 0 <= ny < FIELD_Y) and \
                field[nx][ny] == color and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                same_blocks.append((nx, ny))

    return same_blocks


# 동일한 블록 제거
def delete(same_blocks):
    for x, y in same_blocks:
        field[x][y] = '.'


# 반복문 돌면서 위에서 아래로 블록 내리기
def down():
    for y in range(FIELD_Y):
        for x in range(10, -1, -1):
            for k in range(FIELD_X - 1, x, -1):
                if field[x][y] != '.' and field[k][y] == '.':
                    field[k][y] = field[x][y]
                    field[x][y] = '.'


while True:
    pang = False
    visited = [[False for _ in range(FIELD_Y)] for _ in range(FIELD_X)]

    for i in range(FIELD_X):
        for j in range(FIELD_Y):
            if field[i][j] != '.' and not visited[i][j]:
                same_blocks = bfs(i, j)

                # 동일한 블록이 4개 이상일 경우 터트리기
                if len(same_blocks) >= 4:
                    pang = True
                    delete(same_blocks)


    # 터뜨린 블록이 있으면 밑으로 내리기
    if pang:
        down()
        combo += 1
    else:
        # 더이상 터뜨릴 게 없다면 종료
        break

print(combo)