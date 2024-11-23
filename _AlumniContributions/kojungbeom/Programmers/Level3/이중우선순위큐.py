import heapq
def solution(operations):
    answer = []
    heap = []
    for o in operations:
        command, value = o.split()
        if command == "I":
            heapq.heappush(heap, int(value))
        else:
            if heap:
                if value == '1':
                    heap.sort()
                    heap.pop()
                elif value == '-1':
                    heapq.heappop(heap)
    if heap:
        answer = [max(heap), min(heap)]
    else:
        answer = [0, 0]
    return answer