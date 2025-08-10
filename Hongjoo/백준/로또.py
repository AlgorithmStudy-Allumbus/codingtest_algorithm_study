"""
[BOJ]6603로또/실버2
https://www.acmicpc.net/problem/6603

-주어진 K개(k>6) 숫자에 6개 뽑아 대해 중복x 한 조합의 경우의 수 찾기
->중복 x , 순서 상관x
- 해당 모든 경우의 수는 사전 순으로 출력
- 입력 : K , {해당하는 숫자의 조합}
"""

import sys
input = sys.stdin.readline
# 1. 입력 변수 및 출력 형식에 맞춰 설정하기
while True :
  set_s = list(map(int, input().split()))
  answer = []
  if len(set_s) < 2 : 
    break 
  k= set_s.pop(0)
  #2. 유효성 검사 is_valid 정의
  # check = [True]*len(set_s[1:])
  result = [0]*6 # 출력 리스트
  #3. 백트래킹 함수 정의
  def conbination(level ,idx ): 
    #종료 조건
    if level == 6 : 
      answer.append(result.copy())
      # print(result)
      return 
    # 동작 과정
    for i in range(idx,k):
      result[level] = set_s[i]
      conbination(level+1 ,i+1) # 조합은 idx 보다 작은 i는 탐색 할 필요 없음
      result[level] = 0 
  conbination(0,0)
  # print(answer)
  # 3. 출력 형식 맞추기
  for a in answer: 
    print(" ".join(map(str,a)))
  print("")