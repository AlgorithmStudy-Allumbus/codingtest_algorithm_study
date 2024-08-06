import sys
input = sys.stdin.readline

N = int(input())  # 배열의 크기
k = int(input())  # 찾고자 하는 k번째 작은 값의 위치

start, end = 0, N * N  # 이분탐색 범위 설정 (0 ~ N*N)
# 이분탐색 시작
while start <= end:  # start와 end가 교차되기 전까지 계속 반복
    mid = (start + end) // 2
    count = 0
    # 각 행마다 mid보다 작거나 같은 값이 몇 개인지 세기
    for i in range(1, N + 1):
        # mid를 i로 나눈 값과 N 중 작은 값을 더함
        # 이는 i번째 행에서 mid보다 작거나 같은 값의 개수를 의미
        count += min(mid // i, N)

    if count < k:
        # mid보다 작거나 같은 값의 개수(count)가 k보다 작으면, k번째 값은 더 큰 값 중에 있음
        start = mid + 1
    else:
        # 그렇지 않으면, k번째 값은 더 작은 값 중에 있음
        end = mid - 1

# 최종적으로 start 값이 k번째로 작은 값이 됨
print(start)