def solution(s):
    stack = []
    for c in s:
        # 스택이 비어있는 경우
        if len(stack) == 0:
            stack.append(c)
        # 가장 최근 문자와 비교
        elif stack[-1] == c:
            stack.pop()
        # 문자가 같지 않아서, 삭제할 필요가 없을 경우
        else:
            stack.append(c)
            
    # 짝이 다 맞았다면 스택에 남는 것이 없기 때문에 비어있고, 짝이 맞지 않았다면 스택에 문자가 남아있다.
    # 따라서 스택의 길이가 0인지 비교
    if len(stack) == 0:
        return 1
    else:
        return 0