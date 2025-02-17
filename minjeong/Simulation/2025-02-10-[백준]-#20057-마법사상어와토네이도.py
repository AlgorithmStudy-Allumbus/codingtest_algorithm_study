import sys
input = sys.stdin.readline

def move_sand(time, dx, dy, direction):
    global answer, sx, sy, grid
    for _ in range(time):
        sx += dx
        sy += dy

        if sy < 0:  # 범위 밖일 경우 stop
            break  # 토네이도는 항상 (0, 0)에 멈춘다.

        # 모래 이동
        total = 0  # α(알파)를 구하기 위한 변수
        for ddx, ddy, ratio in direction:
            nx, ny = sx + ddx, sy + ddy

            if ratio == 0:  # α 위치
                new_sand = grid[sx][sy] - total
            else:
                new_sand = int(grid[sx][sy] * ratio)
                total += new_sand

            if 0 <= nx < N and 0 <= ny < N:  # 격자 안
                grid[nx][ny] += new_sand
            else:  # 격자 밖
                answer += new_sand

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 모래 흩날리는 비율 (기준: 왼쪽 방향)
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]

right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

sx, sy = N // 2, N // 2  # 토네이도 시작 위치
answer = 0  # 격자 밖으로 나간 모래양

# 토네이도 이동 방향
for i in range(1, N+1):
    if i % 2 == 1:  # 홀수이면 좌 → 하
        move_sand(i, 0, -1, left)  # 좌
        move_sand(i, 1, 0, down)  # 하
    else:  # 짝수이면 우 → 상
        move_sand(i, 0, 1, right)  # 우
        move_sand(i, -1, 0, up)  # 상

print(answer)
