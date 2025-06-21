"""
https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""

def solution(cacheSize, cities):
    answer = 0
    #1. 모든 도시이름 소문자 -> 대문자로 통일
    for c in range(len(cities)): 
        cities[c]=cities[c].upper()
    stack = []
    # +예외처리 : chachSize가 0일때 -> answer = 5*dB개수 
    if cacheSize <= 0 : 
        return (5*len(cities))
    # 2. City 개수만큼 반복
    for i in range(len(cities)):
        city = cities[i]
        cache_miss = True
        # 2-1 . Stack에 있을때(cache hit)
        for s in range(len(stack)):
            if city == stack[s][1] : # stack에 있음
                answer += 1 # cache hit 시간 추가
                cache_miss = False 
                stack[s][0] =  answer # 데이터 사용 시간 업데이트 
                
        #2-2. 위 cache 탐색 후에도 Cache miss 발생
        if cache_miss : # Cache miss 남  
            # [1] cache miss 발생& stack이 not full
            answer += 5 
            if len(stack) < cacheSize:
                stack.append([answer,city])
            #[2] cache miss 발생 & stack 이 full 한 경우 -> replace 교체 (recently cache)
            else :
                # stack내에 검색 시간이 가장 이른 db 버리기 
                stack.sort(key = lambda x : x[0])
                stack.pop(0)
                # 새로운 data로 교체
                stack.append([answer,city])

    return answer