def sepatate_uv(p): #  문자열 p를 두 "균형잡힌 괄호 문자열" u, v로 분리
    
    open_bracket = 0    # (
    close_bracket = 0   # )
    for i in range(len(p)):
        if p[i] == '(':
            open_bracket += 1
        else:
            close_bracket += 1
        
        # 열린 괄호랑 닫힌 괄호랑 개수가 같아지는 순간 u문자열이랑 v문자열이 나뉨
        if open_bracket == close_bracket:
            # u, v순서로 반환
            return p[:i+1], p[i+1:]

        
def check_correct_string(u): # 문자열 u가 "올바른 괄호 문자열"인지 판단
    # stack이 비어 있다면 올바른 거임
    stack = []
    
    for c in u:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
            
    if stack:
        return False
    else:
        return True
    
def solution(p):
    answer = 0
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if not p:
        return p
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    u, v = sepatate_uv(p)
    # 3. 문자열 u가 올바른 문자열인지 판단
    if check_correct_string(u): # 참이면 문자열 v에 대해 1단계부터 다시 수행
        # 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        answer = u + solution(v)
        return answer
        
    else: # 거짓이라면
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        answer = '('
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        answer += solution(v)
        # 4-3. ')'를 다시 붙입니다. 
        answer += ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        for c in u[1:len(u)-1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('
        #4-5. 생성된 문자열을 반환합니다.
        return answer