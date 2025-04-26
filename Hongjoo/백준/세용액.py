"""
https://www.acmicpc.net/problem/2473
# 두용액 -> 3용액
# 포인트 
#flow
x<= y<= z 일떄 
(1) (x,y) 의 모든 조합
(2)z 는 y+1 ~ N 번째 중 x+y+z -> 0 인 숫자 구하기  
#ME 
(1) Start idx = 0  , end _iex =-1 
(2) middle : for문으로 start+1 : end 내 값 중 -(start+end)과 가장 가까운 값 ?
(3) start + end + miidle 합과 기존 최소값 비교하기 

4
1 2 3 4

4
-1 -2 -3 -4

4
-2 -1 1 2

# 0 가능
6
-10 0 2 3 4 8
=> -10 2 8

"""
 

import sys

INF = 1e12
N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
#1. 오름차순 정렬 과 포인트 초기화

total_min = INF
answer = []
# print(f"arr {arr}")
# 2. 투 포인터 
# x < y<z 일때 - X 는 fix , y,z는 투 포인터
for i in range(N-2):
    x = arr[i]
    yp = i+1
    zp =N-1
    while yp < zp : 
        xyz_sum =x + arr[yp] + arr[zp]
        #결과값 업데이트
        if abs(xyz_sum) < total_min :  # 업데이트
            answer = [x,arr[yp],arr[zp]]
            total_min = abs(xyz_sum) 
        # 포인터 이동 
        if xyz_sum <0 : 
            yp+=1
        elif xyz_sum >0 :
            zp-=1
        else : # xyz_sum == 0 
            print(" ".join(map(str,answer)))
            sys.exit()



str_answer = " ".join(map(str,answer))
print(str_answer)