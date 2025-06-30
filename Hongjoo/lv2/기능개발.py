"""
## 프로그래머스#42586. 기능개발 : 구현, 큐/lv2
> 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

"""
import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    # 1. progress별로 추가 Day 구하기
    days= deque([0 for _ in range(len(progresses))])
    for i in range(len(progresses)) :
        days[i] = math.ceil((100 - progresses[i]) / speeds[i])
    # print(days)
    #2. 같은 배포일을 가진 서비스 개수들 구하기
    while days :
        tmp = 0
        develop_day = days[0] 
        # deque로 develop_days보다 더 빠르게 종료되는 서비스들은 pop 
        while days and develop_day >= days[0] : 
            tmp += 1 
            days.popleft()
        # 해당 develop_day보다 큰 경우,  그 전까지 서비스들이 같은 배포일 가짐 
        answer.append(tmp)
            
                
    return answer