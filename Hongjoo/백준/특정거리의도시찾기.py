"""
4 4 2 1  # 도시 개수 n , 도로 개수 m , 거리 정보 k , 출발 도시 번호 x 
1 2
1 3
2 3
2 4 # 2~m 번 a -> b
다익스트라
"""
import heapq
#0 input
INF = 20000
city_count , road_count , target_km , start =map(int,input().split())

#1. graph 그리기 -> 인접 리스트 방식 , 최단거리 테이블
graph = [[] for i in range(city_count+1) ]
distance = [INF]* (city_count+1)

for _ in range(road_count):
    a,b = map(int, input().split()) 
   # a -> b ,b 는 a 에서 갈수 있는 인접한 city  
    for j in range(len(graph)):
        if  a == j:
            graph[a].append((b,1))


# 다익스트라
#1. 초기 노드 설정  #2. 최단거리 테이블 최기화
q =[]
distance[start]=0
heapq.heappush(q, (0,start))
# 2. 최단 거리(heappop) & 방문 x  노드 선택
while q : 
    dist , now = heapq.heappop(q)
    if distance[now] < dist :
        continue
    #4, Cost(A->X) + Cost(X->B) < Cost(A->B) : 업데이트 & push
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]] :
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
           
islenK = False
for i in range(1, city_count+1):
    if distance[i] == target_km :
        islenK = True
        print(i)
if not islenK :
    print(-1)