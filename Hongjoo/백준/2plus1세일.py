"""
input : 총 유제품 수 N , 각 제품 가격 
goal : 모두 살때 최소 비용
Condition
1. 3개 중 가장 싼것만 무료, 나머지 2개는 가격 지불 

# Flow(greedy)
1. 3개씩 묶기 
    - 값이 큰 놈들 순으로 정렬 
2. 각 묶음 별 제출 가격 count 하기 

문제 : https://www.acmicpc.net/problem/11508
"""

import sys
input = sys.stdin.readline
n = int(input())
products = list()
# 1. price 입력 받기 
for  i in range(n):
    each_price = int(input())
    products.append(each_price)

# 2. 가격 비싼 순 = priority으로 item 정렬
products = sorted(products , reverse= True)
print(products)
# 2. for 문으로 총 price  계산하기
# 이때 item 3개 묶음이 충족 되면, 3개중 최소 가격을 전체 price 에서 빼기 
bags = list()
total = 0 
for item in products : 
    if len(bags) < 3 :  
        bags.append(item)
        total += item 
        # print(bags)
    if len(bags) == 3 : 
        free =  min(bags)
        total -= free
        bags = [] 
print(total)
