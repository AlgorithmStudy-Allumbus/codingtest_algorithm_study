"""
- 명예 전당 : k=3 인 queue : <-| |<-
# 탐색
1. 현재 score  = score[i] 
2. 명예 전당 업데이트 

if  len(deque) >=  k (꽉참) 
    => popleft() &insert
3.발표 점수 = min(deque) 
"""
from collections import deque
def solution(k, score):
    answer = []
    top_k = []
    for i in range(len(score)) : 
        if len(top_k) >= k : # 꽉참
            #업데이트 가능 여부 확인
            if score[i] > top_k[0]  : 
                del top_k[0] #pop 
                top_k.append(score[i])
                # print(f"apdate {score[i]}=> { top_k}")
            
        else : # 여유 남음
            top_k.append(score[i])
        
        top_k = sorted(top_k) #오름차순
        answer.append(top_k[0])
        # print(f"{i} - {score[i]}: {top_k}=> {answer}")
    return answer