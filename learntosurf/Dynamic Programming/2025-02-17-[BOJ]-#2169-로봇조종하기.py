import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split()) # 지도의 크기 
grid = [list(map(int, input().split())) for _ in range(N)] # 각 지역의 가치

# DP 테이블
dp = [[0] * M for _ in range(N)]

# 첫 번째 행 초기화 (왼쪽에서 오른쪽으로 누적합)
dp[0][0] = grid[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + grid[0][j] # (0,1)→(0,2)→(0,3)..

# 두 번째 행부터 (왼쪽에서 오른쪽, 오른쪽에서 왼쪽으로 진행)
for i in range(1, N):
    left_to_right = [0] * M
    right_to_left = [0] * M

    # 왼쪽 → 오른쪽
    left_to_right[0] = dp[i-1][0] + grid[i][0] # 첫번째 열은 위쪽에서만 올 수 있음 
    for j in range(1, M): # 두번째 열부터는 위쪽, 왼쪽에서 오는 경우 중 선택
        left_to_right[j] = max(dp[i-1][j], left_to_right[j-1]) + grid[i][j]

    # 오른쪽 → 왼쪽
    right_to_left[M-1] = dp[i-1][M-1] + grid[i][M-1] # 마지막 열은 위쪽에서만 올 수 있음 
    for j in range(M-2, -1, -1): # 그 다음 열부터는 위쪽, 오른쪽에서 오는 경우 중 선택
        right_to_left[j] = max(dp[i-1][j], right_to_left[j+1]) + grid[i][j]

    # 두 개의 배열을 비교해 dp[i][j] 갱신
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])

# 정답 출력
print(dp[N-1][M-1]) # 마지막 위치에 저장된 값이 탐사한 지역 가치 합의 최대값