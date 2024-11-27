import sys
input = sys.stdin.readline

# 1. 입력받기
n = int(input())  # 아이들의 수 N 입력
lines = [int(input()) for _ in range(n)]  # 현재 줄 서 있는 상태 입력

# 2. DP 초기화
dp = [1] * n  # LIS를 계산하기 위한 초기화 (모든 값 1로 시작)

# 3. LIS 계산
for i in range(1, n):  # 현재 위치 i를 기준으로
    for j in range(i):  # i보다 앞에 있는 모든 j를 탐색
        if lines[i] > lines[j]:  # 앞 번호가 현재 번호보다 작을 때
            dp[i] = max(dp[i], dp[j] + 1)  # LIS 길이를 갱신

# 4. 가장 긴 증가하는 부분 수열의 길이 찾기
lis_length = max(dp)

# 5. 최소로 옮겨야 하는 아이들의 수 출력
print(n - lis_length)  