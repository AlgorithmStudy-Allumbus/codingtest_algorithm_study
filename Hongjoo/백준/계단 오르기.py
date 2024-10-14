'''
1. 계단은 step +1 or step+2
2. 연속된 세계 계단을 모두 밟으면 안됨 (1,2,3,x), 시작점은 계단 ㄴㄴ
3.마지막 도착계단은 반드시 밟기

# flag 
이전 +1 :(new = 현 step +1 ) -> 안됨
이전 +2or 1 : (new=현 step+2) -> 가능 

dp[] : max 값만 넣기
iteration 2 
dp[i] : Max(dp[i-1] + step[i] 

'''
# input 
import sys
n = int(input())
field = list()
for _ in range(n):
    field.append(int(sys.stdin.readline()))
# print(f"field { field} , {len(field)}")
# step : n개 -> 0시작점+ 0~ n-1 
flag = 0 # dp[i-1]에서 온 경우 선택: 1 ,dp[i-2] 에서 온 경우 : 0 
dp = [0 for _ in range(n)]
# print(f"dp {dp} , {len(dp)}")

if n == 1 : 
    print(field[0])
elif n== 2 : 
    print(max(dp[0], 0)+ field[1])
else : #n >= 3

    dp[0] =field[0]# i=0 인 경우 -> dp[0] = 첫 번쨰 & ,flag = 0 (시작은 계단으로 안침)
    if dp[0] > 0 : # 이전 i-1= 0 을 참조한 경우
        flag= 1
    dp[1] = max(dp[0], 0)+ field[1]


    for i in range(2 , n) : 
        if flag == 0 : # 이전 dp[i-2] 참조한 경우
            #dp[i] = max(dp[i-1] + field[i] ,dp[i-2] + field[i]  )
            if dp[i-1] > dp[i-2]  : # +1 선택
                flag = 1
            #+2 선택 -> flag = 0 
            dp[i] = max(dp[i-1], dp[i-2]) + field[i] 
        elif flag == 1 : # 이전 dp[i-1] 참조한 경우
            # 무조건 +2 만 가능  -> flag = 0
            flag = 0
            dp[i] = dp[i-2] + field[i]

    #dp[-1] : 시작~ 도착 지점까지 얻을 수 있는 점수 최대값
    print(dp[-1])