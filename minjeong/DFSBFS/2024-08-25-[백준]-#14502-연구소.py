import copy
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 바이러스가 연구소 내에 확산되는 것을 시뮬레이션 하는 함수
def bfs(new_lab, viruses):
    N = len(new_lab)
    M = len(new_lab[0])
    queue = deque(viruses)
    visited = [[False for _ in range(M)] for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 인접한 네 방향 확인
            nx, ny = x + dx, y + dy
            # 범위 내에 있고, 아직 확산되지 않은 곳이라면
            if (0 <= nx < N and 0 <= ny < M) and new_lab[nx][ny] == 0 and not visited[nx][ny]:
                new_lab[nx][ny] = 2         # 바이러스 확산
                visited[nx][ny] = True      # 방문 표시
                queue.append((nx, ny))      # 큐에 추가

def get_safe_area(new_lab):
    cnt = 0
    for row in new_lab:
        cnt += row.count(0)
    return cnt
   #return sum(row.count(0) for row in new_lab)

def solve(N, M, lab):
    empty_spaces = []   # 빈 칸의 위치를 담을 리스트
    viruses = []        # 바이러스의 위치를 담을 리스트
    # 빈 공간과 바이러스의 위치 저장
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0: # 빈 칸
                empty_spaces.append((i, j))
            if lab[i][j] == 2: # 바이러스
                viruses.append((i, j))

    max_safe_area = 0 # 최대 안전 영역 크기를 저장할 변수

    for walls in combinations(empty_spaces, 3):
        new_lab = copy.deepcopy(lab) # 깊은 복사를 사용하여 lab 복사

        # 벽 설치
        for x, y in walls:
            new_lab[x][y] = 1

        # 바이러스 확산시킴
        bfs(new_lab, viruses)

        # 영역 크기 계산
        safe_area_cnt = get_safe_area(new_lab)
        # 현재 조합의 safe_area가 max_safe_area보다 크다면 값 업데이트
        max_safe_area = max(max_safe_area, safe_area_cnt)

    return max_safe_area


# 입출력
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

print(solve(N, M, lab))