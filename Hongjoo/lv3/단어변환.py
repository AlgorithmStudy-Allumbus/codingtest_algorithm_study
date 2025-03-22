# 최소 편집 거리 =1 확인
def check_edit1(a,b):
    diff= 0 
    for i in range(len(a)) :
        if a[i] != b[i] :
            diff+=1
        if diff > 1 : 
            return False
    if diff == 1 : 
        return True
        
from collections import deque
def solution(begin, target, words):
    answer = 0
    #excep1 :words 에 target없으면 -> 변환 불가
    if target not in words :
        return 0 
    
    # 1. 인접 graph 생성
    graph = [[] for _ in range(len(words)+2)] 
    # begin -> words, target 단방향 
    for k in range(len(words)) :
        if check_edit1(begin, words[k]) :
            graph[0].append(k+1)
    if check_edit1(begin,target):
        graph[0].append(len(words)+1)
    # words -> wrods_1(쌍방향) , target(단방향)    
    for k in range(len(words)):
        for j in range(k ,len(words)):
            if check_edit1(words[k], words[j]):
                graph[k+1].append(j+1)
                graph[j+1].append(k+1)
        if check_edit1(words[k], target):
            graph[k+1].append(len(words)+1)

    #2.BFS 
    visited = [ 0 for _ in range(len(words)+2)]
    def bfs(visited):
        visited[0] = 0
        queue = deque()
        queue.append(0)

        while queue :
            curr_idx = queue.popleft()
            if len(graph[curr_idx]) <= 0 : # 이웃한 놈이 없는 경우 => return 0 
                return 0

            for next_idx in graph[curr_idx] : 
                if not visited[next_idx] :  

                    queue.append(next_idx)
                    visited[next_idx] = visited[curr_idx] + 1 

                if visited[-1] : #성공
                    return visited[-1]
        
        return visited[-1] 
    
    
    # print(graph)