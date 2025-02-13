import sys
from collections import deque
input = sys.stdin.readline

# 입력
N, M, K = map(int, input().split())
grid = [[deque([]) for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    grid[r-1][c-1].append([m, s, d])

# 방향벡터
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
               (1, 0), (1, -1), (0, -1), (-1, -1)]

# K번만큼 반복
temp_grid = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(K):
    # 1. 이동하기
    temp_grid[i][j].clear()  # 기존 구조 초기화

    for i in range(N):
        for j in range(N):
            while grid[i][j]:
                m, s, d = grid[i][j].popleft()
                dx, dy = directions[d]
                nx, ny = (i + dx * s) % N, (j + dy * s) % N
                temp_grid[nx][ny].append([m, s, d])
    grid = temp_grid

    # 2. 2개 이상의 파이어볼 칸은 합치고 나누기
    for i in range(N):
        for j in range(N):
            # 한 칸에 두 개 이상 있을 경우
            if len(grid[i][j]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even = 0, 0, 0, 0
                cnt_total = len(grid[i][j])

                # 합치기
                while grid[i][j]:
                    m, s, d = grid[i][j].popleft()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1

                # 방향 결정
                if cnt_odd == cnt_total or cnt_even == cnt_total:
                    d_list = [0, 2, 4, 6]
                else:
                    d_list = [1, 3, 5, 7]

                # 나누기
                new_m = sum_m // 5          # 질량
                new_s = sum_s // cnt_total  # 속력

                if new_m > 0:  # 질량이 0 이면 소멸
                    for d in d_list:        # 방향
                        grid[i][j].append([new_m, new_s, d])

# 정답(파이어볼 질량의 합) 구하기
answer = 0
for i in range(N):
    for j in range(N):
        for m, s, d in grid[i][j]:
            answer += m

print(answer)