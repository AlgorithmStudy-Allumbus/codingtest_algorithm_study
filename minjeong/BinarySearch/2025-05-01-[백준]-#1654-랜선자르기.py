import sys
input = sys.stdin.readline

K, N = map(int, input().split())  # K: 기존 랜선 수, N: 필요한 랜선 수
arr = [int(input()) for _ in range(K)]

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2  # 현재 시도할 랜선 길이
    cnt = sum(x // mid for x in arr)  # 해당 길이로 만들 수 있는 랜선 개수

    if cnt >= N:
        start = mid + 1  # 더 길게 잘라도 됨
    else:
        end = mid - 1  # 너무 길어서 N개 못 만듦

print(end)  # 조건을 만족하는 최대 길이
