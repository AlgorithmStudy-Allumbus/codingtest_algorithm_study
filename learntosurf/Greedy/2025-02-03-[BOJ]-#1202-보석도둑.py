import sys 
input = sys.stdin.readline
import heapq

N, K = map(int, input().split()) # 보석 개수, 가방 개수
jewels = [tuple(map(int, input().split())) for _ in range(N)] # (보석 무게, 보석 가격)
bags = [int(input()) for _ in range(K)] # 가방 무게 

# 오름차순 정렬 
jewels.sort()
bags.sort()

max_heap = []
total_v = 0
j = 0

for bag in bags: 
    # 현재 가방에 담을 수 있는 보석을 힙에 추가  
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(max_heap, -jewels[j][1]) # 가격을 음수로 저장
        j +=1
    # 현재 가방에서 가장 비싼 보석을 선택 
    if max_heap:
        total_v += -heapq.heappop(max_heap) # 음수로 저장한 값 되돌리기 

print(total_v)
