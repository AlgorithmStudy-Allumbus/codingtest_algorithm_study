"""
num1 =  [1,2,3,...n ] * len(answers) 반복
num2  = [2, 1, 2, 3, 2, 4, 2, 5] 반복
num3 = [3,3,1,1,2,2,4,4,5,5 반복

idea : 답 point = 문제 번호 % 패턴 개수

"""
def solution(answers):
    answer = [0] *3
    num1 = [1,2,3,4,5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    # 0. 패턴 정의하기
    patterns = [num1, num2, num3] 
    # 1.정답 개수 세기
    for i in range(len(answers)):
        for j in range(3):
            pattern = patterns[j]
            p= i % len(pattern) # point이용
            if pattern[p] == answers[i]:
                answer[j]+=1

    #2. 가장 많이 맞춘 사람(중복 고려)
    max_idx = []
    max_num = max(answer) #2-1 가장 많이(max) 맞춘 개수 찾기
    for i in range(len(answer)) : # 2-2. 3명 돌면서 max 중복 값 가진 사람 idx 색출 -> 추가
        if max_num == answer[i] :
            max_idx.append(i+1)
    print(max_idx)
        
    
    return max_idx