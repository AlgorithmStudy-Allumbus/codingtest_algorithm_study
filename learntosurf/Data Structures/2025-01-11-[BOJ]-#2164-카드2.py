import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
cards = deque(range(1, N + 1))  # 1부터 N까지의 숫자를 덱에 저장

while len(cards) > 1:
    cards.popleft()  # 제일 위의 카드를 버림
    cards.append(cards.popleft())  # 그다음 카드를 아래로 옮김

print(cards[0])  # 마지막으로 남은 카드 출력