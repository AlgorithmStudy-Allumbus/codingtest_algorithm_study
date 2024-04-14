def solution(begin, end):
    #1. make map
    # list, range()로 dict 만들기
    # 지정된 value = 0 으로 원하는 size의 dict 만들기
    values = []
    for k in range(begin,end+1):
        values.append(0)
    dic=dict(zip(range(begin,end+1),values))
    print(dic, type(dic))
    #n in 2n, 3n 4n
    n=1 
    while 2*n <= end :
        m=2
        while n*m <= end:
            dic[n*m]= n 
            m+= 1

        n+= 1
    answer=list(dic.values())
    print(answer)
    return answer