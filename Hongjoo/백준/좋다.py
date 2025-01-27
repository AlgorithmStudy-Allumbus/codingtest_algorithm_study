
"""
https://www.acmicpc.net/problem/1253
[조건]
- 배열 내 다른 원소들의 합으로 나타낼 수 있음
- 유형 : two pointer 
-> Answer = a+b 
    - 정렬
    - a, b < Answer  => 음수일 경우에는 아님
    - left_point , right_point
예외
1. 중복 원소 존재할 경우 
6
1 3 2 1 4 4
- 2,3, 4, 4
2. 1개
1
3
-> 0
3. A = 0 일떄
3
0 0 0

2
0 0 
4. 
3
1 1 1

6
1 1 2 2 3 6
-> 2,2,3

# 음수요 ?
4
-1 1 2 3 
2
# 유형 : 이분분할 , two pointer , 
# 알아야 하는 사실 
# 이분 탐색은 target에 대해 작을때 , 클때 , 같을떄 처리 과정을 다르게 둬야 함

"""

import sys

n = int(sys.stdin.readline())
# 조합 재료들 배열로 입력 받기 & 오름 차순 정렬
board = sorted(list(map(int,sys.stdin.readline().split())))
good = 0 # 좋은 수 개수
#1. two pointer - 양쪽 끝에서 시작 
for i in range(n) :
    target  = board[i]
    left = 0 ; right = n-1
    while left<right : # 서로 다른 수를 가르킨다
        if target == (board[left] +board[right]) : 
            # left 와 right 가 각각 target을 가르킬때 -> 각자 진행 방향으로 이동 
            if left == i  :
                left += 1 
            elif right == i :
                right -= 1
            else : 
                good += 1
                break
        elif target < (board[left] +board[right]) : # target이 합보다 작을떄
            right -=1 
        else : # target이 합보다 클때
            left += 1
print(good)