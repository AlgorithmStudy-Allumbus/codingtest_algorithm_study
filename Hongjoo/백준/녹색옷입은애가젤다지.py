"""
[BOJ]_4485 녹색 옷 입은 애가 젤다지?_Gold4
https://solved.ac/problems/tags/dijkstra?sort=solved&direction=desc&page=1
#유형 : Dijkstra
#제출날짜 : 01.27.2025

https://velog.io/@victoriapasta/BOJ-4485-%EB%85%B9%EC%83%89-%EC%98%B7-%EC%9E%85%EC%9D%80-%EC%95%A0%EA%B0%80-%EC%A0%A4%EB%8B%A4%EC%A7%80
"""
"""


"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
# 정답 출력을 위한 cnt 변수
cnt = 0
# n이 0이면 종료
while n != 0:
    cnt += 1
    # 입력
    board = [list(map(int, input().split())) for _ in range(n)]
    # 최소 비용으로 정렬해 줄 heap queue (이것을 기준으로 탐색)
    heap = []
    # 가중치를 저장해줄 distance 테이블
    dist = [[1e9] * n for _ in range(n)]
    # [0][0]부터 시작
    dist[0][0] = board[0][0]
    heapq.heappush(heap, (board[0][0], 0, 0))

    while heap:
        distance, y, x = heapq.heappop(heap)

		#최소 가중치를 먼저 가기 때문에 [N-1][N-1]에 도착하면 바로 리턴
        if y == n-1 and x == n-1:
            print("Problem", str(cnt)+":", distance)
            # n 변수 다시 받고 break
            n = int(input())
            break
		# 상하좌우 방향 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
			
            if 0 <= ny < n and 0 <= nx < n:
                cost = distance + board[ny][nx]
                # 이미 저장된 가중치보다 현재 가중치가 낮으면 업데이트
                if dist[ny][nx] > cost:
                    dist[ny][nx] = distance + board[ny][nx]
                    heapq.heappush(heap, (distance + board[ny][nx], ny, nx))