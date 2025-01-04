"""
# goal:회의 시간이 겹치지 않는 회의의 최대 개수  -> 최적의 해 
-조건 
1. 입력 - 각 회의 I : (시작 시간 , 끝나는 시간)
2 회의는 중단 될 수 없ㅇ,ㅁ
3. 회의 시작 시간 = 끝나는 시간 
4. 0 <= 시작시간, 끝나는 시간 <= 2^31 -1 

# intution : 그리디
- prioirt 정렬 

"""
import sys
from collections import deque
# 0. 회의 리스트 입력 받기 [[시작 시간, 끝나는 시간]]
N = int(sys.stdin.readline())
cov_list =deque()

for n in range(N) :
    start , end = map(int, sys.stdin.readline().split())
    cov_list.append((start ,end))

# 2. 회의 prioirty 기준으로 정렬 -> prior : (1) end time 이 빠른 순 (2) start 가 빠른 순 으로 정렬 
cov_list = deque(sorted(cov_list , key = lambda x : x[0])) 
cov_list = deque(sorted(cov_list , key = lambda x : x[1]))

# # conv_lisg : [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
# 
# (1) 회의실 뽑기
# 2-1 현재 회의 종료 시간 보다 end 가 작으면 -> 제외
# 2-2 같거나 크면 -> 회의실 업데이트 (cnt+1)
cnt = 0
finished_time = 0 
for idx in range(N) :
    start , end = cov_list[idx]
    if finished_time <= start : 

        finished_time= end 
        cnt +=1 
print(cnt)


