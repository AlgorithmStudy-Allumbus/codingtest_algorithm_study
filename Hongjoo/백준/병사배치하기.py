'''
조건 
1. 전투력 -> 내림차순 부분수열
2. 남은 병사들의 수가 최대  = 열외 병사수 최소 
# LIS  , Dynamic 
goal : 남은 병사들의 수가 최대 , 열외하는 병사 수 출력  
'''
import sys

nums =int(sys.stdin.readline()) # 수열 길이 
soldiers =list( map(int,sys.stdin.readline().split())) # 주어진 수열 

# DP 테이블 = 1 로 초기화
dp= [ 1 for _ in range(nums)] 

# 순서를 뒤집어서 'LIS - 최장 증가 부분 수열' 문제로 변환
soldiers.reverse() # goal : 내림차순 -> 오름차순

# 가장 긴 오른차순 부분 수열 (LIS) 알고리즘 수행 

for i in range(1, len(soldiers)) :
    for j in range(0,i) :
        if soldiers[j] < soldiers[i] : # 오름차순 만족 
            dp[i] = max(dp[j]+1 , dp[i]) # i번 병사가 열외 x , 열외 o

# 열외하는 병사 최소 수
print(nums - max(dp))