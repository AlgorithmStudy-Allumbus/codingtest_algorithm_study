import sys
input = sys.stdin.readline

# 입력값 저장
n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

# DP 처리
for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
# 최대 합
print(max(arr[n-1]))