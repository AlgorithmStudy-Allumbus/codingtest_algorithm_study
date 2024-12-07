"""
condition
1. NxN map , some apple , N+1 walls , 
2. snack 's time : size = 0 : 1 , right way

Rule 
1.먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2.만약 벽,자기자신의 몸과 부딪히면 게임이 끝난다. =game over 조건
<사과 - 몸길이 변화 > 
3.만약 이동한 칸에 사과 O => 그 칸에 있던 사과가 없어지고 꼬리 stay , 머리 길어짐 => 즉 몸길이 변함
4.만약 이동한 칸에 사과 X => 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다(즉, 담칸으로 이동만 함). 즉, 몸길이는 변하지 않는다.
-> 머리 부터 ,그리고 꼬리 이동(사과 유무)
#Variable
1. time , 2. 뱀이 차지하는 영역 : stack , 3. 

Flow
1. 입력을 통해 map, 이동 반경 


"""
import sys

''' 1. 입력 값 변수에 할당(field구축 , 뱀의 방향 정보)
- field : N+2
    빈 곳 = 0
    벽, 뱀의 위치 = -1 
    사과 = 1
'''

N = int(sys.stdin.readline()) # 보드 크기 => N+2*(q) 
K = int(sys.stdin.readline()) # 사과 개수

field = [[0 for _ in range(N+2)] for k in range(N+2)]
# 뱀의 첫 위치 & 벽
field[1][1] = -1
for i in range(len(field)):
    for j in range(len(field[0])) :
        if i in [0, N+1] or j in [0,N+1] : 
            field[i][j] = -1

# 사과 위치
for k in range(K) :
    i , j = map(int, sys.stdin.readline().split())
    field[i][j] = 1 

# 뱀의 방향 정보 -> rotate_time=[time, direction]  # 방향을 이동하기 전에 확인하여 t+1 로 저장

L   = int(sys.stdin.readline())
rotate_time = []
for l in range(L):
    t , d = sys.stdin.readline().split()
    rotate_time.append([int(t)+1,d])


"""
2. 게임 start 
- 뱀의 현재 차지하고 있는 위치 : snack = [[머리 좌표] , [몸통 좌표들],...,[꼬리 좌표]]
- & 차지하는 field = -1 
(1) 뱀이 도착한 위치의 field 번호 = -1(본인,벽) 이 아닐때 까지 이동
"""
def change_int_direction(time, current_direction) : # 방향 변환
    direction_map =  ['r','d','l','t'] * 2
    # direction_dict = {'r,':[0,1] ,'d' :[-1,0] ,'l':[0,-1] , 't':[1,0] }
    for ch_t, ch_d in rotate_time :
        if time == ch_t : # {'r,':[0,1] ,'d' :[-1,0] ,'l':[0,-1] , 't':[1,0] }
            # print(f"change direction ")
            idx = direction_map.index(current_direction)
            if ch_d == "D" : #right
                current_direction = direction_map[idx + 1] 
            elif ch_d == "L" :#left 
                current_direction = direction_map[idx - 1]
            break
    
    # direction = direction_dict[current_direction] # [0,1]
    return current_direction # [0,1]
from collections import deque
time = 0
snack = deque() # idx =0 머리 , -1 꼬리
snack_direction = 'r' # r,d,l, u
snack.append([1,1])
direction_dict = {'r':[0,1] ,'d' :[1,0] ,'l':[0,-1] , 't':[-1,0] }
while(1) :
    time += 1
    # print(f"##time : {time}")
    # 사과 확인 
    head_x , head_y = snack[0]
    #1. head 이동  - snack 영역 추가
    snack_direction = change_int_direction(time, snack_direction) 
    move_x , move_y = direction_dict[snack_direction]
    head_x += move_x  ; head_y += move_y
    # print(f"- snack_direction : {snack_direction} # {move_x},{move_y}")
    # print(f"new head : {head_x} , {head_y}")
    #2.현재 head 위치하는 곳의 조건 확인
    if field[head_x][head_y] == -1 : #game over 
        # print(f"!!!gameover : ")
        # print(field)
        # print(f"{head_x} , {head_y} = {field[head_x][head_y]}")
        break 
    elif field[head_x][head_y]  == 0 : # safe(빈곳)
        tail_x , tail_y = snack.pop() #W 꼬리 이동
        field[tail_x][tail_y] = 0
    # field[head_x][head_y]  == 0,1 (사과, 빈곳 )공통점 - 머리 이동 ,         
    field[head_x][head_y] = -1 #field  값 변경(뱀이 차지함) - 사과 먹음
    snack.appendleft([head_x,head_y]) # head 추가
#     print(snack)
print(time)