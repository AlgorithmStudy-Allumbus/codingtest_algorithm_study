def solution(s):
    '''
    규칙 
    - idx = 1 : "(" , 마지막 ")"
    '''
    answer = True

    box_match = list()
    if len(s) %2 != 0:  # 규칙 1 : 짝수개 
        return False 
    for i in range(len(s)) : 
        # 규칙2 : first = "(" , end = ")" 로 구성됨
        if i == 0 and s[i] == ")" : 
            return False
        elif i == len(s)-1 and s[i] == "(" :
            return False
        # 규칙 3 : stack 안에서 "()" 조합이 완성되면 pop 하기
        box_match.append(s[i])
        if len(box_match) > 1 : # 2개 이상 들어가 있으면 
            if  box_match[-2] == "(" and box_match[-1] == ")" : # matching 되면 
                x =box_match.pop()
                y =box_match.pop()
    # 규칙 3-1 : box_match 가 남아 있으면 False, 없으면 True
    if len(box_match) > 0 : 
        return False 
    
    return True                  