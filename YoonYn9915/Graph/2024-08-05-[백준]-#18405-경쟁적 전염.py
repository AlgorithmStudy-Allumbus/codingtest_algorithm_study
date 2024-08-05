from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]  # down, up, right, left
dc = [0, 0, 1, -1]

N, K = map(int, input().split())
board = []  # 바이러스 정보 받아올 배열
for _ in range(N):
    board.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())  # 시간, 행, 열

q = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:  # 바이러스가 있는 위치
            q.append((board[i][j], i, j, 0))  # 바이러스 정보, 행, 열, 흘러간 시간
q.sort()  # (주의) 리스트로 받아 정렬 후 queue로 변경!
q = deque(q)

while q:  # BFS
    viru, row, col, time = q.popleft()
    if time == S:  # 시간이 S만큼 지났다면 종료
        break
    for d in range(4):  # 상하좌우 이동
        r = row + dr[d]
        c = col + dc[d]
        if -1 < r < N and -1 < c < N and not board[r][c]:  # 범위를 벗어나지 않고 위치 값이 0일 때
            board[r][c] = viru  # 바이러스 배치
            q.append((viru, r, c, time+1))  # 다음 번 위치를 큐에 저장

print(board[X-1][Y-1])