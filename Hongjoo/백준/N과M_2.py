"""
#15650. N과M(2)
https://www.acmicpc.net/problem/15650

- 조합 : 1~ N 중 m개로 구성된 수열  출력하기
- 사전순으로 증가하는 하는 순서로 출력
- backtracking 
"""
import sys
n , m = map(int, sys.stdin.readline().split())
# 1. 수열 후보군 나열하기
board = list(range(n+1)) # [1,2,...n]
#2. m 개의 수열 조합 출력하기
stack = list()
result = list()
def backtracking(start , end  ,m) : 
    if len(stack) == m : # 재귀 종료 조건
        print(" ".join(map(str, stack)))
        return 
     
    for i in range(start, end+1) : # 모든 자식 노드 나열 
        if i not in stack : # 선택지 유효 여부 확인 - 중복 확인  
            stack.append(i) # 자식 노드 추가
            backtracking(i+1 , end , m) # 백 트래킹
            stack.pop() # 부모 노드로 회귀
backtracking(1,n, m)