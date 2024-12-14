'''
BOJ #13335. 수강과목 (실버1)
https://www.acmicpc.net/problem/13335
유형: 구현, 시뮬레이션, 자료구조

출처:https://velog.io/@mimmimmu/12%EC%A3%BC%EC%B0%A8-%EB%B0%B1%EC%A4%80-13335%EB%B2%88-%ED%8A%B8%EB%9F%AD-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''


from collections import deque

n, w, L = map(int, input().split())
cars = list(map(int, input().split()))

queue = deque()
for _ in range(w):
    queue.append(0)

time = 0
idx = 0
while idx < n:
    time += 1
    queue.popleft()

    if sum(queue) + cars[idx] <= L:
        queue.append(cars[idx])
        idx += 1
    else:
        queue.append(0)

while queue:
    time += 1
    queue.popleft()

print(time)
