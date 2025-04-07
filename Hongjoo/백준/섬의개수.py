"""
https://www.acmicpc.net/problem/4963
# 유형 : 그래프 탐색 (DFS/BFS)
- goal) 지도 속 섬 군집 개수 구하기
- 각 섬은 가로,세로,대각선 연결 가능
- 땅은 1, 바다는 0
- 지도 밖은 바다 0 
- 입력은 다중 테스트 케이스 -> grid [W,h] => 출력 : 각 테스트 케이스별로 섬의 개수 출력
#flow 
1) 지도 2배열 입력 받기
2) 방문 등록 여부 확인 =  섬 군집 개수 반환 by dfs 
 1 = 방문 x 땅, -1 방문한 땅 , 0 바다
2-1) dfs
"""
# 1. 각 테스트 케이스 분리
# 입력 0,0 전까지 계속 입력 받기
import sys
from collections import deque
input = sys.stdin.readline
# 상하좌우 + 대각선 4개  = 8방위 이동 
dy = [-1, 1, 0,0 , -1,-1,1,1]
dx = [0,0,-1,1 , -1,1,-1,1]


while True : 
    W,H = map(int, input().split())
    # 입력 종료 조건
    if W == 0 and H == 0 : 
        break
    # 지도 입력 받기 
    field = [ [0 for _ in range(W)] for k in range(H)]
    for i in range(H) :
        field[i] =list(map(int, input().split()))
    # 군집 탐색
    def bfs (s_y,s_x):
        q = deque()
        q.append([s_y,s_x])
        field[s_y][s_x] = -1 # -1 방문 등록 
        while q : 
            c_y, c_x = q.popleft()
            for i in range(8):
                n_y , n_x = c_y + dy[i] , c_x + dx[i]
                # 지도 내부 범위 확인 
                if 0<= n_y < H and 0<= n_x < W : 
                    # 방문 등록 안한 곳 + 바다 아닌 섬임
                    
                    if field[n_y][n_x] > 0 : 
                        q.append([n_y , n_x])
                        field[n_y][n_x] = -1

    cnt = 0
    for i in range(H):
        for j in range(W):
            if field[i][j] > 0 : 
                bfs(i, j)
                # print(f"@{cnt}")
                # print(f"{field}")
                cnt+=1
    
    print(f"{cnt}")
            


        



