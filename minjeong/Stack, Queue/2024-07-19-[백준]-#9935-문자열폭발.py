# 최종 제출
import sys
input = sys.stdin.readline

# 초기화
s = input().rstrip()    # 전체 문자열
bomb = input().rstrip() # 폭발 문자열
stack = []              # 스택 자료구조
bomb_length = len(bomb) # 폭발문자열의 길이

# 스택만으로 문자열 폭발 탐색 및 폭발 처리
for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-bomb_length:]) == bomb:
        for _ in range(bomb_length):
            stack.pop()

# 정답 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')