import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())  # 거스름돈 액수
    alphabet = list(map(str, input().split()))
    alphabet = deque(alphabet)
    answer = alphabet.popleft() # 정답 문자열

    while alphabet:
        current = alphabet.popleft()
        if current <= answer[0]:  # 가장 앞의 문자와 비교. 더 앞에 있다면 가장 왼쪽에 붙이기
            answer = current + answer
        else:
            # 뒤에 있다면 가장 오른쪽에 붙이기
            answer += current

    print(answer)