"""
실패
1. 가장 큰 자리수 비교 -> 자리수 가장 작은 수
0. graph
idx : numbers
value : [0,0,0,-1] # ex 62 => [6,2,False,False]
# 조건 2.
3,30,300 비교 -> 3 > 30> 300 우선순위
#반례
1) 110 vs 1 > 1+110
2) [12, 1213] -> 1213+12
"""

def solution(numbers):
    answer = ''
    #0. graph 만들기
    graph = list()
    for n in numbers:
        p =  4-len(str(n))
        if p >  0 : 
            douple_n = str(n)*p
        else :
            douple_n = str(n)
        graph.append([douple_n[:4], p ]) # 자리수 맞춰주기(4자리)
    # print(graph)
    #2.정렬 : 높은 자리수의 값이 큰 순서 대로
    graph.sort(key=lambda x : x[0] , reverse = True)
    # print(graph)
    #3. 합치기
    answer=""
    for i in range(len(graph)):
        num = graph[i][0] ; position = 4-graph[i][1]
        answer += str(int(num[:position]))# "000","0" 경우 0으로 처리
    
    return answer