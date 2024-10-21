
'''
Y축 (before) -> X 축 after)

    A[i]=B[j] 같으면 : 유지 ->대각선:  dp[i,j] = dp[i-1,j-1]
    A[i]!=B[j]의 경우 : 교체 -> 대각선 +1 

    if len(Y) > len(X) : # 빼기 => top down +1  
    if len(Y) < len(X) : # 추가 => +1 left-right(->)
    dp[i][j]= min(왼,위,대각선) +1     
        
'''
import sys
before =[0]+ list(sys.stdin.readline())[:-1]
after = [0] + list(sys.stdin.readline())[:-1]
dp = [[0 for _ in range(len(after))] for k in range(len(before))]

# 2. 최소 편집 거리

for i in range(len(before)):
    for j in range(len(after)) :
        # 2-1최소 편집 거리 map 초기화
        if i== 0 and j>0:
            dp[i][j] = dp[i][j-1]+1 # i=0
        elif j == 0 and i > 0 :
            dp[i][j] = dp[i-1][j]+1    
        # 2-2 최소 편집 거리 점화식
        else : 
            b = before[i]
            a = after[j]

            if a == b :#유지
                dp[i][j] = dp[i-1][j-1]
            else : # 추가 , 빼기 , 교체 중 가장 편집 거리가 적은 경우+1 
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) +1 # 
                # print(f"-{b},{a} : {dp[i][j]} ")


        print(f"{b} -> {a} : dp[{i}{j}] : {dp[i][j]}")
    print("")
# print(dp)

# print("-------------")
print(dp[-1][-1])