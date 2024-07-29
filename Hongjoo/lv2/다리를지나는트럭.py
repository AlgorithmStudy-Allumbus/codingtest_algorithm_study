from collections import deque
import copy
def solution(bridge_length, weight, truck_weights):
    answer = 0
    t=0
    run_truck = deque() # bride 올라간 weight
    timeline = [[0] for _ in range(len(truck_weights))]
    finish =[]
    # 통과 조건(bridge에 있는 시간 >= bridge_length)
    print(len(timeline))
    i=0 # new truck 번호
    while len(finish) <= len(truck_weights)and t<len(truck_weights):
        t+=1 ;
           #2. 나가기
        if t==1:
            run_truck.append(i)
            timeline[i] = 1
            continue
        for r in copy.deepcopy(run_truck) : 
            if timeline[r] > bridge_length : #내보내기
                run_truck.popleft()
                finish.append(r)
                print(f"out {r} ,t={timeline[r]} , run : {run_truck}")
            else :  #충족 x
                timeline[r] += 1
                print("# , run_truck", run_truck)
       
        #1. bridge 무게 조건 
        now_weight = 0
        for j in  copy.deepcopy(run_truck):
            now_weight += truck_weights[j]
        if now_weight + truck_weights[i] <= weight: # 올라감
            run_truck.append(i)
            timeline[i] = 1
        
    return answer