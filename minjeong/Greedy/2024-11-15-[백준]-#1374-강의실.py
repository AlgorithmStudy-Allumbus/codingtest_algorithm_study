import sys
import heapq
input = sys.stdin.readline

n = int(input())
rooms = []

# 강의 정보 입력받기
for _ in range(n):
    no, start, end = map(int, input().split())
    rooms.append((start, end))

# 시작 시간 기준으로 정렬
rooms.sort()

# 최소 힙 초기화
min_heap = []

for start, end in rooms:
    # 현재 강의가 가장 빨리 끝나는 강의 이후 시작하면 해당 강의 종료
    if min_heap and min_heap[0] <= start:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, end)

# 필요한 최소 강의실 개수는 힙의 크기
print(len(min_heap))