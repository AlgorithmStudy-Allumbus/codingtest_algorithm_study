'''
[백준#1806.부분합]
https://www.acmicpc.net/problem/1806

참조:
https://aia1235.tistory.com/46
'''

import sys
N ,S = map(int, sys.stdin.readline().split())
arr = list(map(int, input().split()))

start , end = 0, 0 
min_length = 100000
partial_sum = arr[0]
while start <= end :
    if partial_sum >= S :  # S보다 큰 부분합인 경우
        min_length = min(min_length , end - start +1 ) # 최소 길이 업데이트 확인
        partial_sum -= arr[start]  # start +1 이동
        start += 1 
    else : #partial_sum < S :
        end += 1 
        if end < N : 
            partial_sum += arr[end]
        else :  #반복문 끝
            break  


if min_length == 100000 : # 수열 끝 -> 조건 충족 x
    print(0)
else : 
    print(min_length)