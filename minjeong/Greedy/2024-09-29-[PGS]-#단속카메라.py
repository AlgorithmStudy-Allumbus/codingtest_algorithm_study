import heapq

def solution(routes):
    routes.sort(key=lambda x:x[0])

    answer = 0
    h = [30001]
    for r in routes:
        earliestend = heapq.heappop(h)
        if r[0] > earliestend:
            answer += 1
            h.clear()
        else:
            heapq.heappush(h, earliestend)
        heapq.heappush(h, r[1])
    else:
        if len(h) != 0:
            answer += 1
    return answer