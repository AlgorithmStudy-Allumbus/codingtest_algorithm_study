import sys
answer =0 
N, M = map(int, sys.stdin.readline().split())
board =[[] for _ in range(N)]
# E와 M의 누적합 행렬 정의
e_sum = [[0]*M for _ in range(N)]
m_sum = [[0]*M for _ in range(N)]

for i in range(N):
    board[i] = list(sys.stdin.readline()[:-1])
    for j in range(M):
        if board[i][j] == "E" :
            e_sum[i][j] = 1
        elif board[i][j] == "M" : 
           m_sum[i][j] = 1

# 2.E와 M 행렬 누적합 계산하기
# dp[i][j]  = dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1 + value[i][j]
for i in range(N):
   for j in range(M):
      # E의 누적합 계산
        # i=0 or j=0 일때 누적합 점화식
        if i==0 and j== 0 : 
            e_sum[0][0] = e_sum[0][0]
        elif i== 0 : # 가로형 누적합 계산식 : 
            e_sum[i][j] = e_sum[0][j-1]+e_sum[0][j]
        elif j == 0: # 세로형 누적합 계산식
            e_sum[i][j] = e_sum[i][0] + e_sum[i-1][0]
        else : # 일반적인 누적합 계산식
            e_sum[i][j] = e_sum[i-1][j] + e_sum[i][j-1] - e_sum[i-1][j-1] + e_sum[i][j]

#M의 누적합 계산 : E의 누적합의 역방향(아래로 뒤집기) 
# 기준(i,j) : 왼쪽 위쪽 칸    
for i in range(N-1, -1 , -1):
    for j in range(M-1 , -1 ,-1) :
    # i=0 or j=0 일때 누적합 점화식
        if i== N-1 and j== M-1 : # 맨 오른쪽 아래 칸의 누적합
            m_sum[i][j] = m_sum[i][j]
        elif i== N-1 : # 가로형 누적합 계산식 : 
            m_sum[i][j] = m_sum[i][j+1]+m_sum[i][j]
        elif j == M-1 : # 세로형 누적합 계산식
            m_sum[i][j] = m_sum[i][j] + m_sum[i+1][j]
        else : # 일반적인 누적합 계산식
            m_sum[i][j] = m_sum[i+1][j] + m_sum[i][j+1] - m_sum[i+1][j+1] + m_sum[i][j]

#3. S 을 기준으로 총 경우의 수 구하기
# 경우의 수 = E*M
answer = 0 
for y in range(N):
    for x in range(M):
        # S 의 위치 파악하기
        if board[y][x] == "S" :
            # (y,x) 인 S의 기준에서 E*M 으로 경우의 수 구하기 
            answer += e_sum[y][x]*m_sum[y][x]


#4. 나머지로 출력하기
print(answer%(10**9+7))