import sys
input = sys.stdin.readline

# 1. 입력 처리
n = int(input())  # 수열의 크기
nums = list(map(int, input().split()))  # 수열 A

# 2. 증가 부분 수열 계산 (왼쪽 → 오른쪽)
inc = [1] * n
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            inc[i] = max(inc[i], inc[j] + 1)

# 3. 감소 부분 수열 계산 (오른쪽 → 왼쪽)
dec = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if nums[i] > nums[j]:
            dec[i] = max(dec[i], dec[j] + 1)

# 4. 가장 긴 바이토닉 수열의 길이 계산
result = 0
for i in range(n):
    result = max(result, inc[i] + dec[i] - 1)

# 5. 결과 출력
print(result)
