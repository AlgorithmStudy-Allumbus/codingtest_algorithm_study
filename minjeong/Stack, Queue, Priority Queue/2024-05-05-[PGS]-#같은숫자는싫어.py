def solution(arr):
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0: # 스택이 비어 있다면 추가
            stack.append(arr[i])
        else: # 스택이 비어있지 않다면
            if arr[i] != stack[-1]: # 가장 최근의 스택값과 현재 값을 비교하고, 다를 경우에만 스택에 추가
                stack.append(arr[i])
                
    return stack