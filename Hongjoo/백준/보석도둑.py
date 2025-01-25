"""
# [BOJ] #1202. 보석 도둑
유형 - 그리디 , 우선큐 , 백준 

- 가방 1개에 보석 한개
"""
import sys
from collections import deque

# 1, jewel , bags의 값 입력 받기
total_jewels  , total_bags = map(int, sys.stdin.readline().split())
jewels = [[] for _ in range(total_jewels)]
bags = [ 0 for _ in range(total_bags)]

for i in range(total_jewels) :
    jewels[i] = list(map(int, sys.stdin.readline().split()))

for j in range(total_bags) :
    bags[j] = int(sys.stdin.readline())



#2. 정렬 
#jewel 은 비싼 가격-> 가벼운 무게 순으로 정렬
# bags 은 무게가 무거운 순으로 정렬 
jewels = sorted(jewels , key=lambda x : ( -x[1] , x[0]))
bags = sorted(bags) # max = -1



# #3. 그리디 - 현재 가장 비싼 jewel 순으로 가장 작은 가방에서 넣기
prices = [] 

for  i in range(total_jewels) : 
    jewel_weight , jewel_price  = jewels[i]
    # 현재 jewel 의 무게가 최대 bags 보다 무거우면 =>  끝 
    if jewel_weight > max(bags) :
        continue
    else : # 아니면 => 가방에 바로 넣기
        # jewel의 무게와 가장 가까운 fit한 최적의 bags 찾기
        # diff = 1000000000 ; fit_idx = -1 
        # for k in range(len(bags)) :
        #     curr_diff = bags[k]-jewel_weight
        #     if  curr_diff > 0 and diff > curr_diff  :
        #         diff = curr_diff ; fit_idx= k
        
        for k in range(len(bags)) :
            if bags[k] >= jewel_weight : # 현 jewle weight를 감당 가능한 최소 가방  
                prices.append(jewel_price)
                bags.pop(k) # 나가기 
                break
        if len(bags) == 0 : # 비어있다
            break # 종료
#         print(f"current bags {bags} : jewel {jewel_price} / {jewel_weight}")
#         print(prices)
# print(f"price : {sum(prices)}")
print(sum(prices))