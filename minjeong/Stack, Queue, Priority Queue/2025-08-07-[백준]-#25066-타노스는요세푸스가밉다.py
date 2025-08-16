import sys
from collections import deque
input = sys.stdin.readline

# 청설모 K-1마리를 제거하는 함수
def remove():
    global squirrels
    cnt = K - 1
    while cnt > 0 and squirrels:  # squirrels이 비지 않았는지 확인
        squirrels.popleft()
        cnt -= 1

N, K = map(int, input().split())
squirrels = deque([i+1 for i in range(N)])  # 청설모 번호 초기화
answer = 0  # 마지막으로 남는 청설모의 번호

# 청설모가 1마리 남을 때까지 반복
while len(squirrels) > 1:
    # 남은 청설모가 K보다 적으면 첫 번째 제외 모두 제거
    if len(squirrels) < K:
        print(squirrels[0])
        exit()

    # 첫 번째 청설모를 맨 뒤로 보냄
    squirrels.append(squirrels.popleft())
    # 첫 번째 청설모를 제외한 K-1마리를 제거
    remove()

# 마지막으로 남은 청설모 출력
print(squirrels[0])