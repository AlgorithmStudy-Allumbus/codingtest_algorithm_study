"""
백준 # 15652.N과 M(4)
https://www.acmicpc.net/problem/15652

[문제] 
- 자연수 1~ N 중 M 개 고른 수열 => 재귀함수
- 같은 수 중복 사용 , 중복되는 수열은 다중 출력 불가능 
- 고른 수열은 오름차순
- 출력은 오름차순 => - 원소가 1~ N임으로 이미 오름차순으로 정렬되어 있음(고려x)
[flow]
1. check 를 mxn 의 행렬로 사용 여부 확인(중복 사용과 중복 수열 방지를 위해)
2. 재귀함수로 조건에 해당하는 함수 출력
    - 매개변수 m = result 에 들어간 원소들 개수 = 현재 들어갈 자리수
    (1)  m == M ,즉 result안에 M 개 들어가 있으면, 출력
    (2) m번째 자리에 n이 들어간 경험이 있는지 확인 - check[m][n-1] == 0 
        -> 사용 가능
        조건 2 : 첫 result 원소면 바로 등록
        조건 3 : 아니면 , 이전 자리수에 등록된 result 원소 값보다 커야지 등록 
        - 등록시(result[m] = n) ,  check에도 사용 중 등록하기( check[m][n-1] = 1)
    (3)m+1 인 재귀 함수 수행
    (4) m 번째 자리수에서 들어갈 1~N수 탐색 완료하면
        -> check[m] 은 모두 0으로 리셋하고, m-1 자리수로 backtracking
 
"""

import sys
N, M = map(int, sys.stdin.readline().split())
# 1. 변수 정의
result = [0 for _ in range(M)]
check= [[0 for _ in range(N)] for  i in range(M) ] # row : m번째 위치 , column  : N개 후보군 원소들의 m번째 자리수에 사용 여부


def perm(m) :
    if m == M : 
        print(*result)
    else : # m : 0,1,2 ...M-1
        for n in range(1, N+1) : 
            # print(f"before m : {m} /n {n} -> check {check[m]}")
            if check[m][n-1] == 0 : # 빈 자리 
                if (m == 0) or (m < M and n >= result[m-1]) :  # 첫번쨰 자리 등록 심사 -> pass
                    result[m] = n  # 사용 중     # 그외의 자리 등록 심사 -> 이전 자리수 <= 현재 자리수 조건 만족(중복 출력 방지)
                    check[m][n-1] = 1
                    # print(f"m : {m} /n {n} -> check {check[m]}")
                    # print(f"result { result}")
                    perm(m+1)

        # m 번째 자리에서 들어갈 1~N수 탐색 완료
        # 그러면 check[m] 은 0으로 리셋
        check[m] = [0 for j in range(N)]

perm(0)
                
                