"""
https://www.acmicpc.net/problem/5567
1-> 2다리 이하 친구 관계만 초대 -> 총 인원수 파악
1-2-3-4-5
"""
import sys
from collections import deque
#1.양방향 인접 리스트 만들기
input =sys.stdin.readline

N = int(input())
M = int(input())
friends = [[] for _ in range(N+1)] # 1~ n 번까지
for i in range(1,M+1):
  x,y = map(int, input().split())
  friends[x].append(y)
  friends[y].append(x)

#2. lv2 이하인 BFS 가즈아~
start = 1 
q = deque([[start,0]]) # 학번, 관계 거리
visited = [start]
answer =-1
while q : 
  cnum , crelationship= q.popleft()
  if crelationship >= 3: 
    break # 거리가3 넘으면 강제종료
  answer +=1 
  # print(f"#{cnum} : {crelationship}")
  for nn in friends[cnum] :
    if nn not in visited : 
      q.append([nn, crelationship+1])
      visited.append(nn)
      

# print(visited)
print(answer)