import sys

N = int(sys.stdin.readline())
arr = sorted(map(int, sys.stdin.readline().split()))

left = 0
right = N - 1

answer = (arr[left], arr[right], abs(arr[left] + arr[right]))

# 투 포인터 사용해서 절대값이 0에 가장 가까운 두 값 찾기
while left < right:
    total = arr[left] + arr[right]
    abs_total = abs(total)

    if abs_total < answer[2]:
        answer = (arr[left], arr[right], abs_total)
        if abs_total == 0:
            break
    # 두 용액의 값이 0보다 크면 right를 줄여서 합을 작게 만든다
    if total > 0:
        right -= 1
    else:
        # 두 용액의 값이 0보다 작으면 left를 늘려서 합을 크게 만든다
        left += 1

print(f"{answer[0]} {answer[1]}")