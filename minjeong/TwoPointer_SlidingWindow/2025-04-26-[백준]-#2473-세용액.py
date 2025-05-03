import sys
input = sys.stdin.readline

N = int(input())  # 전체 용액의 수
liquid = sorted(map(int, input().split()))

left = 0
right = N-1
mid = (left + right) // 2
answer = abs(liquid[left] + liquid[mid] + liquid[right])
answer_liquid = [liquid[left], liquid[mid], liquid[right]]

for i in range(N-2):
    left = i + 1
    right = N - 1

    while left < right:
        temp = liquid[i] + liquid[left] + liquid[right]
        if abs(temp) < answer:
            answer = abs(temp)
            answer_liquid = [liquid[i], liquid[left], liquid[right]]
        if temp < 0:
            left += 1
        else:
            right -= 1

print(*answer_liquid)