import sys

# 입력 받기
R, C, T = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 방향 설정 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 공기 청정기 위치 찾기
cleaner = []
for i in range(R):
    if pan[i][0] == -1:
        cleaner.append(i)

# 먼지 확산 함수
def spread():
    temp = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if pan[x][y] > 0:
                value = pan[x][y] // 5
                count = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and pan[nx][ny] != -1:
                        temp[nx][ny] += value
                        count += 1
                pan[x][y] -= value * count
    for x in range(R):
        for y in range(C):
            pan[x][y] += temp[x][y]

# 공기 청정기 작동 함수
def clean():
    # 위쪽 청정기
    top = cleaner[0]
    for i in range(top - 1, 0, -1):
        pan[i][0] = pan[i - 1][0]
    for i in range(C - 1):
        pan[0][i] = pan[0][i + 1]
    for i in range(top):
        pan[i][C - 1] = pan[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        pan[top][i] = pan[top][i - 1]
    pan[top][1] = 0

    # 아래쪽 청정기
    bottom = cleaner[1]
    for i in range(bottom + 1, R - 1):
        pan[i][0] = pan[i + 1][0]
    for i in range(C - 1):
        pan[R - 1][i] = pan[R - 1][i + 1]
    for i in range(R - 1, bottom, -1):
        pan[i][C - 1] = pan[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        pan[bottom][i] = pan[bottom][i - 1]
    pan[bottom][1] = 0

# 시뮬레이션 실행
for _ in range(T):
    spread()
    clean()

# 남은 미세먼지 계산
result = sum(sum(row) for row in pan) + 2  # 공기청정기 위치(-1)를 더하지 않음
print(result)
