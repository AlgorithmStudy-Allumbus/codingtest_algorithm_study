import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().strip().split()))
dp = [0] * (n+1) # dp테이블 1부터 시작할 예정이므로, n+1크기로 초기화

for i in range(1, len(dp)):
    # 점화식: max(누적값, 현재값)
    dp[i] += max(dp[i-1] + nums[i-1], nums[i-1]) # 지금까지 누적한 값과 현재값 중에서 더 큰 값으로 dp에 저장

print(max(dp[1:])) # nums가 모두 음수일 경우, 초기화할 때 사용한 0이 최댓값이 되므로 실제 데이터가 저장되는 1번째 인덱스부터 최댓값을 찾음

