"""



"""

def myprint_3d(arr3) :
    for arr in arr3:
        for lst in arr: 
            print(*lst)
        print()
    print()

def myprint_2d(arr):
    for lst in arr:
        print(*lst)
    print()

# sk_3d ,si_3d, sj_3d = find_3d_start() 
def find_3d_start(): # 3d 출발 지점 좌표
    for i in range(M) :
        for j in range(M) :
            if arr3[4][i][j]==2 : 
                return 4, i, j
            
def find_2d_end(): # 2d에서 최종 도착 지점
    for i in range(N):
        for j in range(N) :
            if arr[i][j] == 4 : 
                arr[i][j] = 0 
                return i , j

def find_3d_base(): #  전체 맵에서 3d 영역 시작(절대)좌표  - 좌측 상단
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] ==3 :
                return i, j 

# 3d 차원 & 2d 시작 위치 (텔레포트) 좌표 반환
# 3d : 상대 좌표 -> 2d 전체 맵 절대 좌표
def find_3d_end_2d_start():
    #[1] 3차원 시작 좌표(base) 찾기 =3 등장 -> 좌측상단 
    bi , bj  = find_3d_base()

    #[2] 3차원 좌표에서 2d 차원 연결 좌표 찾기 (1차 목적지 in 3d )
    # i,j : 2d 전체 맵 기준 
    # si ,sj = 2d통로 = 3d 통로 : (ek,ei,ej)
    for i in range(bi , bi+M) :
        for j in range(bj, bj+M) :
            if arr[i][j]!=3 : # 3차원 위치 아니면  skip
                continue
            
            # 1차 출구 : 3d 차원에서 ->2d 로 텔레포트 하는 위치
            if arr[i][j+1] == 0 : # 우측에 3d - 2d 탈출구 (3차원 우측으로 1차 출구)
                return 0 , M-1 , (M-1)-(i-bi) , i, j+1  # ek(평면) = 0 동쪽 , ei = M-1 , ej = i , si = i , sj = j+1
            elif arr[i][j-1] ==0 : # 좌측 1차 출구
                 return 1, M-1, i-bi, i, j-1    # ek(평면)=1, ei=M-1, ej=i, si=i, sj=j+1
            elif arr[i+1][j]==0 : # 아래쪽 1차 출구
                return 2, M-1 , j-bj,  i+1 ,j # ek(평면)=2, ei=M-1, ej=i, si=i, sj=j+1
            elif arr[i-1][j] == 0 : # 위쪽에 1차 출구
                return 3 ,M-1 , (M-1)-(j-bj) , i-1 , j # ek(평면)=3, ei=M-1, ej=i, si=i, sj=j+1
    #여기까지 올릴 없지만 
    return -1 
            
from collections import deque 
# dist = bfs_3d(sk_3d ,si_3d, sj_3d ,ek_3d , ei_3d,ej_3d)

left_nxt = {0:2, 2:1, 1:3, 3:0}
right_nxt = {0:3, 2:0, 1:2, 3:1}

def bfs_3d(sk ,si, sj ,ek , ei,ej):
    q = deque()
    v = [[[0]*M for _ in range(M)] for k in range(5) ] # 방문 여부 + 최소 거리 

    q.append((sk , si, sj))
    v[sk][si][sj] = 1 

    while q : 
        ck ,ci , cj = q.popleft()
        
        # 목적지 도달
        if (ck,ci,cj) == (ek,ei, ej) : 
            return v[ck][ci][cj]


        # 4방향, 범위내/ 범위 밖 -> 다른 k 로 이동 처리 , 미방문
        for di,dj in ((-1,0) ,(1,0), (0,-1), (0,1)):
            ni , nj = ci+di , cj + dj
            # 범위 밖으로 이동- > 다른 k 평면으로 이동 
            if ni<0 : #(1) 위쪽 범위 밖 이탈
                if ck == 0 : nk , ni , nj = 4 , (M-1)-cj , M-1
                elif ck == 1 :  nk,ni , nj = 4 , cj , 0
                elif ck == 2 : nk , ni, nj = 4, M-1 , cj
                elif ck == 3 :  nk , ni ,nj = 4,0,(M-1)-cj
                elif ck == 4 : nk, ni, nj  = 3 , 0 ,(M-1)-cj
            elif ni >= M : #(2) 아래쪽으로 범위 이탈
                if ck == 4 : nk, ni, nj  = 2, 0, cj
                else :  continue
            elif nj < 0 : # (3) 왼쪽 범위 이탈
                if ck ==4 : nk , ni , nj = 1, 0 , ci
                else : 
                    nk, ni, nj  = left_nxt[ck], ci , M-1
            elif nj >= M : # (4) 오른쪽 범위 이탈
                if ck == 4 :  nk, ni, nj  = 0 , 0, (M-1)-ci
                else : 
                    nk, ni, nj  = right_nxt[ck] , ci, 0
            else : # (5) 범위 내
                nk = ck 
            # 미방문 , 조건 맞으면 
            if v[nk][ni][nj] == 0 and arr3[nk][ni][nj] == 0 : 
                q.append((nk,ni,nj))
                v[nk][ni][nj] = v[ck][ci][cj]+1
    # 여긴 경로 없음 
    return -1 
