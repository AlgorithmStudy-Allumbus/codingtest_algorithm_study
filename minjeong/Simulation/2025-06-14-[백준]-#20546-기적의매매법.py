import sys
import math
input = sys.stdin.readline

"""
준형: BNP
- 첫 날 최대치를 사고, 절대 매도하지 않는다.

성민: Timing
- 전량 매수 Or 전량매도
- 3일 연속 가격이 전일대비 상승할 경우 -> 전량매도. (전일과 오늘의 주가가 동일한 것은 가격 상승 아님)
- 3일 연속 가격이 전일대비 하락하는 경우 -> 전량 매수. (전일과 오늘의 주가가 동일한 것은 가격 하락 아님)

두 사람에게 주어진 현금은 동일하다.2021년 1월 14일의 자산이 더 많은 사람이 승리한다.
준현이가 이기면 BNP, 성민이가 이기면 TIMING, 동점일 경우 SAMESAME이다.
자산 = 현금 + 1월 14일 주가 * 주식 수

준형: 10주 -> 0 + 38 * 10 = 380 / 1주. 14원
성민: 
"""

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
