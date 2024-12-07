import sys
input = sys.stdin.readline

# 1. 입력받기
N, K = map(int, input().split())    # N: 최대 공부 시간, K: 과목 수
lectures = [[0, 0]]                 # 수강 과목 리스트 (중요도, 필요한 공부 시간)
for _ in range(K):
    lectures.append(list(map(int, input().split())))  # 중요도와 공부 시간

# 2. DP 초기화
dp = [[0] * (N + 1) for _ in range(K + 1)]

# 3. DP 채우기(냅색 알고리즘)
for i in range(1, K + 1):           # 각 과목에 대해
    importance = lectures[i][0]     # 중요도
    time = lectures[i][1]           # 필요한 공부 시간
    for j in range(1, N + 1):       # 공부 시간 1부터 N까지
        if j >= time:               # 현재 공부 시간으로 이 과목을 선택 가능 -> 더 큰 값으로 갱신
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + importance)
        else:                       # 충족할 수 없다 -> 이전 값 유지
            dp[i][j] = dp[i-1][j]

# 4. 결과 출력
print(dp[K][N])