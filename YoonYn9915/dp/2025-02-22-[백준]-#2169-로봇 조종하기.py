import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 첫번째 행의 최대가치는 왼쪽에서 오는 방향밖에 없음
for i in range(1, M):
    arr[0][i] += arr[0][i - 1]

for i in range(1, N):
    # 위쪽, 왼쪽에서 오는 경로의 최대 가치 저장
    dp1 = arr[i][:]
    # 위쪽, 오른쪽에서 오는 경로의 최대 가치 저장
    dp2 = arr[i][:]
    for j in range(M):
        if j == 0:
            # 첫번째 행은 왼쪽에서 오는 경로가 없음
            dp1[j] += arr[i - 1][j]
            dp2[M - 1 - j] += arr[i - 1][M - 1 - j]
        else:
            # 위에서 오거나 왼쪽에서 오는 것 중 최대값
            dp1[j] += max(arr[i - 1][j], dp1[j - 1])
            # 위에서 오거나 오른쪽에서 오는 것 중 최대값
            dp2[M - 1 - j] += max(arr[i - 1][M - 1 - j], dp2[M - j])
    for j in range(M):
        arr[i][j] = max(dp1[j], dp2[j])
print(arr[-1][-1])
