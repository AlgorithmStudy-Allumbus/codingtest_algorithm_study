import sys
from collections import deque
input = sys.stdin.readline

def get_result(goal_sec, goal_x, goal_y, grid, n, k):
    virus_info = [] # 바이러스 정보를 담는 리스트 초기화

    # 시험관을 순회하며 바이러스 팀섹
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:                             # 바이러스라면
                virus_info.append((grid[i][j], 0, i, j))    # 바이러스 번호, 현재 시간, x좌표, y좌표를 추가

    virus_info.sort()                               # 바이러스 정보 리스트를 오름차순으로 정렬
    queue = deque(virus_info)                       # 큐 초기화
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 방향 리스트 (상, 하, 좌, 우)

    while queue:
        virus_num, time, x, y = queue.popleft()

        # 목표 시간에 도달하면 종료
        if time == goal_sec:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy # 현재 지점에서 상하좌우 인접한 지점
            #  시험관 범위 안에 있고 아직 바이러스가 없는 경우 현재의 바이러스를 전파
            if (0 <= nx < n and 0 <= ny < n) and grid[nx][ny] == 0:
                grid[nx][ny] = virus_num
                queue.append((virus_num, time + 1, nx, ny))

    return grid[goal_x][goal_y]

# 입력 처리
n, k = map(int, input().split())    # n: 시험관 크기 / k: 바이러스 개수
grid = []                           # 시험관 정보
for _ in range(n):
    li = list(map(int, input().split()))
    grid.append(li)
s, x, y = map(int, input().split()) # 시간, x좌표, y좌표

# 함수 호출 및 결과 출력
print(get_result(s, x-1, y-1, grid, n, k))
