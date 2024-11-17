def one_to_n(n):
    return n*(n+1) /2
def solution(a, b):
    '''
    1~ 5 합 = 1+2+3+4+5 = 15 : n(n+1) /2  = 5*6/2 = 15
    '''
     # big , small
    if a > b : 
        n=a ; m=b
    elif a < b : 
        n=b ; m =a
    else :  # a==b
        return a
    answer = one_to_n(n) - one_to_n(m-1)
    
    return answer