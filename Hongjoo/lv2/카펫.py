def solution(brown, yellow):
    sum = brown + yellow
    # 1. w,h in [sum의 약수 후보군]
    m=2 
    li = []
    while m <= sum :
        if sum % m  == 0 :
            li.append(m)
        m += 1
    print(li)
    # 2. 조건
    #2-1 w 가로 >= h 세로
    #2-2 갈색 = 2(w-1) + 2(h-1)
    #2-3 노란색 = (w-2) * (h-2)
    for w in li : 
        for h in li:
            if w>=h and  brown == (2*w+2*h-4) and yellow == ((w-2)*(h-2)) :
                answer = [w,h]
                return answer