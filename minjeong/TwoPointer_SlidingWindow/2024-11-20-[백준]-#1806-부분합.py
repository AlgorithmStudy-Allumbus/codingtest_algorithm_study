import sys

input = sys.stdin.readline

# 입력 받기
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

# 초기 변수 설정
interval_sum = 0
end = 0
count = N + 1  # 최소 길이 초기값 설정 (최대값)

# 슬라이딩 윈도우 알고리즘
for start in range(N):
    # end를 확장하며 구간 합 계산
    while interval_sum < S and end < N:
        interval_sum += numbers[end]
        end += 1

    # 부분합이 S 이상이면 최소 길이 갱신
    if interval_sum >= S:
        count = min(count, end - start)

    # 구간 시작점을 이동하며 부분합 감소
    interval_sum -= numbers[start]

# 결과 출력 (조건 만족 구간이 없으면 0)
print(0 if count == N + 1 else count)
