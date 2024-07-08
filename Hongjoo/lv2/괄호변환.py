answer = ''
def u_notcorrect(u,v):
    #4-4 자르고 -> 뒤집기
    u = list(u[1:-1]) # 4-4
    if bool(u) :
        for i in range(len(u)):
            if u[i]==")":
                u[i] = "("
            else :
                u[i] = ")"
        
    u = "".join(u)
    # 4-1, 4-2,4-3
    tmp= '(' + cut_wuv(v) +')' + str(u) 
    return tmp


def isCorrectString(u) :  # u = p[s:e+1]
    count = 0
    for s in u : 
        if s == "(" :
            count+=1
        elif s == ")" :
            count-=1
        if count < 0 : 
            return False 
    return count == 0
     
def cut_wuv(w): 
    global answer
    # 1. 빈 문자열 -> 빈 문자열
    if w == "": 
        return ""
    #2 w = u+v로 나누기
    e =0 #end idx 가리키는 two point
    while e < len(w): 
        e +=1
         # u 구하기 #2
        if w[:e+1].count('(') == w[:e+1].count(')'):
            w=w[:] ;u = w[:e+1] ; v = w[e+1:]
            break
    
    # 3. 
    if not isCorrectString(u): #4올바른 괄호 문자열 x(onlt 균형 잡힌 문자열)
        answer+=str(u_notcorrect(u,v))
        return answer
                
    else : #3 u 가 올바른 괄호 문자열
        answer =  str(u) +cut_wuv(v)
        return answer 

    
def solution(p):
    global answer 
    answer=cut_wuv(p)
    return answer