# 2435 : 기상청 인턴 신현수
import sys
input = sys.stdin.readline

N, K = map(int, input().split())        # N: 온도 측정 전체 날짜. K: 합을 구하기 위한 연속적인 날짜 수
temps = list(map(int, input().split())) # 온도 정수 수열

prefix_sum = [0] * (N - K + 1) # 누적합 배열 초기화. 누적합 배열은 N

# 누적합 배열에 값 채워넣기
for i in range(len(prefix_sum)):
    # i~i+K-1까지의 범위를 모두 더한 값을 누적합 배열에 채워넣음
    prefix_sum[i] = sum(temps[i:i + K])

print(max(prefix_sum)) # 누적합 배열에서 가장 큰 값을 출력