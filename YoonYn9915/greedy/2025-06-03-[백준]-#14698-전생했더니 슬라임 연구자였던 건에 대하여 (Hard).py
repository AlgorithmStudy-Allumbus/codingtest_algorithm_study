'''
요구사항
1. A만큼의 에너지를 가진 슬라임과 B만큼의 에너지를 가진 슬라임을 합성하려면 A × B 만큼의 에너지 필요.
2. N마리의 슬라임들을 적절히 합성해서 1마리의 슬라임으로 만들때, 필요한 에너지 값을 모두 곱한 값을 최소로 만든다.
3. 슬라임을 모두 합성했을 때 청구될 비용의 최솟값을 1, 000, 000, 007로 나눈 나머지를 출력한다. 에너지가 전혀 필요하지 않은 경우엔 1 을 출력한다.

1. 아이디어
곱의 누적곱이 최소가 되게 하려면 곱셈의 결과가 최소가 나오게 해야 함. 즉 큰 수를 가장 적게 곱하고
되도록 작은수 X 작은수 형태로 풀이. 따라서 각 경우마다 가장 작은 두 수를 그리디하게 뽑아서 곱하고 누적곱해주면 된다.

2. 시간복잡도
슬라임 수 N (1 ≤ N ≤ 60), i번째 슬라임의 에너지 Ci (2 ≤ Ci ≤ 2 × 1018)일때,
모든 테스트 케이스에 대한 N 의 총합이 1, 000, 000을 넘지 않음으로 테스트 케이스의 수는 최대 500,000.
즉 O(test_case * (N-1)) == O(500,000 * 59)로 만족.

3. 구현
3-1. 입력받기
3-2. N-1번 가장 작은 두 수를 뽑는다.
3-3. 두 수를 곱하고 정답변수에 누적시킨다.
3-4. 곱한 두 슬라임을 제거하고, 새 슬라임을 추가한다.
3-5. 정답 출력

'''


import heapq
import sys

inp = sys.stdin.readline
MOD = 1000000007

test_case = int(inp())

for _ in range(test_case):
    N = int(inp())
    arr = list(map(int, inp().split()))

    if N == 1:
        print(1)
        continue

    hq = []
    for num in arr:
        heapq.heappush(hq, num)

    result = 1
    while len(hq) > 1:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        energy = a * b
        result = (result * energy) % MOD
        heapq.heappush(hq, energy)

    print(result)