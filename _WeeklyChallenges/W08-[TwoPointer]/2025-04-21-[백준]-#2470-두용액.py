import sys
input = sys.stdin.readline

N = int(input())  # 전체 용액의 수
liquid = sorted(map(int, input().split()))

left = 0
right = N - 1

# 초기값 설정
answer = abs(liquid[left] + liquid[right])
answer_liquid = [liquid[left], liquid[right]]

while left < right:
    temp = liquid[left] + liquid[right]
    # 합이 0에 더 가까우면 정답 갱신
    if abs(temp) < answer:
        answer = abs(temp)
        answer_liquid = [liquid[left], liquid[right]]
    # 포인터 이동
    if temp < 0:
        left += 1
    else:
        right -= 1

print(answer_liquid[0], answer_liquid[1])