"""
# slide window , 투 포인터
-연속된 날짜의 온도 합 중 최대값 출력 = goal
- sum(temp[s:e]) 같은 한번씩 슬라이딩으로 합을 구하면 시간 초과 발생
- window 범위 내 start 와 end 포인트 값을 빼고, 더하는 식으로 전체 합 구하기
# flow
1. temp 리스트 입력 받기
-window size =k , N  : 날짜
2. window 범위에 해당하는 리스트 합 중 최대값 구하기
next_window = 이전 window - 앞 + 뒤
=> sliding winodw을 통해 window 내 맨앞과 맨 뒤 값만 구해서 더하고 빼면 범위내 총합 구할 수 있다.

"""
import sys
input = sys.stdin.readline
#0. 전체 일수 = N , 연속 일수= K ,
N , k = map(int,input().split())
temp = list(map(int, input().split()))

# 1. 첫 window 범위 초기화 
sum_tmp = sum(temp[0:k]) # 초기 window 내 리스트의 합
max_sum = sum_tmp # 최대값을 window 합 초기값으로 설정
# 2. 투 포인터 (s,e)을 이동하여 window 범위 합 구하기 
# e :새로운 window 범위에 들어가는 값
# s :새로운 window 범위에서 빠지는 값 
for e in range(k, N):
  s = e-k # 0 n-k
  sum_tmp = sum_tmp - temp[s] + temp[e] # 새로운 window 범위 내의 합
  max_sum = max(max_sum , sum_tmp) # 

print(max_sum)
