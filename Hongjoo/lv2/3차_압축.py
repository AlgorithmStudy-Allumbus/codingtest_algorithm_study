"""
## 프로그래머스#17684. [3차]_압축: 구현 / lv2
> 문제 링크  :  https://school.programmers.co.kr/learn/courses/30/lessons/17684
"""
def solution(msg):
    answer = []
    # 1. 사전 초기기 
    dict = {}
    idx = 1 # 초기 사전 idx 
    for o in range(65, 65+ 26) :
        dict[chr(o)] = idx 
        idx += 1
    last_idx = idx-1
    #2. 입출력 단어 압축하기
    prev_idx = -1
    w_s = 0 ; w_l = 1
    while w_s+w_l <= len(msg) :  
        word = msg[w_s : w_s + w_l]
        idx = dict.get(word , -1 )
        if idx > -1 :  
            prev_idx = idx
            w_l += 1
            continue
        #사전에 없음
        else : 
          last_idx += 1
          dict[word] = last_idx # 사전 등록하기
          w_s = w_s + w_l - 1 #탐색 point 업데이트 
          w_l  = 1 # 단어 길이 초기화
          answer+= [prev_idx]# 이전 존재한 단어의 idx 는 출력 리스트에 추가
    answer+= [prev_idx] # 마지막 w 의 인덱스 출력

    
    return answer