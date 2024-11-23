def solution(s):
    answer = 0
    opps = 1
    
    if s[0] == "+" :
        opps = 1
        answer = int(s[1:])
    elif s[0] == "-" :
        opps = 0
        answer = int(s[1:]) * (-1)
    else :
        answer = int(s)
           
    
    return answer