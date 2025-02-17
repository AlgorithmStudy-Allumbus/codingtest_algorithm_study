"""
#19638. 센팀와 마법의 뿅망치
https://www.acmicpc.net/problem/19638
# 문제 조건 
1. 입력 : 인구수 N , 대조군 키 H , 횟수 제한 T  / 거인 키 n1, n2 ...
2. L -> L/2 // 
3. T 개 안에 H > N개키
# flow
goal) 키가 큰 거인 선택 -> 때리기 
- 최소 길이 1 => H = 1, -> 무조건 No
# 문제 핵심
- sort 사용시 런타임 에러
- 따라서 heapq가 핵심
"""

import sys
import heapq
N , H, threshold= list(map(int, sys.stdin.readline().split()))

heights = []
for i in range(N) :
    h = int(sys.stdin.readline())
    heapq.heappush(heights ,-1* h)
    # heights.append(h)



cnt = 0 
for trial in range(threshold+1) :
    current_top = -1*heapq.heappop(heights)
    if  current_top == 1 or H > current_top : # 중간 종료 조건 : (1) 
        break    

    if trial >= threshold : 

        break

    heapq.heappush(heights , -1*(current_top// 2)) 
     
    #1. 가장 큰 거인 VS  센티의 키 차이 비교

if  H > current_top :
    print("YES")
    print(trial)
else :
    print("NO")
    print(current_top)
