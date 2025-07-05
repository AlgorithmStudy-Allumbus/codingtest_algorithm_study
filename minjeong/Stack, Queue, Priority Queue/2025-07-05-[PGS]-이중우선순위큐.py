import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    number_count = {}  # 각 숫자가 큐에 몇 번 남았는지 카운트
    size = 0  # 현재 큐에 남아있는 총 원소 수

    for op in operations:
        cmd, num_str = op.split(' ')
        num = int(num_str)

        if cmd == 'I':
            # 삽입
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            number_count[num] = number_count.get(num, 0) + 1
            size += 1
        else:  # cmd == 'D'
            if size == 0:
                # 큐가 비어있다면 연산 무시
                continue

            if num == 1:
                # 최댓값 삭제
                while max_heap:
                    x = -heapq.heappop(max_heap)
                    if number_count.get(x, 0) > 0:
                        # num이 1번 이상 등장했다면, 카운트 반영
                        number_count[x] -= 1
                        size -= 1
                        break
            else:
                # num == -1, 최솟값 삭제
                while min_heap:
                    x = heapq.heappop(min_heap)
                    if number_count.get(x, 0) > 0:
                        # num이 1번 이상 등장했다면, 카운트 반영
                        number_count[x] -= 1
                        size -= 1
                        break

    # 연산 후 큐가 비어있다면 [0, 0]
    if size == 0:
        return [0, 0]

    # 남아있는 최댓값 찾기
    max_value = 0
    while max_heap:
        x = -heapq.heappop(max_heap)
        if number_count.get(x, 0) > 0:
            max_value = x
            break

    # 남아있는 최솟값 찾기
    min_value = 0
    while min_heap:
        x = heapq.heappop(min_heap)
        if number_count.get(x, 0) > 0:
            min_value = x
            break

    return [max_value, min_value]