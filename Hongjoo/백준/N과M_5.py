"""
#15654. N과 M (5)
https://www.acmicpc.net/problem/15654

- N개의 원소들로 구성된 수열 중, 개수가 m개인 수열들 찾기
- 사전순 = 오름차순으로 출력  
- 중복되는 수열 => 재귀
# TIL
q = [1,2,3]
print(*q) > 1,2,3 # 한줄로 리스트 원소들 출력 가능
"""
import sys

#0. 입력 받기 
N , M = map(int, sys.stdin.readline().split())
# M개의 수열 결과를 저장할 배열
result = [0 for _ in range(M)]
# 해당 원소 사용 여부 check 함수
check = [0 for _ in range(N)]
# n 개 수열 원소 후보군 저장하는 리스트
elements = list(map(int, sys.stdin.readline().split()))
#오름 차순 정렬 for 오름차순 결과 출력
elements.sort()
# print(elements)

# 1. m 개 수열 찾기 by 재귀 함수
"""
def fun(n) :
    if  재귀종료 조건 
    else : 
    재귀로 다음 스테이지로 넘어가기 전에 실행하는 코드들
    fun(n+-1) # 재귀
    이전 재귀 함수의 재귀종료 조건 종료 후 실행

"""
 
# start point 
def perm(m) : # m : result 안에 들어가있는 원소 개수 = 넣을 위치
    if m == M : # result  개수 같으면 = 재귀 종료 조건
        print(*result) # 출력

    else : 
        for i in range(N) : # 더 뽑아야 하면 , N 개 후보군 중에 확인
            if check[i] == 0 : #현재 후보원소(i) 사용 가능함
                result[m] = elements[i] # result에 등록
                check[i] = 1 # 사용중
                perm(m+1) # result 에 m+1 개 들어가 있음
                check[i] = 0  # 사용 완료

perm(0 )

"""
# (추가)요건 출력된 순열 중에 중복 없이 출력되는 경우

# start point 
def perm(m , start_point) : # m : result 안에 들어가있는 원소 개수 = 넣을 위치
    if m == M : # result  개수 같으면 = 재귀 종료 조건
        print(*result) # 출력
        # print(check)
        for s in range(start_point+1,N):
            check[s] = 0  # 사용 완료
        # print(f"현재 ; {check}")
    else : 
        for i in range(N) : # 더 뽑아야 하면 , N 개 후보군 중에 확인
            if check[i] == 0 : #현재 후보원소(i) 사용 가능함
                result[m] = elements[i] # result에 등록
                check[i] = 1 # 사용중
                # print(f"업데이트 중 {check}")
                perm(m+1, start_point) # result 에 m+1 개 들어가 있음
                start_point += 1 # 다음 칸으로 이동 

perm(0 , 0)
"""