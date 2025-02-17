import sys
input = sys.stdin.readline
import heapq

N, Hcenti, T = map(int, input().split())
giants = [-int(input().strip()) for _ in range(N)]  # 최대 힙을 위해 음수 변환

# 최대 힙 생성
heapq.heapify(giants)
used_hammer = 0  # 사용한 뿅망치 횟수

# 마법의 뿅망치를 사용
for _ in range(T):
    tallest = -heapq.heappop(giants)  # 가장 큰 거인 추출
    
    if tallest < Hcenti:  # 센티보다 작아졌다면 종료
        heapq.heappush(giants, -tallest)
        break

    if tallest == 1:  # 키가 1이면 줄일 수 없으므로 다시 넣고 종료
        heapq.heappush(giants, -tallest)
        break

    new_height = tallest // 2  # 키 줄이기
    heapq.heappush(giants, -new_height)  # 줄인 값 다시 삽입
    used_hammer += 1  # 사용 횟수 증가

# 가장 키가 큰 거인 확인 (힙이 비었으면 0)
tallest_remaining = -heapq.heappop(giants) if giants else 0

if tallest_remaining < Hcenti:
    print("YES")
    print(used_hammer)
else:
    print("NO")
    print(tallest_remaining)
