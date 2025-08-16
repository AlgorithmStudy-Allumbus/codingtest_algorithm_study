import sys
input = sys.stdin.readline

N, C = map(int, input().split())  # N: 집 개수, C: 공유기 개수
houses = [int(input()) for _ in range(N)]  # 집 좌표 리스트
houses.sort()

left = 1  # 최소 거리
right = houses[N-1] - houses[0]
result = 0

while left <= right:
    mid = (left + right) // 2  # 현재 설정된 거리
    cnt = 1  # 공유기 최소 1대
    check = houses[0]

    for i in range(N):
        if houses[i] - check >= mid: # 현재 설정된 거리 이상이면 공유기 개수 늘리기
            cnt += 1
            check = houses[i]
    if cnt >= C:  # 공유기 설치 수가 C 이상이면, 공유기간 거리 늘리기
        left = mid + 1
        result = max(result, mid)
    else:  # 공유기 설치 수가 C보다 미만이면, 공유기간 거리 줄이기
        right = mid - 1

print(result)