import math
def solution(progresses, speeds):
    answer = [] # 정답리스트
    stack = []  # 스택
    feat_count = len(progresses) # 총 기능 개수
    for i in range(feat_count):
        day = math.ceil((100 - progresses[i]) / speeds[i]) # 걸리는 날짜 계산, 무조건 올림
        # 스택이 비어 있거나, 처음 스택에 들어간 값보다 걸리는 날짜가 같거나 작다면 push
        if not stack or stack[0] >= day: 
            stack.append(day)
        # 아니라면 스택의 길이를 정답리스트에 추가하고 스택에 새로운 값으로 대치
        else:
            answer.append(len(stack))
            stack = [day]
    answer.append(len(stack)) # 마지막에 추가하지 못한 answer 추가
    return answer
