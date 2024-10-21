#정올 : https://jungol.co.kr/problem/1318

import  sys 

n= int(sys.stdin.readline())
while n != 0 :
    # dp 세팅하기 
    # ugly = [ 0 for _ in range(n)]
    ugly= list()
    ugly.append(1)
    # 기존 array 
    nums = [2,3,5]

    for i in range(n) :
        tmp = [ ugly[i] * j for j in nums] 
        ugly += tmp #이전 ugly에 추가
        ugly= set(ugly) # 중복 제거
        ugly = list(ugly)
        ugly.sort() # 정렬

    print(ugly[n-1])
    n= int(sys.stdin.readline())
    