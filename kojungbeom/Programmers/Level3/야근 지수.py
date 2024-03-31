import heapq
def solution(n, works):
    # n: 남은 시간
    # works: 각 일에 대한 작업량을 나타낸 array
    # 야근피로도 = 야근 시작 시점에서 남은 일의 작업량을 제곱해서 더한것
    # works의 길이가 20,000 미만이니까.. O(n**2)까지도 Okay..?
    # 매번 정렬해야지 생각하고도 heap을 떠올리지못한 나를 탓하라.
    answer = 0
    works2 = [-w for w in works]
    heapq.heapify(works2)
    
    while n > 0:
        value = heapq.heappop(works2)
        if value != 0:
            value += 1
        n -= 1
        heapq.heappush(works2, value)
        
    answer = sum([(w * -1) ** 2 for w in works2]) 
    return answer