def solution(s):
    answer = True
    print(s)
    #1. s은 ( 로 시작, ) 가 끝
    if s[0] == ")":
        answer = False
        return answer
    elif s[-1] == "(":
        answer = False
        return answer
    #2.) 와 (의 개수 동일
    left = 0
    right = 0
    for n in s : 
        if n == "(":
            left +=1 
        elif n == ")":
            right +=1
        else:
            answer = False
            return answer 
    
    if left != right : 
        answer = False
        return answer
            

    return True