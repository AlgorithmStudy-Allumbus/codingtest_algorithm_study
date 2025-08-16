import sys 
input = sys.stdin.readline

#1. 입력 변수 + 오름차순 정렬
N , C  = map(int, input().split())
arr =sorted([int(input()) for _ in range(N)])

#2. “최소 거리 dist”의 탐색 범위 초기화 # 이진 탐색
start = 1 ; end = arr[-1] - arr[0] 
answer = 0  # 최소 거리 중 최대 거리 

#3.최소 인접 거리 dist 최대값 찾기
#설치 공유기는 dist이상의 간격으로 설치
while start <= end : 
  mid = (start+end)//2
  cnt = 1 # arr[0]은 설치 시작점
  
  #[1] 최소 인접 거리가 mid 이상으로 "최대 설치 가능 공유기 개수계산"
  prev = arr[0] # 이전에 설치한 공유기 위치
  for i in range(1,N) :
    if arr[i] - prev >= mid : # 공유기 등록
      prev = arr[i]
      cnt+=1 
    # 공유기 등록하기엔 dist부족한 경우 -> 다음 arr로 이동 

  #[2] 최소거리 dist 이분 탐색
  # 조건 : 설치한 공유기 개수 Cnt 가 C 이상
  # True 경우 ,  최소거리 Answer 업데이트, 탐색 범위 (mid+1 : end) 이동
  if cnt >= C :
    answer = max(answer ,mid)
    start = mid+1
  # False 경우: 탐색 범위 Lower bound로 이동(start : mid)
  else : 
    end = mid - 1

print(answer)