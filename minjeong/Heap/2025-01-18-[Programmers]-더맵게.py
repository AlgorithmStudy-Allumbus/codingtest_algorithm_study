import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:

        if scoville[0] >= K:
            return answer
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        answer += 1
        heapq.heappush(scoville, mix_scoville)

    if scoville[0] >= K:
        return answer
    else:
        return -1