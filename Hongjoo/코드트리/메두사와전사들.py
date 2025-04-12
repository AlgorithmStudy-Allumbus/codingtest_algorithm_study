"""
BFS , 구현 , 시뮬레이션
"""
#상 o, 우상,  우, 우하 , 하, 좌하, 좌, 좌상
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]
#디버깅 용
def myprint(arr):
  for lst in arr: 
    print(*lst) # 2행 리시트는 1열이 1 instacne
  print()

# [0] BFS 로 메듀사 최단경로  : 도로 따라 공원까지 - 상하좌우
# route = find_route(si,sj,ei,ej)
from collections import deque
def find_route(si,sj,ei,ej): 
  q = deque()
  v = [ [0]*N for _ in range(N)] # 방문 여부 & *직전 위치*

  q.append((si,sj))
  v[si][sj] = (si,sj) # 직전 위치 저장

  while q : 
    ci, cj = q.popleft()

    # 목적지 도착 -> 경로 저장
    if (ci,cj)==(ei,ej) :

      route = []
      ci,cj = v[ci][cj]
      while (ci,cj) !=(si,sj): # 출발지가 아니면 저장
        route.append((ci,cj))
        ci,cj = v[ci][cj]
      return route[::-1] #역순(메듀사 이동 start- > end  순서대로)
  
    # 4방향(상하좌우), 범위내 , 미방문 ,조건(==0)
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
      ni, nj = ci+di , cj+ dj
      if 0<= ni <N and 0<=nj <N and v[ni][nj]== 0 and arr[ni][nj] ==0:
        q.append((ni,nj))
        v[ni][nj] = (ci,cj) # 바로 이전 좌표 저장

  #여기까지 오면? : 목적지 못찾음
  return -1


#  mark_line(v,ni,nj,dr)
def mark_line(v,ci,cj,dr):  # dir 방향 직선으로 : M ~>1 "w ~2"

  while 0<= ci< N and 0 <= cj<N: # 범위 나가는걸 방지
    v[ci][cj] = 2 # 시각적 구분을 위해 2로 표기 = safe 존
    ci,cj = ci+di[dr],cj+dj[dr] # 다음 dr 방향 칸 이동 

  

def mark_safe(v,si ,sj ,dr,org_dr): # si ,sj : 전사 위치
  #[1] 직선방향표기
  ci,cj = si+di[dr], sj+dj[dr]

  mark_line(v,ci,cj,dr) # v에 dr방향으로 이동 가능 지역 표시
 
  #[2]전사가 바라보는 방향으로 한줄 식 표시 : 전사에게 가려져 이동 가능 지역
  ci,cj = si+di[org_dr],sj+dj[org_dr] # 이동한 svf poin 초기화
  
  while 0<=ci<N and 0<=cj<N:          # 범위내라면 계속 진행
    mark_line(v,ci,cj,dr)
    ci,cj = ci+di[org_dr],cj+dj[org_dr] # org_dir로 point(대각선) 위치 이동


# tv , tstone = make_stone(marr , mi , mj dr) >>>tv , tston

def make_stone (marr, mi,mj,dr):
  v = [[0]*N for _ in range(N)]
  cnt = 0 # stone된 병사 개수
  
#   myprint(marr)
  #[1] dr 방향으로 w(>0) 만날때 까지 1 표시 , 이후 2 표시
  ni, nj = mi + di[dr] , mj+dj[dr]
  
  while 0<=ni<N and 0<=nj<N : # 범위내리면서 계속 진행
    v[ni][nj] = 1
    
    if marr[ni][nj] > 0 : # 병사 w 만남
      cnt+=marr[ni][nj] # 해당 영역의 모든 w 석화
      ni, nj = ni + di[dr] , nj+dj[dr] # 다음 칸으로 이동
  
      mark_line(v,ni,nj,dr) # v에 dr 방향으로 이동 가능 지역 표시

      break
    ni, nj = ni + di[dr] , nj+dj[dr]
  #[2] dr -1 ,dr +1 방향으로 M의 시선 동일 처리, 대각선 원점 잡고 dr 방향으로 처리
  for org_dr in ((dr-1)%8 , (dr+1)%8):
    si,sj = mi+di[org_dr], mj+dj[org_dr] # 첫 대각선 위치부터 체크

    # 대각선 시야각 영역 확인
    while 0<=si <N and 0<=sj <N : # 대각선 방향으로 초기 위치 탐색 후 직선 시선
      if v[si][sj] == 0 and marr[si][sj]> 0: # 전사 만남
        v[si][sj] = 1 
        cnt += marr[si][sj]
        mark_safe(v,si,sj,dr,org_dr) # 전사가 바라보는 방향으로 safe(이동 가능 범위) 표시
        break
      # W 가 길 중간에 있는 경우
      ci ,cj = si,sj # 첫 위치가 전사가 아닐 경우는 직선으로
      while 0 <= ci <N and 0<= cj <N: # 범위 내리면서 계속 진행
        if v[ci][cj]==0: # 처음 방문
          v[ci][cj] = 1 
          if marr[ci][cj]>0 : # 전사로 막히면
            cnt+= marr[ci][cj]
            mark_safe(v, ci,cj,dr,org_dr) # v에서 dr 방향으로 이동 가능 지역 표시
            break
        else :  
          break
        ci,cj = ci+di[dr], cj+dj[dr]

      si,sj = si+di[org_dr], sj+dj[org_dr]
  return v, cnt

