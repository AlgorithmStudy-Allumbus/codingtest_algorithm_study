import sys
sys.setrecursionlimit(10000) #재귀 limit 설정(파이썬 최대 깊이 늘리는 모듈 이용)

input = sys.stdin.readline
# dfs 함수 정의
def dfs(x, y):
    # x와 y의 위치가 벗어나거나, 양배추리스트에 없는 위치라면 그냥 반환
    if x < 0 or x >= M or y < 0 or y >= N  or cabbage_filed[x][y] == 0:
        return
    
    # 현재 위치 방문 처리 
    cabbage_filed[x][y] = 0 # 배추 있던 자리 1->0으로 변경해서 중복 방지

    # 상하좌우 위치 탐색
    dfs(x+1, y) # 오른쪽 배추 탐색
    dfs(x-1, y) # 왼쪽 배추 탐색
    dfs(x, y+1) # 위쪽 배추 탐색
    dfs(x, y-1) # 아래쪽 배추 탐색


T = int(input()) # 테스트케이스 수
for _ in range(T):
    M, N, K = map(int, input().strip().split()) # M: 가로길이, N: 세로길이, K: 배추개수
    cabbage_filed = [[0] * N for _ in range(M)] # 양배추밭 리스트 초기화
    
    for _ in range(K):
        x, y = map(int, input().strip().split())
        cabbage_filed[x][y] = 1 # 입력받은 x, y 위치에 배추가 있으므로 1로 변경
    
    worms = 0 # 지렁이 필요 수 초기화
    for i in range(M):
        for j in range(N):
            if cabbage_filed[i][j] == 1: # 배추가 심어져 있고 아직 방문하지 않은 경우
                worms += 1 # 지렁이 수 +1
                dfs(i, j)# dfs 호출하여 모든 연결된 배추 방문 처리
                

    print(worms) # 현재 테스트케이스에 대한 지렁이 수 출력