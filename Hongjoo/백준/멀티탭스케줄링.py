"""
콘센트에 남은 기기 중 담 순번 없거나 가장 나중인 것 부터 교체 
DP..?
"""
import sys
N , K = map(int,sys.stdin.readline().split())
#1. 사용순서
use_case  = list(map(int,sys.stdin.readline().split()))
timelines =[[] for _ in range(K+1)] # idx : 기기 번호, value : times(순번)

# 2. dp 리스트 만들기 
for name in range(len(use_case)): # 0~k 초
  for idx in range(1,K+1): # 1~k번호 device  
    if idx == use_case[name]:
      timelines[idx].append(name) 

# 시간 별로 plug in 업데이트 
# plug in 한 기기 중 다음 업데이트가 늦는 기기 부터 plut out -> 교체 

cnt = 0 
current_plug = [] 
for time in range(K):
  current_device = use_case[time]
  #0. current_device가 현재 plug에 그대로 존재하는 경우 , continue
  if current_device in current_plug :
    timelines[current_device].pop(0) 
    continue

  #1. plug 가 남으면 -> 그냥 넣기
  if len(current_plug) < N : 
    current_plug.append(current_device)
    timelines[current_device].pop(0) 

  #2. plug 공간 없으면 -> plug out할 것 찾기-> 교체
  else :
    changed_device_idx = 0
    plug_out_hole = 0 
    for hole in range(N) :
      if len(timelines[current_plug[hole]]) <=0 : # 만약 다음 순번에서 사용 안하는 경우 , 바로 교체 장치로 선정
        plug_out_hole = hole
        break
      if timelines[current_plug[hole]][0] >changed_device_idx:
        changed_device_idx = timelines[current_plug[hole]][0] # next time
        plug_out_hole = hole 
    #plug out
    cnt +=  1
    current_plug.pop(plug_out_hole)
    # 교체
    current_plug.append(current_device)
    timelines[current_device].pop(0)

print(cnt)