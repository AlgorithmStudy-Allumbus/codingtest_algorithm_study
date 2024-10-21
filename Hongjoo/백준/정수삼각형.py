"""
-top-dowm 방향으로 내려올때 , 각 경로에서 요소들의 최대합을 리스트 dp 에 누적시키기
1, 2중 for 문 
2. 모든 경로에 대해 숫자의 누적합을 dp 리스트에 넣기
 - 맨 left , right  : idx = 0 , -1 경우 
    =>  dp[stage][0] =dp[stage-1][0] +  graph[stage][0] 
    => dp[stage][-1] =dp[stage-1][-1] +  graph[stage][-1]
- 가운데 [idx : 1~ state-1]
    => dp[stage][idx] = max(dp[stage-1][idx] + graph[stage][idx-1] , dp[stage-1][idx] + graph[stage][idx] ) 
    
[7]
[10,15]
8 1 0
[18]  , [11vs 16 = 16] , [15+0]
2 7 4 4
[18 +2] [18 + 7 vs 16 + 7] [] [15+ 4]

"""
import sys
#1. input
n = int(sys.stdin.readline())
graph= []
for i in range(n) : 
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)
# 2. Initialize List dp

dp = [graph[0]]

#3. dynamic programing 

for stage in range(1,n) :
    tmp = []
    num_list = graph[stage] # add 
    
    for idx in range(len(num_list)) : 
        total_sum = 0 
        if idx == 0  :  # left
            total_sum = dp[stage-1][0] + num_list[0]
        elif idx < len(num_list)-1: # middle                
            total_sum = max(dp[stage-1][idx-1] + num_list[idx], dp[stage-1][idx] + num_list[idx])
        else: # idx == -1: #right
            total_sum = dp[stage-1][-1] + num_list[-1]
        tmp.append(total_sum)
        
    dp.append(tmp)
 

answer = max(dp[-1])
print(f"{answer}")