# dist = bfs_2d(v , dist ,si,sj, ei , ej )
def bfs_2d(v , dist ,si,sj, ei , ej ):
    q= deque()
    
    q.append((si,sj))
    v[si][sj] = dist 

    while q : 
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):
            return v[ci][cj]
        # 네방향, 범위내, (미방문)/조건맞으면(길이고, v[ci][cj]+1<v[ni][nj]  - 최단 거리)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0 and v[ci][cj]+1<v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1

    return -1 
##########
########
#1. 입력변수  - 공간 한변의 길이N , 시간의 벽 한 변의 길이M, 시간 이상 현상 개수 F 공백
N,M,F = map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(N)]
arr3 = [ [list(map(int, input().split())) for _ in range(M)] for k in range(5) ]
wall = [ list(map(int, input().split())) for _ in range(F)] # 시간 이상 : 초기위치 (r,c) , 확산 방향 d,  확산 상수 v

# [1] 주요 위치 찾기 
# 3d 의 시작 , 3차원 끝(탈출) , 2차원 시작 , 2차원 끝 좌표 탐색 
sk_3d ,si_3d, sj_3d = find_3d_start() 
ei , ej = find_2d_end() # 3d 출구(1차 도착지점) 좌표
ek_3d , ei_3d,ej_3d , si,sj =find_3d_end_2d_start() # 3d 출구(1차 도착지점) 랑 2d 시작점 
# print(f"1111111111111111")
# print(sk_3d ,si_3d, sj_3d )
# print(ei , ej )
# print(ek_3d , ei_3d,ej_3d , si,sj)

#[2] 3차원 공간 탐색 : 시작 위치 -> 탈출 위치거리 탐색(BFS 최단거리)
dist = bfs_3d(sk_3d ,si_3d, sj_3d ,ek_3d , ei_3d,ej_3d)
# 동 서 남 북
di=[ 0, 0, 1,-1]
dj=[ 1,-1, 0, 0]
if dist !=  -1 : # 3d 탈출 불가능
    #[3] 2차원 탐색 준비 : 시간 이상 현상 처리해서 v 에 시간 표시 : BFS 확산시 v 배수보다 작으면 통과 표시
    # value: 이상 현상이 발생하는 time 
    v = [[401]*N for _ in range(N)]
    
    for wi, wj , wd ,wv in wall : # 이상 현상 초기 위치 , 확산 방향 , 확산 상수
        v[wi][wj]  = 1 
        for mul in range(1, N+1) :
            wi ,wj = wi+di[wd] , wj + dj[wd] # 다음 확산될 곳
            if 0<= wi <N and 0<=wj <N and arr[wi][wj] == 0 and (wi,wj)!=(ei,ej) : # wv 단위로 wd 방향으로 확산표시(출구가 아닌 경우)
                if v[wi][wj] > wv*mul : # 더 큰값일때만 갱신(겹칠 수 있음)
                    v[wi][wj] = wv*mul
            else : 
                break
    
    #[4] 2차원 시작 위치에서 BFS로 탈출구 탐색
    dist = bfs_2d(v , dist ,si,sj, ei , ej )
print(dist)