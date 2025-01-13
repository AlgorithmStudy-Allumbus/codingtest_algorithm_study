import sys
from collections import deque

input = sys.stdin.readline

# 입력 문자열 처리
S = deque(input().strip())
temp = deque([])  # 단어를 저장하는 임시 리스트
answer = deque([])  # 결과 저장 리스트

tag = False  # 태그 상태 확인

while S:
    # 태그 시작
    if S[0] == "<":
        tag = True

    # 태그 시작 또는 공백 처리
    if S[0] == " " or S[0] == "<":
        # temp에 저장된 단어 뒤집기
        while temp:
            answer.append(temp.pop())
        # 태그 내용 추가
        if tag:
            while S[0] != ">":
                answer.append(S.popleft())
            tag = False
        # 공백 또는 닫는 태그 추가
        answer.append(S.popleft())
    else:
        # 단어를 temp에 저장
        temp.append(S.popleft())

# 남아 있는 단어 처리
while temp:
    answer.append(temp.pop())

# 결과 출력
print(''.join(answer))
