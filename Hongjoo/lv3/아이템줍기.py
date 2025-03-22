"""
2hour 
- 직사각형 바깥 테두리 이동
 - x축, y축 좌표가 같은 경우 없음(꼭짓점, 변 공유 x  )
 - 분리x, 포함x  => only 겹침
goal) 캐릭터(start) -> 아이템 최단거리(BFS)

#key idea : 좌표 & grid 2배 처리하기
(참고.https://jyeonnyang2.tistory.com/247#google_vignette)
#1. 인접 행렬
-field[x][y] =  길에 해당하는 (x,y) 칸 = 1 ,길 x 인 칸은 (x,y )= 0 

-(1) 각 직사각형 테두리에 해당하는 좌표 선출
- (2) A- > B 각 범위에 겹치는 테두리 자표 제거[필터링]
    -> 내부 빈 공간은 상관x 
#2. BFS
- visited 사용 to 누적 거리 
"""
from collections import deque
def get_outlier(x1,y1,x2,y2):

    pos_outliers = list()
    # 가로 
    for x in range(x1,x2+1,1):
        pos_outliers.append([x,y1])
        pos_outliers.append([x,y2])
    # 세로
    for y in range(y1, y2+1, 1):
        if  [x1,y] in pos_outliers or [x2,y] in pos_outliers:
            continue
        pos_outliers.append([x1,y])
        pos_outliers.append([x2,y])
    return sorted(pos_outliers)
        
        
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    field = [[0 for _ in range(51*2)] for k in range(51*2)]
    #인접 행렬
    characterX, characterY = characterX*2 , characterY*2
    itemX, itemY = itemX*2 , itemY*2
    #1.각 직사각형 칸 획득
    for k in range(len(rectangle)):
        #outlier 칸 찾기
        x1,y1 ,x2 ,y2 = rectangle[k]
        x1 = x1*2 ; x2 = x2*2 ; y1 = y1*2 ; y2 = y2*2 # 2배 
        outliers = get_outlier(x1,y1,x2,y2)
        
        #필터링
        # 모든 변 = 1  - 영역 겹치는 모서리만 =0
        for i in range(len(outliers)):
            out_x , out_y= outliers[i]
            field[out_x][out_y] = 1 
        # 영역 겹치는 모서리 탐색 -> =0 
        for j in range(len(rectangle)) : 
            if j == k : # 본인껀 스킵
                continue
            fil_x1 , fil_y1 , fil_x2 , fil_y2 =  rectangle[j]
            fil_x1 , fil_y1  =fil_x1*2 , fil_y1*2
            fil_x2 , fil_y2  = fil_x2*2 , fil_y2*2 
            for i in range(len(outliers)):
                out_x , out_y = outliers[i]
                # 면적이 겹침 -> 필터링
                if fil_x2 > out_x > fil_x1 and fil_y2 > out_y > fil_y1: 
                    field[out_x][out_y] = 0 
        
        # for i in range(51):
        #     for k in range(51):
        #         if field[i][k] == 1:
        #             print (f"[{i},{k}")

    # stage 2. BFS로 최단 거리 찾기
    # 상하좌우
    dx =[0,0,1,-1]
    dy= [1,-1,0,0]
    queue = deque([(characterX,characterY)]) #queue 초기화
    field[characterX][characterY]=0
    while queue : 
        cur_x, cur_y = queue.popleft()
        #인접 노드
        for idx in range(4):
            # 루트만 가능
            next_x ,next_y = cur_x + dx[idx] , cur_y + dy[idx]
            if field[next_x][next_y] == 1   : # 방문 x & 길
                field[next_x][next_y] = field[cur_x][cur_y] +1 
                # print(f"#{field[next_x][next_y]}")
                if next_x == itemX and next_y == itemY: # 목적지 도착 -> 결과 반환
                    # print(f"#####{field[next_x][next_y]}")
                    return field[next_x][next_y]//2
                    break
                queue.append((next_x,next_y))
                
        # print(f"#: {cur_x},{cur_y} => {field[cur_x][cur_y]}")
        
        # print(f">{queue}")
        # print(f"##{field[next_x][next_y]}")
    
    
    return answer