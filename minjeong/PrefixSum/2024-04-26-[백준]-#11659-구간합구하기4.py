import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
prefix = [0] * (N+1) 

# 누적합 구하기
for i in range(len(nums)):
    prefix[i+1] = nums[i] + prefix[i]

# 구간합 구하기 (누적합 - 구간)
for _ in range(M):
    start, end = map(int, input().strip().split())
    result = prefix[end] - prefix[start-1] # 누적
    print(result)