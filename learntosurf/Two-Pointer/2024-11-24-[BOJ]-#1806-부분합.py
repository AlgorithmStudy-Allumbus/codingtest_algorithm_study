import sys 
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

def min_subarray_length(N, S, arr):
    # 초기화
    start, end = 0, 0
    current_sum = 0
    min_length = float('inf')  # 최소 길이를 아주 큰 값으로 초기화

    # 슬라이딩 윈도우 실행
    while end < N:
        # 현재 값을 current_sum에 추가
        current_sum += arr[end]
        
        # current_sum이 S 이상이면 조건 만족
        while current_sum >= S:
            # 구간 길이 계산 후 최소 길이 갱신
            min_length = min(min_length, end - start + 1)
            # start를 오른쪽으로 이동하며 구간을 줄임
            current_sum -= arr[start]
            start += 1
        
        # end를 오른쪽으로 이동
        end += 1

    # 조건을 만족하는 구간이 없으면 0 반환, 아니면 최소 길이 반환
    return 0 if min_length == float('inf') else min_length
    
result = min_subarray_length(N, S, arr)
print(result)