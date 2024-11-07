from itertools import combinations
from math import comb

cards = [i for i in range(1, 11)] * 2 # 20장의 카드 리스트 구성 (1~10 2장씩)

def judge(card1, card2):
    # 땡: 두 카드가 같을 경우 
    if card1 == card2:
        return f"{card1}땡"
    
    # 끗: 땡이 아닐 경우 두 카드의 합을 10으로 나눈 나머지 
    else: 
        sum_value = (card1 + card2) % 10 
        return f"{sum_value}끗"

# 족보 우선순위 설정 (높은 족보일수록 더 높은 값)
rank_order = {f"{i}땡": 10-i for i in range(1, 11)}
rank_order.update({f"{i}끗": -i for i in range(10)})  # 끗 족보는 숫자가 클수록 강하지만 땡보다는 약함
                                                     # 끗 족보에는 음수를 사용해 낮은 값을 할당하여, 땡 족보보다 낮은 순위로 설정

def win_probability(y_card1, y_card2):
    win_count = 0 
    total_count = 0
    
    y_rank = rank_order[judge(y_card1, y_card2)] # 영학이의 족보
    
    # 상대방이 2장을 뽑는 모든 경우의 수 
    for opp_card1, opp_card2 in combinations(cards, 2):
        
        remaining_cards = cards.copy()
        remaining_cards.remove(opp_card1)
        remaining_cards.remove(opp_card2)
        
        opp_rank = rank_order[judge(opp_card1, opp_card2)] # 상대방의 족보
        
        total_count += 1
        
        if y_rank > opp_rank: # 영학이가 이기는 경우의 수 
            win_count += 1
        
    probability = win_count / total_count
    return f"{probability:.3f}" # 소수점 셋째 자리까지 출력

y_card1, y_card2 = map(int, input().split())
print(win_probability(y_card1, y_card2))

# print(win_probability(1, 1)) # 0.941
# print(win_probability(1, 2)) # 0.275
# print(win_probability(1, 9)) # 0.000
# print(win_probability(10, 10)) # 1.000