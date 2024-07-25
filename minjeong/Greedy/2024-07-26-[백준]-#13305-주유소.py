import sys
input = sys.stdin.readline

# 초기화
n = int(input()) # n: 도시의 개수
road = list(map(int, input().split())) # 도로의 길이
oil_price = list(map(int, input().split())) # 리터당 가격

min_cost = 0 # 최저 비용
min_price = oil_price[0] # 첫번째 도시의 기름 가격

for i in range(n - 1):
    if oil_price[i] < min_price:  # 현재 도시에서의 기름 가격이 최소 가격보다 작으면 갱신
        min_price = oil_price[i]
    min_cost += min_price * road[i] # 현재 도시에서 다음 도시로 이동할 때 드는 비용을 추가

print(min_cost)

