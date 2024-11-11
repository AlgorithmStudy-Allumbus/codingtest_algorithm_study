from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque([(x, 0)])  # (현재 수, 연산 횟수)

    while queue:
        current, count = queue.popleft()

        if current == y:
            return count

        if current > y:
            continue

        if current not in visited:
            visited.add(current)
            queue.append((current + n, count + 1))
            queue.append((current * 2, count + 1))
            queue.append((current * 3, count + 1))

    return -1