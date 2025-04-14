"""
https://www.acmicpc.net/problem/2437

# 문제
- 저울 N개의 조합의 합으로 구현할 수 없는 양의 최소값 구하기
- N<=1000개
- 1개 무게 >= 1,000,0000
유형 : 그리디 , 정렬

"""
#1. 입력 저울추 & 오름차순 정렬
N = int(input())
weights = sorted(list(map(int, input().split())))
target = 1 
for w in weights : 
  if target < w :
    break
  
  target += w
print(target)
