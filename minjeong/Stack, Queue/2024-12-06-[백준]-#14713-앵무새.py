import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 앵무새 수
S = []  # 앵무새 문장
for _ in range(N):
    S.append(deque(input().split()))
L = deque(input().split())  # 받아 적은 문장

while L:
    current = L.popleft()  # 현재 단어
    found = False

    # 각 앵무새 문장에서 단어 찾기
    for s in S:
        if s and s[0] == current:  # 매칭되는 단어가 있다면
            s.popleft()  # 단어 제거
            found = True
            break

    if not found:  # 매칭되는 단어가 없으면 Impossible
        print("Impossible")
        exit()

# 모든 문장이 비었는지 확인
if any(s for s in S):  # S에 남은 문장이 있다면 Impossible
    print("Impossible")
else:
    print("Possible")