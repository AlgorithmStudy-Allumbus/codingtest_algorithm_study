import sys
input = sys.stdin.readline
# N: 온도를 측정한 전체 날짜 수 / K: 연속적인 날짜의 수
N, K = map(int, input().strip().split()) 
temp = list(map(int, input().strip().split())) # 온도 리스트
prefix_sum = [0] * (N+1)  # 누적합 리스트
section = N - K + 1       # 구간합 리스트를 초기화하기 위한 크기
range_sum = [0] * section # 구간합 리스트

# 누적합 구하기
for i in range(len(temp)):
    prefix_sum[i+1] = temp[i] + prefix_sum[i]

# 구간합 구하기
for i in range(K, section+K):
    range_sum[i-K] = prefix_sum[i] - prefix_sum[i-K] 

print(max(range_sum)) # K일의 온도의 합이 최대가 되는 값