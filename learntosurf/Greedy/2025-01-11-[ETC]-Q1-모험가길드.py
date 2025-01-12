import sys 
input = sys.stdin.readline

N = int(input())
fear = list(map(int, input().split()))
fear.sort() # 오름차순 정렬 

group = 0 # 그룹 수
member = 0 # 현재 그룹에 포함된 모험가의 수

for i in fear: 
    # 현재 그룹에 인원 추가 
    member += 1 
    if member >= i: # 현재 그룹에 포함된 모험가의 수가 공포도 이상이면 그룹 결성
        group += 1 
        member = 0 # 현재 그룹에 포함된 인원 초기화 

print(group)