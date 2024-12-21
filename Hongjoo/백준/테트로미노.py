"""
2024.12.14, 과제문제, 2hour 
"""

import sys

#0. 입력 변수를 통해 각 칸에 정수값을 가지는 NxM 행 graph 정의
N,M = map(int,sys.stdin.readline().split())
graph=[[0 for _ in range(M)] for k in range(N)]
for i in range(N)  :
  graph[i] = list( map(int,sys.stdin.readline().split()))

max_num = 0 
#2. graph 내 특정 칸(절대좌표 , (row,col)) 기준에서 
#가질 수 있는 19개 형태의 테트로미노 영역 속 정수들의 합의 최대 값 찾기
#함수 내부에선 상대좌표(r,c)로 칸의 위치 파악
def tetries_sum (row,col):
  sub_maxsum = 0
  #2-1. 19개 테트로미노는 크게 4가지 직사각형 형태의 영역으로 소분류 
  for n,m in [[1,4],[2,3],[3,2],[4,1]]: 
    sub_sum=0 # 특정 칸(row,col)에서 가질 수 있는 정수합 중 최대값

    #2-2. 19개 중 graph(NxM) 안에서 가질 수 있는 테트로미노만 적용
    if row>=0 and row + n <=N and col>=0 and col+m <=M : 
      #(1) 직사각형(4가지) 영역내 모든 정수값들의 합
      for r in range(n): 
        for c in range(m):
          
          sub_sum +=graph[row + r][col+ c]
      #(2) 2x3 과 3x2 형태 영역 중 빠져야 하는 2개 칸들의 정수값의 합 구하기 
      if n==2 and m==3 or n==3 and m==2 : 
        del_tmp = list()
        #a. 2x3 직사각형 영역 중 빠져야 하는 2개 칸들의 조합(상대좌표) : 10개
        if n == 2 and m == 3 : 
          del_candidates = [[[0,0],[0,1]],[[0,1],[0,2]],[[1,0],[1,1]],[[1,1],[1,2]],
          [[0,0],[1,0]],[[0,2],[1,2]],[[0,0],[1,2]],[[0,2],[1,0]],[[0,0],[0,2]],[[1,0],[1,2]]
          ]
        #b. 3x2 직사각형 영역 중 빠져야 하는 2개 칸들의 조합(상대좌표) : 10개
        elif n==3 and m == 2 :
          del_candidates = [[[0,0],[0,1]],
                            [[0,0],[1,0]],[[0,1],[1,1]],[[1,0],[2,0]],[[1,1],[2,1]],[[2,0],[2,1]],
                            [[0,0],[2,1]],[[2,0],[0,1]],[[0,0],[2,0]],[[0,1],[2,1]]]
        #(3) 빼야하는 2개 칸들의 조합들(10종류)에 대해 정수값의 합 구하기  
        for n1,n2 in del_candidates:
          del_tmp.append(graph[row +n1[0]][col+ n1[1]] +graph[row+n2[0]][col+n2[1]])
        #(4) 2x3 또는 3x2 영역에서 합의 최대값을 구하기 위해 10개의 뺄 값 중 최소값으로 빼기
        sub_sum -= min(del_tmp) 
           
      sub_maxsum = max(sub_maxsum , sub_sum) # 최대값 업데이트
      
       
    else : #테트로미노가 graph 범위를 벗어남  -> skip
      continue
  return sub_maxsum # 절대좌표(row,col) 칸 기준에서 가질 수 있는 합의 최대

max_sum = 0 #전체 graph 내 합의 최대값
# 1. graph 내 모든 칸을 순회
for i in range(N) :
  for j in range(M) :
    new_sub_sum=tetries_sum(i,j) # 2. 절대 좌표(i,j) 칸 기준에서 가질 수 있는 합의 최대 값 계산 
    max_sum= max(max_sum,new_sub_sum)  #3.전체 graph 내 합의 최대값 업데이트
print(max_sum)
