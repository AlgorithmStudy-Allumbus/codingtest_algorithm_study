from itertools import permutations
def isPrime(n):
    if n <= 1 : 
        return False
    
    end = int(n**(1/2))
    for i in range(2,end+1):
        if n% i == 0 :
            return False
    return True
    
def solution(numbers):
    count = 0
    
    arrnum= set() # 중복 방지
    #1. 문자열 분리하기 -> 리스트[] 에 넣기
    li = list(numbers)
   # 분리된 숫자들을 "순열 조합"
    for i in range(1,len(numbers)+1) : 
        p_arr =permutations(li,i)
        for perm in p_arr :
            num = int("".join(perm))
            arrnum.add(num)
    print( arrnum)
    #prime 확인
    for n in arrnum: 
        if isPrime(n) : 
            count+= 1
    return count
        