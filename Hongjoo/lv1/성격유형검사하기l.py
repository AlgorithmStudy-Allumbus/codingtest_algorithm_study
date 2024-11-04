"""
1 - R,T 
2 - C,F
3,- J , M
4 - A, N

=> 7 : +3N , 6 : +2N , 5 : +1N  4: 0  , 3 : +A , 2: +2A , 1 : + 3A (비동의)
"""

def solution(survey, choices):
    answer = ''
    vote = list()
    for i in range(len(survey)) : 
        a = survey[i][0] ; b = survey[i][1] #  비동의 , 동의
        target = ''
        tmp = choices[i]-4

        if tmp > 0 : # 양수 -> 동의
            target = b 
        elif tmp < 0 : # 음수 -> 비동의
            target = a 
            tmp = tmp * (-1)
        else : # tmp == 0
            continue

        # vote에 여부 확인 
        if len(vote) == 0 : # 초기화
            vote.append([target,tmp])
            continue
        for k in range(len(vote)) :
            if  vote[k][0] == target : # 있으면 -> 더하기
                vote[k][1] += tmp
                break
            if k >= len(vote)-1 : 
                 # 없으면 -> 업데이트
                vote.append([target,tmp])

    answer_list = [0,0,0,0]
    twin= [["R","C" ,"J" ,"A"] ,["T" , "F" , "M" , "N"]]
    for k in range(len(vote)) :
        if vote[k][0] in twin[0]: # 음수
            answer_list[twin[0].index(vote[k][0])]-= vote[k][1]
        elif vote[k][0] in twin[1]: # 양수
            answer_list[twin[1].index(vote[k][0])] += vote[k][1]

    
    for j in range(len(answer_list)):
        if answer_list[j] > 0 :# 양수
            answer+= twin[1][j]
        else :# 음수
            answer+= twin[0][j]
         
    return answer