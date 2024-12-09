"""
N :물건 개수 , K : 제한 무게
W , V :  개별 물건 무게 , 가지
goal: max V 

6 4 3 5
13 8 6 12

-> 13/6 ,8/4 , 6/3 , 5/2
goal : 낮은 무게부터 넣기
[[3, 6], [4, 8], [5, 12], [6, 13]]
1. sum(W) <= K인 조합 찾기 
2. w확인? 
"""
#1. 변수 입력 받기
import sys 
objects = list()
N , K = map(int,sys.stdin.readline().split() )
for i in range(N) :
    W , V =  map(int,sys.stdin.readline().split() )
    objects.append([W,V]) 

# 가벼운 순으로 나열
objects = sorted(objects)
# print(objects) 
bags = list() 
#2. two point
# start + window 
# for start  in range(len(objects)) : 
#     for end in range(1,len(objects)) : # end point 
start = 0 ; end= 1 
max_values = 0
# 물건 1개의 무게 < target weight 

while start < N and start < end and objects[end-1][0] <=  K :
    
    Subset = objects[start : end] # length = start -end 
    currnet_weight = 0  ; current_values = 0
    # print(Subset)
    
    for w,v in Subset : 
        currnet_weight += w 
        current_values += v

    if currnet_weight <= K :# K 보다 현재 배낭 무게가 가벼우면 업데이트 진행 
        max_values = max(max_values , current_values)
        end += 1
    elif currnet_weight <= K  or end > N:# current_weight > k 이거나  end == N 이면 초기화
        current_values = 0 
        start += 1
        end = start +1
    # print("end",end )
    # if end > N:
    #     start += 1
    #     end = start +1
    #     # print(f"update { max_values}")
print(max_values)