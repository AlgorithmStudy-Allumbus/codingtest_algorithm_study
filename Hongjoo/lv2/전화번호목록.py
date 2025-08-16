"""
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""

def solution(phone_book):
    answer = True
    #1. 글자수로 정렬하기
    phone_book = sorted(phone_book , key = lambda x : (len(x)))
    #2. key = 전번인 해쉬맵 생성
    hash_map = {}
    for phone in phone_book : 
        hash_map[phone] = 1
    #3. hashmap에 접두어 비교하기
    for phone in phone_book : 
        tmp = ""
        # 접두어 한 글자씩 추가해서 hasp_map의 key들 중에 같은게 있는지 확인
        for n in phone : 
            tmp += n
            if tmp in hash_map and tmp!= phone : 
                answer = False

                
                
            
        
    return answer