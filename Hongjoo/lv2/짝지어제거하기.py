def solution(s):
    answer = 1
    match_box = list()
    for i in range(len(s)) :
        match_box.append(s[i])
        if len(match_box) > 1 :
            if match_box[-2] == match_box[-1] :
                match_box.pop()
                match_box.pop()

    if len(match_box) > 0 : 
        return 0
    
    return answer