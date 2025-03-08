import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

# Union 연산(두 집합을 합치기 위한 함수)
def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a > p_b:  # 값이 더 작은 쪽을 부모로 설정
        parent[p_a] = p_b
    else:
        parent[p_b] = p_a

# Find 연산(같은 집합에 속하는지 확인하기 위한 함수)
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

# 연산 수행
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 초기: 각 원소가 자기 자신을 부모로 가짐

for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag == 0:  # 합집합 연산
        union(a, b)
    else:  # 같은 집합 확인 연산
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
