import sys
input = sys.stdin.readline

# 입력
N = int(input())
arr = list(map(int, input().split()))

arr.sort()  # 투 포인터를 적용하기 위해 배열을 오름차순으로 정렬
cnt = 0     # 좋은 수 개수

for i in range(N):
    target = arr[i]  # 현재 '좋은 수'인지 확인할 목표값
    left, right = 0, N-1
    while left < right:
        # 타겟 값과 동일할 경우
        if target == arr[left] + arr[right]:
            if right == i:  # target이 양수이고 자기 자신이라면
                right -= 1
            elif left == i:  # target이 음수이고 자기 자신이라면
                left += 1
            else:  # 좋은 수 찾음
                cnt += 1
                break
        # 타겟 값이 더 클 경우, 왼쪽 포인터를 오른쪽으로 이동
        elif target > arr[left] + arr[right]:
            left += 1
        # 타겟 값이 더 작을 경우, 오른쪽 포인터를 왼쪽으로 이동
        else:
            right -= 1

# 정답 출력
print(cnt)
