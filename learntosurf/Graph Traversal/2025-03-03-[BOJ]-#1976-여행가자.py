'''
3 > 도시의 수 N
3 > 여행 계획에 속한 도시의 수 M

> NxN 행렬 (N개의 줄에 N개의 정수) 
0 1 0 1번 도시는 2번 도시와 연결
1 0 1 2번 도시는 1,3번 도시와 연결
0 1 0 3번 도시는 2번 도시와 연결

i 번째 줄의 j번째 수 (i, j)는 i번째 도시에서 j번째 도시의 연결 정보 (i-j)
-> (i, j) = (j, i) 
1이면 연결, 0이면 연결 X
같은 도시 여러번 방문 가능 

1 2 3 > 여행 계획 (1번->2번->3번)
1-2-3 => 모두 연결되어 있어서 YES
'''

import sys 
input = sys.stdin.readline

N = int(input().strip()) # 도시의 수 
M = int(input().strip()) # 여행 계획에 속한 도시의 수

# 도시의 연결 정보 
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split()))) # NxN 행렬

plan = list(map(int, input().split())) # 여행 계획 

'''
그래서 어떻게..??
여행계획에 속한 도시들이 모두 연결되어있는지를 확인 
-> 첫번째 도시에서 출발해서 다음 도시로 이동하는지 하나씩 확인..?
'''
def travel():
    for i in range(M-1): # (M-1)번 반복하면서 현재 도시에서 다음 도시로 이동 가능 여부 확인 
        current_city = plan[i]-1 # 현재 도시
        next_city = plan[i+1]-1 # 다음 도시
        
        if graph[current_city][next_city] == 0: # 이동할 수 없는 경우 
            return 'NO'
    
    return 'YES'

print(travel())
'''
아 이렇게 하면 근데 경유 하는 경우 고려를 못함.. 아 아닌가/?
4
3
0 0 1 0 
0 0 0 1
1 0 0 0 
0 1 0 0
1 2 4
일때 No 

여러번 방문이 가능
'''