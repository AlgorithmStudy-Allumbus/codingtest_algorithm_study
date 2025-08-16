"""
[BOJ]#16987.계란으로계란치기:백트레킹/골드5
https://www.acmicpc.net/problem/16987
"""
import sys

#0. 입력 변수 정의 및 초기화 하기
input= sys.stdin.readline
N = int(input())
eggs = [[] for _ in range(N)]

for i in range(N):
  durability , weight =map(int ,input().split())
  eggs[i] = [durability , weight]

# 1. backtracking 수행하기
max_cnt = 0 
def backtracking(idx,cnt) :
  global max_cnt
  print(f"stage {idx}")
  # pruning 조건 : 현재 남은 횟수로 2개씩 깨도  max_cnt 업데이트 불가 경우
  if max_cnt >= (cnt + (N-idx)*2):
    return 0
  #1. 종료 조건 : (1. 모든 계란 선택 완료 n == N)
  if idx >= N : # 1개 이하 남아있을떄 
    max_cnt = max(max_cnt , cnt)
    return 0 
  
  #1-2. 현재 선택한 계란 (idx) 가 깨져있는 경우
  if eggs[idx][0] <= 0 : 
    backtracking(idx+1 , cnt)
  #2.동작 과정- 계란 깨기
  else : # 현재 계란 lived -> 부딫힐 계란 선택 & 부딫치기
    flag =False
    for j in range(N) :#현재 계란 부딫칠 계란 선택 (본인idx 아님 or 생존 )
      if j!= idx and eggs[j][0] > 0 : 
        # 충돌
        eggs[idx] =eggs[idx] -eggs[j][1]
        eggs[j] =eggs[j] -eggs[idx][1]
        backtracking(idx+1 , cnt+int(eggs[idx][0]<=0) + int(eggs[j][0]<=0) ) # 충돌 계산하기
        flag = True
        # 충돌 원상 복귀
        eggs[idx] =eggs[idx] +eggs[j][1]
        eggs[j] =eggs[j] +eggs[idx][1]
    # 한 번도 안 깨짐 -> 선택한 idx 내려두고 다음 idx +1 로 이동  
    if not flag : 
      backtracking(idx+1 , cnt )

  return 0 

backtracking(0 ,0)
print(max_cnt)