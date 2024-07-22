INF = int(1e9) #무한을 나타내는 갑스올  10억 설정

# 노드 개수 & 간선의 개수 입력
n = int(input())
m = int(input())
#1. graph 설정 -인접 행렬(2차원 , nxn ) , 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#1-1. 자기 자신에서 자기 자신 가는 비용 {Cost (A->A)}= 0 초기화
for a in range(1,n+1) :
    for b in range(1,n+1):
        if a==b:
            graph[a][a] = 0

#1-2 .각 간선에 대한 정보를 입력 받아, 그 값으로 초기화 :   Cost(A->B) = 초기값
for _ in range(m):
    # Cost(A->B) = c
    a,b,c = map(int, input().split())
    graph[a][b]= c

#2. 플로이드 워샬 점화식 수행
# a->b : a->k->b vs a->b
for k in range(1,n+1):   
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

# 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF :
            print("INF", end="")
        else :
            print(graph[a][b], end ="")
print()