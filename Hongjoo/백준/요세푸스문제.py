"""
[BOJ]#1158. 요세푸스문제: 실버 4
https://www.acmicpc.net/problem/1158

-1 ~ n 번쨰 사람 중  순서대로 k 번째 사람 제거 
- 출력 : 제거되는 순서대로 출력

#FL0W 
유형 : 구현, 큐 
원형 큐 배치하기
 7,3 : 0~ 6
 <3, 6, 2, 7, 5, 1, 4>
"""
import sys
N , K = map(int , sys.stdin.readline().split())

#1. 원형 큐 만들기 
elements = [i for i in range(1,N+1)]
answer = []
p = 0 
while elements : 
    p = (p + K-1) % len(elements)
    answer.append(elements.pop(p))
#2.출력 
print("<"+", ".join(list(map(str, answer))) + ">")
