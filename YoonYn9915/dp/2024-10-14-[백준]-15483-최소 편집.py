import sys

# 두 문자열 입력
a = sys.stdin.readline()
b = sys.stdin.readline()

# 최소 편집 거리 계산을 위한 DP 테이블 생성
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

# 최소 편집 거리 계산
for i in range(len(a)+1):
    for j in range(len(b)+1):
        # 첫 번째 행일 경우
        if (i == 0):
            dp[i][j] = j
        # 첫 번째 열일 경우
        elif (j == 0):
            dp[i][j] = i
        else:
            # 현재 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
            if (a[i-1] == b[j-1]):
                dp[i][j] = dp[i-1][j-1]
            # 현재 문자가 다르다면,
            # 세 가지 경우[삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위)] 중에서 최솟값을 찾고 +1
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

print(dp[len(a)][len(b)])