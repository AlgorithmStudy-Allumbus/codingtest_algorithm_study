import sys
input = sys.stdin.readline

# 1. 입력받기
n = int(input())  # 상자의 개수
boxes = list(map(int, input().split()))  # 상자의 크기 배열

# 2. DP 초기화
dp = [1] * n  # 모든 상자는 최소 자기 자신을 포함하므로 초기값 1

# 3. DP 계산
for i in range(n):  # i는 현재 상자를 가리킴
    for j in range(i):  # j는 i 이전의 상자를 가리킴
        if boxes[j] < boxes[i]:  # j번째 상자가 i번째 상자 안에 들어갈 수 있는 경우
            dp[i] = max(dp[i], dp[j] + 1)  # dp 갱신: 기존 값 vs j까지의 값 + 1

# 4. 정답 출력
print(max(dp))  # dp 배열에서 최대값이 한 번에 넣을 수 있는 최대 상자 개수