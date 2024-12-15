N = int(input())

# 가로, 세로, 대각선 순
dx = [0, 1, 1]
dy = [1, 0, 1]


def dfs(x, y, dir):
    # 이미 방문한 상태라면 결과를 반환
    if memo[x][y][dir] != -1:
        return memo[x][y][dir]

    # 종료 조건: 목표에 도달하면 경로 1개 추가
    if x == N - 1 and y == N - 1:
        return 1

    # 경로 수
    paths = 0

    for dir_idx in range(3):
        # 현재 방향에서 이동 불가능한 방향 건너뛰기
        if (dir == 0 and dir_idx == 1) or (dir == 1 and dir_idx == 0):
            continue

        newX = x + dx[dir_idx]
        newY = y + dy[dir_idx]

        # 이동 가능한지 검사
        if 0 <= newX < N and 0 <= newY < N and arr[newX][newY] == 0:
            if dir_idx == 2:  # 대각선
                if arr[newX - 1][newY] == 1 or arr[newX][newY - 1] == 1:
                    continue

            # DFS 탐색
            paths += dfs(newX, newY, dir_idx)

    # 결과를 메모이제이션에 저장
    memo[x][y][dir] = paths
    return paths


# 입력
arr = [list(map(int, input().split())) for _ in range(N)]

# 메모이제이션 초기화: -1로 채움
memo = [[[-1] * 3 for _ in range(N)] for _ in range(N)]

# DFS 시작
print(dfs(0, 1, 0))
