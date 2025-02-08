import heapq

population, centi_height, limit = map(int, input().split())

arr_heights = []
max_height = -1

for _ in range(population):
    heapq.heappush(arr_heights, -(int(input())))

if centi_height > -arr_heights[0]:
    print("YES")
    print(0)
    exit(0)

for i in range(limit):
    # 키가 가장 큰 거인 선택
    max_height = -(heapq.heappop(arr_heights))

    # 가장 큰 거인의 키가 1인 경우 뿅망치 무효화.
    if max_height == 1:
        heapq.heappush(arr_heights, -(max_height))
    else:
        heapq.heappush(arr_heights, -(max_height//2))

    max_height = -(heapq.heappop(arr_heights))

    if centi_height > max_height:
        print("YES")
        print(i+1)
        exit(0)
    heapq.heappush(arr_heights, -max_height)


print("NO")
print(max_height)


