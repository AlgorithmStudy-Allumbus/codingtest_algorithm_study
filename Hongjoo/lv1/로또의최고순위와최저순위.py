"""
6/range(1,45+1)
최고 순위, 최저 순위
1. 알수 없는 번호 개수: 0의 개수 => unknown_n
2. 최저 순위 = 6- (1개,0개 == 0 개로 취급, 현재 맞는 개수)
3. 최고 순위 = 6- 현재 맞은 개수
"""
def solution(lottos, win_nums):
    answer = []
    #1. 0의 개수
    correct= 0 ; unknown = 0
    #2. 알수 없는 개수, ,현재 맞은 개수
    for i in range(len(lottos)):
        if lottos[i] == 0 :
            unknown += 1
        elif lottos[i] in win_nums : 
            win_nums.remove(lottos[i])
            correct+=1
    #3. 순위 = 7- 맞은 개수(1개 맞은 개수 == 0개 맞은 개수 = 1로 취급)
    for c in [correct+unknown,correct] :
        if c == 0 :
            c= 1
        rank = 7-c
        answer.append(rank)
    return answer