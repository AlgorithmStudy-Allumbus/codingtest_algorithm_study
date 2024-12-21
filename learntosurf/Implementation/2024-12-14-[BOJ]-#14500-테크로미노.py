import sys
input = sys.stdin.readline

# 테트로미노의 전체 경우의 수를 저장
tets = [
    # 1x4 막대
    [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],
    # 2x2 정사각형
    [(0, 1), (1, 0), (1, 1)],
    # ㄹ자 모양
    [(1, 0), (1, 1), (2, 1)], [(0, 1), (1, 0), (1, -1)],
    # ㄹ자 대칭
    [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)],
    # ㄴ자 모양 (회전 포함)
    [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (1, 1), (2, 1)], [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 2)],
    # ㄴ자 대칭 (회전 포함)
    [(1, 0), (2, 0), (0, 1)], [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, -1)], [(1, 0), (1, 1), (2, 0)],
    # ㅗ자 모양 (회전 포함)
    [(0, -1), (0, 1), (1, 0)], [(0, 1), (-1, 1), (1, 1)],
    [(0, -1), (0, 1), (-1, 0)], [(1, 0), (0, 1), (-1, 0)],
]

# 주어진 좌표에서 특정 테트로미노를 배치했을 때의 합 계산
def calc(i, j, tet):
    total = arr[i][j]  # 시작 좌표의 값
    for di, dj in tet:
        ni, nj = i + di, j + dj
        # 범위를 벗어나면 무효
        if 0 <= ni < N and 0 <= nj < M:
            total += arr[ni][nj]
        else:
            return 0
    return total

# 모든 위치에서 가능한 테트로미노를 배치해 최대값 계산
def max_tetromino_sum():
    max_sum = 0
    for i in range(N):
        for j in range(M):
            for tet in tets:
                max_sum = max(max_sum, calc(i, j, tet))
    return max_sum


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(max_tetromino_sum())