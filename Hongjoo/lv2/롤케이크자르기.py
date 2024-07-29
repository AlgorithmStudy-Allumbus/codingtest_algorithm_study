"""
# 계수 정렬 idea 적용
"""

def solution(topping):
    answer = 0 # 공평하게 자를 수 있는 경우의 수
    # 0, graph
    forward = set()
    backward = dict()
    # 1. key 종류, value: toppping 중복 개수
    for t in topping:
        backward[str(t)]= backward.get(str(t),0)
        backward[str(t)] += 1
    print(backward)
    #2. forward vs backward
    for t in topping :
        # f 에서 t가 추가됨 == b에서 t 빠짐
        forward.add(t)
        backward[str(t)] -=1
        if backward[str(t)] == 0 :
            del backward[str(t)]
        
        # 토핑 종류 같은 경우 = 공평 한 경우
        if len(forward) == len(backward.keys()):
            answer+=1
        
    return answer