import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

# CCTV 위치 저장
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))

total_cctv = len(cctvs)  # 전체 CCTV 개수
min_blind_spot = 1e9  # 정답으로 반환할 사각지대 개수

# CCTV별 방향 설정
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 -> 우 -> 하 -> 좌
cctv_dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}


# 사각지대 개수 구하는 함수
def count_zero(temp):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cnt += 1
    return cnt


# DFS 함수
def dfs(idx, office):
    global min_blind_spot
    # 종료 조건
    if idx == total_cctv:
        # 종료할 때는 사각지대(= 0) 개수 세고, 최소값 갱신해야 한다.
        blind_spot = count_zero(office)
        min_blind_spot = min(min_blind_spot, blind_spot)
        return

    x, y, number = cctvs[idx]
    for cctv_dir in cctv_dirs[number]:
        # temp에 현재 office 리스트 깊은 복사
        temp = copy.deepcopy(office)

        for dir in cctv_dir:
            dx, dy = directions[dir]
            nx, ny = x + dx, y + dy

            while 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = '#'  # CCTV 감시OK
                nx += dx
                ny += dy

        dfs(idx + 1, temp)


dfs(0, office)
print(min_blind_spot)