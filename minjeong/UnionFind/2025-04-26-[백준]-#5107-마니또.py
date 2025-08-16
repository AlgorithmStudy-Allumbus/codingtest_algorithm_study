import sys

input = sys.stdin.readline


# Find 연산(같은 집합에 속하는지 확인하기 위한 함수)
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])  # 경로 압축
    return parent[a]


# Union 연산(두 집합을 합치기 위한 함수)
def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a > p_b:  # 값이 더 작은 쪽을 부모로 설정
        parent[p_a] = p_b
    else:
        parent[p_b] = p_a


tc_num = 0  # 테스트케이스 개수
while True:
    N = int(input())
    parent = [i for i in range(N + 1)]  # 초기: 각 원소가 자기 자신을 부모로 가짐
    manito = {}
    tc_num += 1  # 테스트케이스 업데이트

    if N == 0:  # 입력 종료
        break

    for _ in range(N):
        from_p, to_p = input().split()
        # manito에 번호 부여
        if from_p not in manito:
            manito[from_p] = len(manito) + 1
        if to_p not in manito:
            manito[to_p] = len(manito) + 1
        # 합집합 연산
        union(parent[manito[from_p]], parent[manito[to_p]])

    parent = set(parent)

    print(tc_num, len(parent) - 1)  # 0이 포함되어 있으므로 1 빼주어야 함
