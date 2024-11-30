'''
[문제] : https://school.programmers.co.kr/learn/courses/30/lessons/12924#
[Flow]
연속된 자연수의 조합-> two point 
0. 초기화
 start == end-1 = 0
while end <=  len(words)  and start < end 
1. sum(words[start,end]) < target
    -> end += 1
2.  sum(words[start,end]) == target
    -> count += 1 
    -> start += 1 
    -> end = start +1  

3.  sum(words[start,end]) > 0 
    -> 2와 동일 
    
'''
def solution(n):
    answer = 1 # 본인= target
    start = 0 ; end  = start +1 ;
    answer_li = []
    half= round(n//2) +2 
    field = range(1,half) # 반올림 
    field = list(field)

    while n > 2 and end <=  len(field)  and start < end  and start < len(field): #
        current =sum(field[start : end])
        if current < n : 
            end += 1
        else : # currnet >= n
            if current == n : 
                answer += 1
                answer_li.append([start, end])
            start += 1
            end = start +1 
    return answer