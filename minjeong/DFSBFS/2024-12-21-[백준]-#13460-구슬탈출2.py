import sys
from collections import deque
input = sys.stdin.readline

# 보드의 크기 입력
N, M = map(int, input().split())                                 # N: 세로, M: 가로
rect_board = [list(map(str, input().strip())) for _ in range(N)] # 직사각형 보드

# BFS 탐색 방향 (상, 우, 하, 좌)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 빨간 구슬(R)과 파란 구슬(B)의 초기 위치 찾기
rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if rect_board[i][j] == 'R':
            rx, ry = i, j
        if rect_board[i][j] == 'B':
            bx, by = i, j

# BFS 탐색 준비
queue = deque([(rx, ry, bx, by, 1)])  # (rx, ry, bx, by, depth)
visited = set()
visited.add((rx, ry, bx, by)) # 방문 체크

# 구슬 이동 함수
def move(x, y, dx, dy):
    # 빨간 구슬과 파란 구슬을 보드에서 #이나 O를 만날 때까지 이동
    count = 0
    while rect_board[x + dx][y + dy] != '#' and rect_board[x][y] != 'O':
        x += dx
        y += dy
        count += 1 # 이동횟수
    return x, y, count


# BFS 탐색
while queue:
    rx, ry, bx, by, depth = queue.popleft()

    # 10번을 초과했다면 실패
    if depth > 10:
        print(-1)
        exit()

    # BFS 4방향 탐색
    for dx, dy in directions:
        # 빨간 구슬과 파란 구슬 이동
        nrx, nry, r_count = move(rx, ry, dx, dy)
        nbx, nby, b_count = move(bx, by, dx, dy)

        # 파란 구슬이 구멍에 빠지면 실패 -> 다음 방향 탐색
        if rect_board[nbx][nby] == 'O':
            continue

        # 빨간 구슬이 구멍에 빠지면 성공
        if rect_board[nrx][nry] == 'O':
            print(depth)
            exit()

        # 두 구슬이 겹칠 경우, 더 많이 이동한 구슬을 한 칸 뒤로
        if nrx == nbx and nry == nby:
            if r_count > b_count:
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy


        # 방문하지 않은 경우에만 큐에 추가
        if (nrx, nry, nbx, nby) not in visited:
            queue.append((nrx, nry, nbx, nby, depth + 1))
            visited.add((nrx, nry, nbx, nby))
# 10번 이내에 성공하지 못했다면 -1 출력

print(-1)