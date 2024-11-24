import sys
input = sys.stdin.readline

# 1️⃣ 입력 받기
n = int(input())  # 수열의 크기
nums = list(map(int, input().split()))  # 수열
dp = [1] * n  # DP 배열 초기화 (모든 원소 길이 1로 초기화)

# 2️⃣ DP 계산
for i in range(n):  # 현재 원소
    for j in range(i):  # 이전 원소들과 비교
        if nums[i] < nums[j]:  # 감소 조건
            dp[i] = max(dp[i], dp[j] + 1)

# 3️⃣ 결과 출력
print(max(dp))  # dp 배열 중 가장 큰 값 출력
