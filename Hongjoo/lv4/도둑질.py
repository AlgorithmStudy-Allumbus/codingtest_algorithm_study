def solution(money):
    #1. 원형 탐색의 함정고려 -> 1번째 포함, 마지막만 포함
    # 3개 이상
    m1 = [0] + money[0:len(money)-1]
    m2 = [0] + money[1:len(money)]
    ms = [m1,m2]
    #2.점화식: 현제 위치 = MAX(이전, 전전 + 현위치)
    max_num = 0
    for c in ms :
        for i in range(2,len(c)):
            c[i] = max(c[i-1],c[i-2]+c[i])
        if max_num < c[len(c)-1]:
            max_num = c[len(c)-1]
    return max_num