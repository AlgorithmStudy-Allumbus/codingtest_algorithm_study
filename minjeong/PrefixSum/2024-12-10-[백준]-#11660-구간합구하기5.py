import sys
input = sys.stdin.readline

# 누적합 테이블 계산
def get_prefix_sum(grid, N):
    prefix_sum = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix_sum[i][j] = (
                grid[i-1][j-1]
                + prefix_sum[i-1][j]
                + prefix_sum[i][j-1]
                - prefix_sum[i-1][j-1]
            )
    return prefix_sum

# 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 누적합
prefix_sum = get_prefix_sum(grid, N)

# 범위 합 계산
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = (
        prefix_sum[x2][y2]
        - prefix_sum[x1-1][y2]
        - prefix_sum[x2][y1-1]
        + prefix_sum[x1-1][y1-1]
    )
    print(answer)
