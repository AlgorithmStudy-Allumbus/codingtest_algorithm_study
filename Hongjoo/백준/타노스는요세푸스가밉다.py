"""
[BOJ] #28066.타노스는 요세푸스가 밉다 : 큐 / 실버2
https://www.acmicpc.net/problem/28066
"""
import sys
from collections import deque
input = sys.stdin.readline

N , K = map(int , input().split())

elements = deque([i for i in range(1, N+1)])
start = 0 
while len(elements) > 1 : # 탐색 종료 조건 : 청설모가 1마리 이하로 남을 떄 

  if len(elements) < K : # K보다 적게 남아있으면, 강제종료
    print(elements[0])
    exit()
  # elements 개수 >= K
  first = elements[0]
  # 1. K개 삭제(first 도 포함해서 일단 삭제) 
  for i in range(K): # K-1 개 삭제

    elements.popleft()

  #2.기본 첫번째 요소를 맨 뒤쪽에 추가,  
  # 다음 첫번째 요소는 자동 맨 앞(idx= 0 )으로 배치됨
  elements.append(first)

  
print(elements[0])