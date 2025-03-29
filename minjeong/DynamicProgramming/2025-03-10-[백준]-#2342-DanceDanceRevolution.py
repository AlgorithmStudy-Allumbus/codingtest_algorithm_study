import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))

n = len(nums)
dp = [[[4*len(nums) for _ in range(5)] for _ in range(5)]
      for _ in range(len(nums))]
dp[0][0][0] = 0  # 초기값


def move(start, end):
    if start == 0:  # 0을 거침
        return 2
    if start == end:  # 같은 지점
        return 1
    if abs(start - end) % 2 == 0: # 짝수차이가 나면 반대지점
        return 4
    else:
        return 3


for i in range(n-1):
    start = nums[i]
    for left in range(5):
        for right in range(5):
            dp[i+1][left][start] = min(dp[i+1][left][start], dp[i][left][right] + move(right, start))
            dp[i+1][start][right] = min(dp[i+1][start][right], dp[i][left][right] + move(left, start))

print(min(map(min, dp[n-1])))