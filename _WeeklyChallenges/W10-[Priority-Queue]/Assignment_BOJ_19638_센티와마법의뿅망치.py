'''
BOJ #19638. 센티와 마법의 뿅망치 (실버1)
https://www.acmicpc.net/problem/19638
유형: Priority Queue, Data Structure
'''

'''
풀이1
'''
import sys
import heapq

input = sys.stdin.readline

# 입력
N, H, T = map(int, input().split())  # N: 거인의 나라 인구 수, H: 센티의 키, T: 뿅망치 횟수 제한
heights = []

for _ in range(N):
    heapq.heappush(heights, -int(input()))  # 최대힙을 위해 음수로 저장

cnt = 0  # 사용한 뿅망치 개수

# 뿅망치 사용
while cnt < T:
    tallest = -heapq.heappop(heights)  # 가장 큰 키를 가져옴

    if tallest < H:  # 센티보다 작은 거인이 나오면 즉시 종료
        print(f"YES\n{cnt}")
        break

    # 키가 1이면 더 줄일 수 없음
    if tallest == 1:
        heapq.heappush(heights, -1)
    else:
        heapq.heappush(heights, -(tallest // 2))

    cnt += 1
else:
    # 뿅망치 사용을 모두 소진한 경우
    tallest_after = -heapq.heappop(heights)  # 남아 있는 가장 큰 키
    if tallest_after < H:
        print(f"YES\n{cnt}")
    else:
        print(f"NO\n{tallest_after}")

'''
풀이2 (최적화된 풀이로, heapreplace()를 사용하여 heappop()과 heappush()를 한 번의 연산으로 처리함)
출처: https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-19638-%EC%84%BC%ED%8B%B0%EC%99%80-%EB%A7%88%EB%B2%95%EC%9D%98-%EB%BF%85%EB%A7%9D%EC%B9%98-Heapq
'''
import sys, heapq
input = sys.stdin.readline

n, h, t = map(int, input().split())
giants = [-int(input()) for _ in range(n)]
heapq.heapify(giants)
cnt = 0

for i in range(t):
    if -giants[0] == 1 or -giants[0] < h:
        break
    else:
        heapq.heapreplace(giants, -(-giants[0] // 2))
        cnt += 1

if -giants[0] >= h:
    print('NO', -giants[0], sep='\n')
else:
    print('YES', cnt, sep='\n')
