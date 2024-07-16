"""
시작 = 1 
if 시작 ~ # 노드(N개) 까지의 최단 거리 <= K : 배달 가능True 
다익스트라 
"""
import heapq
INF = 2001

def dikstra(graph, distance, start) :
    #2. distance 초기화 : (0,start)로 초기화 / q에 (0,start 넣기)
    q= []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    #3. q에서 최단 거리(start -> X)  & 방문x 노드 선택  
    while q :
        dist , now = heapq.heappop(q) # A->X
        if distance[now] < dist: # 방문 완료
            continue
        #4. Cost(X->B)계산 + Cost(A->X) < Cost(A->B) => distance 업데이트 + q에 넣기
        #  graph 인접 간선(i[1]) , dist, 현distance[B]
        for i in graph[now]: # i = (b,c)....
            cost = dist + i[1] 
            if cost < distance[i[0]] :
                distance[i[0]] = cost 
                heapq.heappush(q,(cost,i[0]))
    return distance

def solution(N, road, K):
    # input 
    graph = [[] for _ in range(N+1)] 
    distance = [INF]*(N+1) # 최단거리 그래프
    
    #0 그래프 필드 정의 a : [(b,c)...]  #양방향
    road.sort()    
    for r in road : 
        a=r[0] ; b = r[1] ; c= r[2]
        graph[a].append([b,c])
        graph[b].append([a,c])

    # 다익스트라
    distance = dikstra(graph ,distance, 1)
  
    # 거리 < K 인 마을 개수
    count = 0
    for city in range(1, N+1) :
        if distance[city] <= K : 
            count+=1
    return count
        