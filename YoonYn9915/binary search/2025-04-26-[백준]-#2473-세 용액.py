import sys

inp = sys.stdin.readline

N = int(inp())
arr = list(map(int, inp().split()))
arr.sort()

min_value = int(1e10)
answer = [-1, -1, -1]

# 각 용액을 순회하며
for i in range(N):
    left = i + 1
    right = N - 1

    # i번 용액을 넣었을 때 값이 가장 0에 가까운 두 값 찾기
    while left < right:
        if left == i:
            left = i + 1
            continue
        elif right == i:
            right = i - 1
            continue

        total = arr[i] + arr[left] + arr[right]

        # 세 용액의 합이 0에 가장 가까우면 업데이트
        if abs(total) < min_value:
            min_value = abs(total)
            answer = [arr[i], arr[left], arr[right]]

        if total == 0:
            break
        elif total < 0:
            left += 1
        else:
            right -= 1

answer.sort()

for ans in answer:
    print(ans, end=" ")
