def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5] # 1번 수포자가 찍는 방식
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] # 2번 수포자가 찍는 방식
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자가 찍는 방식
    scores = [0, 0, 0] # 각각 1번, 2번, 3번의 점수를 담은 리스트
    
    for i in range(len(answers)): # 시험 문제의 정답 개수만큼 반복
        # 정답인지 판별. 이때 찍는 방식의 크기를 넘어가면 나머지 연산을 이용해 반복할 수 있도록 처리
        if p1[i%(len(p1))] == answers[i]:
            scores[0] += 1
        if p2[i%(len(p2))] == answers[i]:
            scores[1] += 1
        if p3[i%(len(p3))] == answers[i]:
            scores[2] += 1

    if scores.count(max(scores)) == 3: # 3명이 동점인 경우
        answer = [1,2,3]
    elif scores.count(max(scores)) == 2: # 2명이 동점인 경우
        # 최고점 한 사람 찾은 후, 그 사람의 점수를 0점으로 바꾸고, 다시 최고점을 찾는다.
        answer.append(scores.index(max(scores))+1) 
        scores[scores.index(max(scores))] = 0
        answer.append(scores.index(max(scores))+1)
    else: # 최고점이 1명만 있는 경우
        answer = [scores.index(max(scores))+1]
        
    return answer