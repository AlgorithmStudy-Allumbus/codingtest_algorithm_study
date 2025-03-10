import sys, math
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y):
    queue = deque([(x, y)])
    boards[x][y] = 1  # 방문 처리
    areas = 1  # 현재 덩어리 크기

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상하좌우 이동

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and boards[nx][ny] == 0:
                boards[nx][ny] = 1  # 방문 처리
                queue.append((nx, ny))
                areas += 1  # 영역 개수 증가
    return areas

total_nums = 0
use_seed = False

# 버섯이 자랄 수 있는 칸 찾기
for i in range(N):
    for j in range(N):
        if boards[i][j] == 0:
            areas = bfs(i, j)  # BFS로 덩어리 크기 계산
            nums = math.ceil(areas / K)  # 필요한 포자 개수
            total_nums += nums 
            use_seed = True  # 포자 사용 가능 여부 확인

if not use_seed:
    print('IMPOSSIBLE')
elif total_nums <= M:
    print('POSSIBLE')
    print(M - total_nums)  # 남은 포자 개수 출력
else:
    print('IMPOSSIBLE')
