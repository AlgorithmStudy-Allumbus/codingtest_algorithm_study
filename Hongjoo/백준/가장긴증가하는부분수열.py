"""
백준 #11053. 가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053

# Intutition : DP

가장 긴 증가하는 부분수열  
=> 부분수열 내 최대값보다 크면, 부분수열에 추가 & 기준 최대 값 업데이트

 # set 은 삽입시 순서를 보장하지 않음(순서 없는 자료형 , 즉 출력 및 삽입시 랜덤하게 섞임)
https://okky.kr/questions/571601
 """
import sys

N = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
# dp[i] : 0~ i번째 Subset 중 가장 긴 증가하는 부분 수열 갯수
# 
# Subset  중 가장 큰 수 찾기(비교군) 
# 비교군 VS 현재값 -> 크면 dp +1  , 작으면 dp

# 0. dp 초기값 :  Subset 총 개수 
dp = [ 1 for _ in range(N)]
for i in range(1, N) :
    for j in range(i):
        if input_list[i] > input_list[j] : 
            dp[i] = max(dp[i] , dp[j]+1)

    

print(max(dp))