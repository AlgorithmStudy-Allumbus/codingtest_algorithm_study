import sys

inp = sys.stdin.readline

n = int(inp())

roads = list(map(int, inp().split()))
oil_prices = list(map(int, inp().split()))

# 최소 비용
answer = 0
# 현재 도시
loc = 0

while True:
    # 현재 도시보다 기름값이 적은 곳 찾기
    for i in range(loc + 1, n):
        if oil_prices[loc] > oil_prices[i] or i == n - 1:
            # 이곳까지 가기 위해 현재 도시에서 주유하면서 비용 소모
            # 현재 도시의 기름값 * i번 도시까지 가야 할 거리
            answer += oil_prices[loc] * sum(roads[loc:i])
            loc = i
            break

    if loc == n - 1:
        break

print(answer)