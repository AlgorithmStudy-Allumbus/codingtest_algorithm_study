"""
https://www.acmicpc.net/problem/2470

# 음 - 염 / 양 - 산성  
goal) 2개 혼합 -> 0에 가장 가까운 두 용액 찾기
# 출력
 - 2개 오름차순 출력
 - 경우가 2개 이상이면 둘중에 1개 아무거나
# flow 
1. 오름차순 정렬 
2. 2개가 +- 조합인 경우 => 양끝에 투 포인터..?
    => [-99,-2,-1,4,98]
        start         end 
        #2-1. 둘 간 합이 기존 min보다 작으면 -> 업데이트 
        # start와 end의 절대값 크기 차이를 기준으로 포인터가 이동함
        if abs(arr[start]) > abs(arr[end]) => start += 1 이동 , end 유지
        elif # end -= 1 이동 
        else : #같으면 
            break #끝
        
        
        # until : start = end 가 같은 idx를 가르키면 (start >= end)
        


2. 2개가 ++ 조합 => + 중 최소값 2개의 합
3. 2개가 -- 조합 =>  -중 최대값 2개의 합 
=> 3개 비교 후 가장 0에 가까운 값 찾기
 """

import sys
N = int(sys.stdin.readline())
liqs = sorted(list(map(int, sys.stdin.readline().split())))

# print(liqs)
# 1. +- 의 조합
start = 0 ; end = len(liqs)-1
closed_z = [start,end,abs(liqs[start] + liqs[end])]
while start < end :
    c = liqs[start] + liqs[end]
    if closed_z[-1] > abs(c) : 
        closed_z = [start,end, abs(c)]
        if c == 0 : 
            break
        # print(f"##")
    # print(f"# {c} : {closed_z}   =  {liqs[start]} / {liqs[end]}")

    if abs(liqs[start]) > abs(liqs[end]) : 
        start+= 1
    # elif abs(liqs[start]) < abs(liqs[end]) : 
    else :
        end -=1


print(liqs[closed_z[0]] , liqs[closed_z[1]])


