"""
[프로그래머스] 거리두기 확인하기: 백트레킹 / lv2
https://school.programmers.co.kr/learn/courses/30/lessons/81302
"""
from collections import deque

dy =[1,-1,0,0] ; dx=[0,0,-1,1]         
def solution(places):
    answer = []
    for place in places : 
        # 1. 응시자 위치 확인 
        people = []
        for i in range(5) :
            for j in range(5) :
                if place[i][j] == "P":
                    people.append([i,j])
        #2. 응시자 별로 거리 확인하기
        def bfs(start):
            clv = 0 
            visited = [[-1]*5 for _ in range(5)] # 거리 저장하기(lv)
            q = deque([start]) 
            visited[start[0]][start[1]] = 0 
            while q  :
                cy,cx = q.popleft()
                clv = visited[cy][cx]
                if clv >= 2 : 
                    break
                for d in range(4):
                    ny,nx = cy + dy[d] , cx +dx[d]
                    if 0<= ny < 5 and 0 <= nx < 5 and visited[ny][nx] <= -1  : 
                        if place[ny][nx] == "X": 
                            visited[ny][nx] = clv +1 
                            continue
                        elif place[ny][nx] == "O":
                            q.append([ny,nx])
                            visited[ny][nx] = clv +1 
                        elif place[ny][nx] == "P" :
                            return False 
            return True 
        flag = True
        for p in range(len(people)):
            start = people[p]
            flag = bfs(start) 
            if not flag : 
                break
        if flag: 
            answer.append(1)
        else :
            answer.append(0)
        
            
    # print(people)
    # print(f"answer{answer}")
    return answer