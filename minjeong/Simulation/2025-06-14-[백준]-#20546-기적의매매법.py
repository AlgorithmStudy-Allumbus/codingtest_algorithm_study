import sys
import math
input = sys.stdin.readline

money = int(input())
prices = list(map(int, input().split()))

# 준현이 (BNP)
jh_cash = money
jh_stock = 0
for price in prices:
    if jh_cash >= price:
        jh_stock += jh_cash // price
        jh_cash = jh_cash % price
jh_total = jh_cash + jh_stock * prices[-1]

# 성민이 (TIMING)
sm_cash = money
sm_stock = 0
for i in range(3, 14):
    # 3일 연속 상승
    if prices[i-3] < prices[i-2] < prices[i-1]:
        sm_cash += sm_stock * prices[i]
        sm_stock = 0
    # 3일 연속 하락
    elif prices[i-3] > prices[i-2] > prices[i-1]:
        can_buy = sm_cash // prices[i]
        sm_stock += can_buy
        sm_cash -= can_buy * prices[i]
sm_total = sm_cash + sm_stock * prices[-1]

# 결과 출력
if jh_total > sm_total:
    print("BNP")
elif jh_total < sm_total:
    print("TIMING")
else:
    print("SAMESAME")
