import sys
from collections import deque

input = sys.stdin.readline


def AC():
    p = input().strip()  # 수행할 함수
    n = int(input())  # 배열 크기
    nums = input().strip()  # 배열 입력

    # 배열 처리
    if nums == "[]":
        nums = deque()
    else:
        nums = deque(map(int, nums[1:-1].split(",")))

    reverse = False  # 뒤집기 플래그
    for command in p:
        if command == "R":
            reverse = not reverse  # R이 나올 때마다 뒤집기 상태 토글
        elif command == "D":
            if not nums:  # 비어있는 경우 에러 출력
                print("error")
                return
            if reverse:  # 뒤집힌 상태라면 뒤에서 제거
                nums.pop()
            else:  # 그렇지 않다면 앞에서 제거
                nums.popleft()

    # 최종 출력
    if reverse:
        nums.reverse()  # 필요시 뒤집기
    print("[" + ",".join(map(str, nums)) + "]")


# 테스트 케이스 처리
T = int(input())  # 테스트 케이스 수
for _ in range(T):
    AC()