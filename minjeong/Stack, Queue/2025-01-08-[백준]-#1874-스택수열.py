import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 수열의 길이
stack = deque([])  # 스택 초기화
answer = deque([])  # 연산 기록
flag = True  # 수열을 만들 수 있는지 확인하는 플래그
current = 1  # 현재 push할 숫자

# n번 반복하며 수열 입력
for _ in range(n):
    num = int(input())

    # 현재 숫자가 수열의 값에 도달할 때까지 push
    while current <= num:
        stack.append(current)
        answer.append("+")
        current += 1

    # 스택 최상단이 수열의 값과 일치하면 pop
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        # 만들 수 없는 경우
        flag = False

# 결과 출력
if flag:
    for a in answer:
        print(a)
else:
    print("NO")
