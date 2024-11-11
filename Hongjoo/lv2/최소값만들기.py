def solution(A,B):
    # 누적 최소값 방법 :  최소 * 최대 
    '''
    5+ 8+16 = 29
    4+ 6 = 10 
    '''
    a= sorted(A)
    b = sorted(B)
    print(b)
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[-1+ -1*i]


    return answer