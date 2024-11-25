import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())  # 수열의 크기
numbers = list(map(int, input().split()))  # 수열
x = int(input())  # 목표 숫자

# 초기화
left = 0
right = n - 1
count = 0

# 수열 정렬
numbers.sort()

# 투 포인터 탐색
while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum > x:
        right -= 1  # 합이 크면 오른쪽 포인터를 왼쪽으로
    elif current_sum < x:
        left += 1  # 합이 작으면 왼쪽 포인터를 오른쪽으로
    else:
        count += 1  # 조건 만족
        left += 1
        right -= 1

# 결과 출력
print(count)