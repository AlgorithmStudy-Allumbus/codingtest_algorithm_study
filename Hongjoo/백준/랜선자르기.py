K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]
# 1. 범위 초기화
start = 1
end = max(lines)
#2. 이분 탐색
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid

    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)