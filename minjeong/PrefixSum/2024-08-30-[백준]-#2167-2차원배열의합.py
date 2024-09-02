import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# Prefix sum array를 생성
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

# prefix_sum 배열을 채우기
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

K = int(input())  # 합을 구할 부분의 개수
for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]

    print(result)