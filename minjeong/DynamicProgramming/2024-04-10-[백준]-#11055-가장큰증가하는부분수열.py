import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n
dp[0] = nums[0]


for i in range(len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+nums[i])
        else:
            dp[i] = max(dp[i], nums[i])

    print(dp)
print(max(dp))
