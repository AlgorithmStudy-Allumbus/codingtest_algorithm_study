import sys
import heapq

input = sys.stdin.readline

# 입력
N, H, T = map(int, input().split())  # N: 거인의 나라 인구 수, H: 센티의 키, T: 뿅망치 횟수 제한
heights = []

for _ in range(N):
    heapq.heappush(heights, -int(input()))  # 최대힙을 위해 음수로 저장

cnt = 0  # 사용한 뿅망치 개수

# 뿅망치 사용
while cnt < T:
    tallest = -heapq.heappop(heights)  # 가장 큰 키를 가져옴

    if tallest < H:  # 센티보다 작은 거인이 나오면 즉시 종료
        print(f"YES\n{cnt}")
        break

    # 키가 1이면 더 줄일 수 없음
    if tallest == 1:
        heapq.heappush(heights, -1)
    else:
        heapq.heappush(heights, -(tallest // 2))

    cnt += 1
else:
    # 뿅망치 사용을 모두 소진한 경우
    tallest_after = -heapq.heappop(heights)  # 남아 있는 가장 큰 키
    if tallest_after < H:
        print(f"YES\n{cnt}")
    else:
        print(f"NO\n{tallest_after}")
