import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
# 1번부터 N번까지 사람을 큐에 넣기
people = deque([i+1 for i in range(N)])
answer = [] # 제거된 순서를 저장할 리스트

while people:
		# K-1번 앞의 원소를 빼서 뒤로 보냄 (원형 이동)
    for _ in range(K-1):
        cur = people.popleft()
        people.append(cur)
    # K번째에서 제거
    answer.append(people.popleft())

# 정답 출력
print("<" + ", ".join(map(str, answer)) + ">")