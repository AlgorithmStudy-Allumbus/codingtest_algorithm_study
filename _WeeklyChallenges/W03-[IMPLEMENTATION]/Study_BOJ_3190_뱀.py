'''
BOJ #3190. 뱀 (골드5)
https://www.acmicpc.net/problem/3190
유형: 구현, 시뮬레이션, 자료구조
'''


import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
maps = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):#사과의 위치
    x,y = map(int,input().split())
    maps[x][y] = 2
info = {}
l = int(input())
for _ in range(l):# 뱀의 방향변환정보 (초, 방향 L:왼쪽 D:오른쪽)
    sec, direct = input().split()
    info[int(sec)] = direct
time = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
x, y = 1, 1
maps[y][x] = 1
d = 0
snakes = deque([(1, 1)])

while True:
    nx, ny = x+dx[d], y+dy[d]
    # 뱀의 몸통에 닿거나 벽에 부딪히는 경우 종료
    if nx<=0 or ny<=0 or nx>n or ny>n or (nx,ny) in snakes:
        break
    # 사과를 먹지 못하면 꼬리 없애기
    if maps[ny][nx]!=2:
        a,b = snakes.popleft()
        maps[b][a]=0
    x, y = nx, ny
    maps[y][x] = 1
    snakes.append((nx, ny))
    time+=1
	
    # 시간에 해당하는 방향전환 정보가 있을 경우
    if time in info.keys():
        if info[time] == "D":
            d = (d+1)%4
        else:
            nd = 3 if d==0 else d-1
            d = nd
print(time+1)
