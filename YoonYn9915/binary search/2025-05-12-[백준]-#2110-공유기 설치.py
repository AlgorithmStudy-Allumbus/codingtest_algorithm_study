'''

1. 아이디어
 - C개의 공유기를 N개의 집에 설치해서, 가장 인접한 두 공유기 사이의 거리 중 최댓값.
 - 가장 인접한 두 공유기 사이의 거리를 구하기 위해 최소거리를 설정하고, 그 최소거리만큼 띄워서 공유기 설치
 - 설치한 공유기가 c개 미만이면 최소거리를 낮춤, 설치한 공유기가 c개 이상이면 최소거리를 늘림.(최댓값을 찾기 위해서)
 - 이분탐색 알고리즘을 사용하여 '(1, 가장 오른쪽 집 - 가장 왼쪽 집)' 범위에서 최소거리 찾기
2. 시간 복잡도
 - N(2<= N <= 200,000), M(2 <= M <= N) 일때,
   완전탐색으로 N개의 집 중 공유기를 설치할 M개를 조합하는 시간복잡도는 O(NCM)이고
   조합한 배열에서 인접한 두 공유기 사이의 거리를 구하는 것은 O(M-1)이므로 O(NCM * (M-1))은 시간 초과.
 - 이분탐색은 O(N*logN)이므로 N이 200,000일때도 가능.

3. 구현
3-1. 입력받기
3-2. 배열 정렬
3-3. 이분탐색
    - start, end, 를 각각 1과 arr[n-1] - arr[0]로 초기화.
    - 공유기를 최소거리만큼 띄워서 설치.
    - 설치 공유기 개수가 c보다 작으면 end를 mid로 설정.
    - 설치 공유기 개수가 c이상이면 start를 mid+1로 설정.
    - start와 end가 교차하면 종료

'''

import sys

inp = sys.stdin.readline


def install_router(mid):
    # 가장 왼쪽의 집은 무조건 설치
    router_count = 1
    previous_house = house[0]

    # 이전에 공유기를 설치했던 집 좌표 + mid <= 현재 집 좌표인지 확인
    for i in range(N):
        if previous_house + mid <= house[i]:
            router_count += 1
            previous_house = house[i]

    return router_count


# 입력받기
N, C = map(int, inp().split())
house = list(map(int, [inp() for _ in range(N)]))

# 정렬
house.sort()

# 인접한 두 집의 가능한 최소거리와 최대거리
start = 1
end = house[N - 1] - house[0]

# 정답
answer = 0

while start <= end:
    # 이분탐색을 위한 mid
    mid = (start + end) // 2

    # 설치한 공유기 개수를 반환
    router_count = install_router(mid)

    if router_count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
