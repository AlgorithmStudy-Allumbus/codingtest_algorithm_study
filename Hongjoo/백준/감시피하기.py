"""
role : 1. T , S , O 
T - 상하좌우 like 룩  
  - 장애물 막히면 뒤에 못봄

1. T 가 볼 수 있는 영역 -> S 탐색 여부 확인
2. 


"""
import sys
def backtracking(cnt):
    global flag

    # 3개 장애믈 설치 끝나면
    if cnt == 3 :
        # 선생님들 위치에서 감시
        if check_S():
            flag = True # 성공하면 flag를 True로 초기화
            return True
    else : # 모든 빈 공간에 장애물 3개씩 설치해보기
        for x  in range(n):
            for y in range(n) :
                if graph[x][y] == "X":
                    graph[x][y] = "O"
                    backtracking(cnt+1) # backtraking
                    graph[x][y] = "X" 
        

def check_S() : 
    #check_S : 선생님 시야 함수 (bfs -> 근데 dfs에 가깝지 않나???)
    #check = True # T가 S 를 못 찾음
    
    # 상하좌우 움직이는 배열
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for t in teachers : # 선생님 위치에서
        
        for k in range(4): #상하좌우 탐색
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            # 선생님 x,y 좌표
            while  0 <= nx < n and 0 <= ny < n : # graph 범위 밖 넘어가는 것 차단
                if graph[nx][ny] == "O" : #방애물 있으면 해당 방향 스킵
                    break
                if graph[nx][ny] == "S"  : # S 가 있으면 실패
                     return False
                nx += dx[k]
                ny += dy[k]

    # 모두 통과하면 S가 안보이는 것으로 성공
    return True
        

# input 받기 -  graph , T 위치 , X 위치
n = int(sys.stdin.readline())
flag = False # (답) 전체 시야 차단 yes or no  
graph = [] # 전체 MAP 위치
teachers = list () # 선생님 (T) 좌표

for i in range(n):
    graph.append(list(map(str , sys.stdin.readline().split())))
    for j in range(n):
        if graph[i][j] == "T": # 선생님 있는 좌표 저장
            teachers.append([i,j])


# BFS 
backtracking(0)

if flag :
    print("YES")
else :
    print("NO")