# move_cnt , attk_cnt = move_men(v,mi,mj)

def move_men(v,mi,mj) :
  # [3] 전사의 이동 - (상하좌우)(좌우상하) 메두사 시야 아니면 (!=1)
  move , attk = 0,0
  for dirs in (((-1,0),(1,0),(0,-1),(0,1)), ((0,-1),(0,1),(-1,0),(1,0))):
    for idx in range(len(men)-1,-1,-1): 
      ci ,cj = men[idx] 
      if v[ci][cj] == 1 : # 메듀사 시야 내에 있으면 -> 정지
        continue 
      dist = abs(mi-ci) +abs(mj-cj) # 현재 거리
      for di,dj in dirs : 
        ni,nj = ci +di ,cj +dj # w 의 다음 이동 공간
        #범위내 메듀사 시야 아니고, 현재 거리보다 더 줄어드는 방향 (상하좌우 우선순위로 이동)
        if 0<=ni<N and 0<=nj<N and v[ni][nj]!=1 and  dist>abs(mi-ni)+abs(mj-nj):
          if (ni,nj) == (mi,mj): # 공격 -> 죽음
            attk+=1 
            men.pop(idx) 
          else :  
            men[idx] = [ni,nj]
          move += 1
          break
  return move, attk

###############
# main FLOW
###############

    
# 0. 입력 
# 마을 크기 M , 전산수 N / 메듀사 위치정보s ,  공원 위치 정보 e /  M명 전사 좌표 N/ 개의 도로 정보 
N , M = map(int, input().split())
si , sj , ei , ej = map(int , input().split())
tlist = list(map(int , input().split()))

# 전사 좌표 
men = []
for i in range(0, M*2 , 2) :
  men.append([tlist[i], tlist[i+1]])
# 필드 정보
arr =[list(map(int, input().split())) for _ in range(N)]



# [0] BFS 로 메듀사 최단경로  : 도로 따라 공원까지 - 상하좌우

route = find_route(si,sj,ei,ej)



if route == -1 : # 길이 없는 경우
  print(-1)
else : 
  for mi,mj in route :  # 각 time = idx 별 메듀사 위치 
    move_cnt , attk_cnt = 0, 0
    # [1]메듀사의 이동 : 지정된 최단거리로 한칸 이동 (전사와 만날 경우 , 전사 삭제)
    
    for i in range(len(men)-1,-1,-1) : # 역순 탐색
      if men[i] == [mi,mj] :
        men.pop(i)

    #[2] 메듀사 시선 : 상하좌우 방향중 "가장 많이 stone 되는 방향" 선택
    # v[] : 메듀사의 시선 명시해서 이동시 참조(메듀사시선 =1 , 전사에게 가려진 곳 ==2 ,빈땅 ==0)
    # mar[][] : 지도에 있는 현재 전사 수 (및 위치) 표시(중복 존재 가능)
    marr = [[0]*N for _ in range(N)]
    for ti, tj in men : 
      marr[ti][tj] += 1
    

    max_stone = -1 # 4 방위 중 max stoning 가능한 개수
    v= [] #현 필드내 메듀사 시선으로 생기는 영억 속성 설정

    # 4방위 바교 
    for dr in (0,4,6,2) : # 상하좌우 순서대로 처리 
      tv , tstone = make_stone(marr , mi , mj, dr) 
      # 최대값 갱신 - max_stone 개수 & 시선 영역 속성 설정
      if max_stone < tstone : 
        max_stone = tstone
        v = tv

    


    #[3] 전사의 이동 (한 칸씩 두번) : 메듀사 있는 경우 공격
    # 메듀사와 가까워지는 방향으로 접근
    move_cnt , attk_cnt = move_men(v,mi,mj)
  
    print(move_cnt, max_stone , attk_cnt)
  print(0)