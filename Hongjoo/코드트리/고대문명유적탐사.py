"""
#2024삼성 상반기 오전1번 문제 / 고대문명유적탐사
#링크 : https://www.codetree.ai/ko/frequent-problems/problems/ancient-ruin-exploration/description?introductionSetId=&bookmarkId=


"""
"""
# 유형 : 걍 구현 
- . 5x5위 7가지 유물(1-7)
1. 탐사 진행 - 지정된 3x3회전 시계방향으로 [90,180 , 270] 중 하나의 각도로 회전
    => 각 회전시 "각도| 획득가치 | 중심좌표" 저장  
    - (1) 유물 1차 획득 가치 최대화
    - (2) 회전 각도 최소화
    - (3) 회전 중심 좌표 열(row)이 최소 -> 행 최소


2. 유물 획득 
- 3개 같은 종류 이웃하면 -> 사라지는 조각 개수 = 유물 가지 => 필트에 빔
- 생성 순서는 유적 벽면 순서 -> 열이 작은 쪽 -> & 행 큰것 순서 up 
- 조각 고갈 문제는 없음, 단 사용한 조각은 재활용 x > 

3. 탐사 반복 (출력조건)
- K번 (1번 : 탐사진행 -> 유물획득) => 획득 유물 가치 출력
- 중간 획득 유물 방법 존재 x -> 종료 (출력 : x )

"""

"""
<전체 flow> 
# 0. 변수 입력 : 탐사 회수 K , 유물 스페어 개수 M 
### K 번 반복
# 중심좌표 후보군 9개 / 각도 후보군 3개 -> 27번 반복 
#1. def 회전(중심좌표, 각도)

#2. 유물 획득 -> 유물 가치 저장
#-> 27번 반복
#3. 해당 턴에서 Best choice 인 상황 결정
# 3.유물 업데이트 
### 
"""
"""
input : 중심 좌표, angle , field
ouptut : 변환된 field

위치 idx : 
[[i-1 , j-1], [i-1, j],[i-1,j+1],[i+1,j-1] , [i,j] [ i,j+1], [i+1,j-1],[i+1,j],[i+1,j+1]]
90 = [7,5,1,8,5,2,9,6,3]
80 = [7,8,9,4,5,6,1,2,3]
270 = [1,4,7,2,5,8,3,6,9]
"""
"""
# 유물 획득 함수 : BFS
# 현 field  상황에서 얻을 수 있는 경우의 수 
def get_old (field):
"""

# 중심 좌표 후보군 +
# 0. 입력 변수 입력 받기
K , M = map(int, input().split())
# 0-1. 초기 필드 값 받기

sfield = [list(map(int,input().split())) for _ in range(5) ]
wall = list(map(int, input().split()))
# 상하좌우 
dy = [-1,1,0,0]
dx = [0,0,-1,1]


# (1) 90/180/270 회전 함수 
def rotate(i,j, angle ,field) :
    old_33=[[i-1 , j-1], [i-1, j],[i-1,j+1],[i+1,j-1] , [i,j] ,[ i,j+1], [i+1,j-1],[i+1,j],[i+1,j+1]]
    ro_pos =[]
    if angle == "90":
        ro_pos  = [6,4,0,7,4,1,8,5,2]
    elif angle == "180":
        ro_pos  = [6,7,8,3,4,5,0,1,2]
    else:
        ro_pos  = [0,3,6,1,4,7,2,5,8]
    new_field = [row[:] for row in field]
    for p in range(0,9):

       old = field[old_33[p][0]][old_33[p][1]]
       new_field[old_33[ro_pos.index(p)][0]][old_33[ro_pos.index(p)][1]] = old
    return field

# 현 field 상황에서 가치 업데이트
def get_old (field):
    del_pos = []
    visited = [] # 방문 여부 
    oldest = [] # 각 start point에서 연결된 유물 위치 
    for i in range(5):
        for j in range(5):
            if [i,j] not in visited : 
                # start point와 같은 종류의 유물만 획득 가능
                q = []
                q.append([i,j])
                visited.append([i,j])
                while q : 
                    cy,cx = q.pop()
                    for d in range(4) :
                        ny , nx = cy + dy[d] , cx + dx[d] 
                        if 0 <= ny < 5 and 0 <= nx < 5 :
                            if [ny,nx] not in  visited and field[ny][nx] == field[cy][cx]:
                                q.append([ny,nx])
                                visited.append([ny,nx])
                                oldest.append([ny,nx])
                
                    # 획득 있으면 -> 유물 개수 + 위치 누적
                if len(oldest) >= 3 :  # 3개 이상 연결시 획득 가능
                    del_pos.extend(oldest)
                    # print(del_pos)
                    oldest.clear()

    return len(del_pos) , del_pos
# best 상황 선택
def cur_best(current_case):
    arr = sorted(current_case , key=lambda x : (-x[0] , x[1] , x[2], x[3]))
    return arr[0] 


answer = []

for k in range(K):
    current_case = [] # 27경우 [유물가지, 각도 , 열, 행 ,삭제 위치 ]
    # 9개의 중심좌표 후보군
    ro_sub = [90,180,270]
    center_sub= [[1,1], [1,2],[1,3],[2,1] ,[2,2] ,[2,3],[3,1],[3,2],[3,3]]
    for center_y  , center_x in center_sub :
        for ro_angle in ro_sub : 
            sub_field = rotate(center_y,center_x, ro_angle ,sfield) 
            value_sub , del_sub  = get_old (sub_field)
            current_case.append([value_sub, ro_angle,  center_y, center_x, sub_field ,del_sub])
            
    #3. 해당 턴에서 베스트 상황 1개 선택
    # value 가 없는 경우 -> 끝
    if len(current_case) <= 0 : 
        break 
    best_sit=cur_best(current_case)
    answer.append(best_sit[0])
    #4. fiedl 상황 업데이트
    # 유물 매꾸기 - sort로 삭제된 위치 정렬 후 wall(유물벽면) 수행
    arr = sorted(best_sit[-1] , key = lambda x : (x[0] , -x[1])) # 사라진 유물 위치 
    sfield = best_sit[-2]
    pointer = 0 
    for y,x in arr : 
        node = wall[pointer]
        sfield[y][x] = node 
        pointer= (pointer+1)%len(wall)
        
print(answer)