'''
요구사항
1. 매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나갈 때, 최소한 몇 번의 비교가 필요한지를 계산

1. 아이디어
- A개, B개 두 묶음의 카드를 비교하는데 A+B번 비교해야 함.
- 비교한 횟수를 누적시켜 최소값을 찾아야 하므로 비교횟수가 가장 작은 것들부터 시작해야 함.
- A, B, C 3개의 카드 묶음이 있고 A < B < C라면, (A+B) + ((A+B) + C)가 최소값이다.

2. 시간복잡도
- (1 ≤ N ≤ 100,000)
- O(N + (N-1) * logN), 대략 O(NlogN)으로 시간복잡도 만족.

3. 구현
3.1 입력받기
3.2 카드 묶음 정렬(우선순위 큐에 저장)
3.3 가장 카드가 적은 묶음 2개를 뽑아 더한 값을 정답변수에 누적시키고 다시 우선순위큐에 저장
3.4 우선순위 큐가 하나 남을때까지 반복
3.5 정답 출력
'''

import sys
import heapq

inp = sys.stdin.readline

N = int(inp().strip())
arr = []
answer = 0

for _ in range(N):
    arr.append(int(inp().strip()))

# 매번 최소 카드 묶음 2개를 뽑기 위해 heap 사용
heapq.heapify(arr)

while len(arr) > 1:
    min1 = heapq.heappop(arr)
    min2 = heapq.heappop(arr)

    answer += min1 + min2
    heapq.heappush(arr, min1 + min2)

print(answer)
