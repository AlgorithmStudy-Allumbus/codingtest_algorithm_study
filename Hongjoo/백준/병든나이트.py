"""
실버3
https://www.acmicpc.net/problem/1783

#문제 : 그래프탐색(DFS , BFS)
- NxM 의 왼쪽 아래 칸 시작 
- 4가지 방법으로 이동 
    (1) 2칸 위 , 1칸 오른쪽 
    (2) 1칸 위로 2칸 오른쪽
    (3) 1칸 아래로 , 2칸 오른쪽
    (4) 2칸 아래 , 1칸 오느ㅜㄹ쪽
- goal)  방문할 수 있는  "최대 칸 개수"  구하기 

# 조건 
- <이동횟수가 4번 이상 -> 이동 방법 모두 사용 
- < 4번 이하 - 제약 없음 


"""
n, m = map(int, input().split())

result = 0
# n이 1일 때 무조건 1
if n == 1:
  result = 1
# n이 2일 때
elif n == 2: 
  if m >= 1 and m <= 6: #m이 1~6일 때
    result = (m + 1) // 2 
  elif m >= 7: #7이상일 때
    result = 4
# n이 3 이상일 때
elif n >= 3: 
  if m <= 6: #m이 1~6일 때
    result = min(m, 4)
  elif m >= 7: #m이 7 이상일 때
    result = m - 2
print(result)
