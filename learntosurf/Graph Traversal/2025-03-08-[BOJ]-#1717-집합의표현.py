import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)  # 트리 깊이 관리
result = []

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:  # 더 랭크가 높은 루트로 합침
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1  # 같은 랭크면 한쪽의 랭크 증가


for _ in range(m):
    op, a, b = map(int, input().split())
    
    if op == 0:  # 합집합 연산
        union(a, b)
    
    elif op == 1:  # 같은 집합 여부 확인
        if find(a) == find(b):
            result.append("YES")
        else:
            result.append("NO")

sys.stdout.write("\n".join(result) + "\n")
