from collections import deque

def solution(cacheSize, cities):
    totalTime = 0
    cache = deque([])
    '''
    전체적인 과정은 FIFO로 수행된다.
    만약 이미 존재하는 도시라면 맨 뒤로 다시 보낸다. 
    '''

    for i in range(len(cities)):
        city = cities[i].lower()     # 대소문자 구분 없으므로 cities를 lowercase로 바꾸기
        if cacheSize == 0:  # cacheSize가 0인 경우에 대한 예외처리(TC 7, 17)
            totalTime += 5
            continue    # 그 후 바로 빠져나옴
        if city in cache:        # 캐시에 도시가 이미 존재하는 경우
            cache.remove(city)
            cache.append(city)
            totalTime += 1 # cache hit
        else:
            if len(cache) == cacheSize and cacheSize > 0: # 캐시가 가득찼다면, 맨 앞에 하나 버린다. 이때 cacheSize가 0인 경우도 있다. 이때는 popleft하면 에러가 나므로 cacheSize가 0이상인 경우만 처리되도록 한다.                    
                cache.popleft()
            cache.append(city)
            totalTime += 5 # cache miss
            
             
    return totalTime
