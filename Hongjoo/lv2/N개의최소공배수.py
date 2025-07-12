"""
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12953

n개의 숫자들의 최소 공배수 
Inspect :n 개의 숫자들이 모두 "1" 이 될 때 까지  2~100의 자연수들의 값으로 나누기
ex) 
[2,6,8,14]
e = 2  :  [1,3,4,7] => elements = [2]
e = 3  :  [1.1.4.7] => elements = [2,3]
e = 4 :   [1,1,1,7]  => elements = [2,3,4]
e = 5 :   [1,1,1,7] => 유지
e = 6 ...

"""
def solution(arr) :
    answer = 1
    elements = []
    
    e = 2 
    # 1. 
    while e<=100 or arr.count(1) != len(arr) : 
        
        flag = False 
        #2. 해당 e 로 배열 arr 가 나누어 떨어지는 지 확인 -> 떨어지면 flag = True , 해당 arr[k] 은 e의 몫으로 구성함
        for k in range(len(arr)) :
            if arr[k] == 1 : 
                continue 
            if arr[k] % e == 0 : 
                arr[k] =arr[k] // e 
                flag = True 
        #3. 해당 e 값이 배열 arr 의 값 중 하나 이상의 구성 요소일때 , 최소공배수 구성워소 elements 배열에 추가 
        if flag : 
            elements.append(e)
        else : # 해당 값이 구성 원소 아닐 경우 -> 다음 e 로 다시 도전하기
            e+= 1
                
    
    for e in elements :
        answer*= e 
    return answer
