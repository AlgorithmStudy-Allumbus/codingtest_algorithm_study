def solution(food):
    answer = ''
    # 1. find sub that is one person will eat order 
    sub = ""
    re_sub = ""
    count =0
    for i in range(1, len(food)):
        count = food[i]//2
        for j in range(count):
            sub+=str(i)
    for k in sub[::-1]:
        re_sub += k
    
    answer = sub + "0" + re_sub
        
    return answer