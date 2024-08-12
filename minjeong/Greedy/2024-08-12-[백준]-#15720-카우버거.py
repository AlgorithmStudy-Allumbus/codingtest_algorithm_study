import sys
input = sys.stdin.readline

burgers, sides, drinks = map(int, input().split())
burger_prices = list(map(int, input().split()))
sides_prices = list(map(int, input().split()))
drinks_prices = list(map(int, input().split()))

# 세트 할인이 적용되기 전 가격
before_price = sum(burger_prices) + sum(sides_prices) + sum(drinks_prices)

# 세트 할인이 적용된 후 최소 가격 계산
burger_prices.sort(reverse=True)
sides_prices.sort(reverse=True)
drinks_prices.sort(reverse=True)

count = min(burgers, sides, drinks)
after_price = 0

# 세트 할인이 적용된 부분
for i in range(count):
    set_price = burger_prices[i] + sides_prices[i] + drinks_prices[i]
    after_price += set_price * 0.9  # 10% 할인 적용

# 세트 할인이 적용되지 않은 부분
after_price += sum(burger_prices[count:]) + sum(sides_prices[count:]) + sum(drinks_prices[count:])

# 결과 출력
print(before_price)
print(int(after_price))