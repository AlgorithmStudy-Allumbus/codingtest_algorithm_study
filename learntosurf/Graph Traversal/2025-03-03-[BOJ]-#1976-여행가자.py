import sys 
input = sys.stdin.readline

N = int(input().strip()) # 도시의 수 
M = int(input().strip()) # 여행 계획에 속한 도시의 수

# 유니온 파인드 부모 배열
parent = [i for i in range(N)]  

# find 연산: 경로 압축을 이용하여 루트 노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# union 연산: 두 집합을 합치기
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x  # y의 루트를 x로 연결

# 도시 연결 정보 처리
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:  # 두 도시가 연결된 경우
            union(i, j)

# 여행 계획 입력
plan = list(map(int, input().split()))

# 여행 경로가 같은 집합인지 확인
root = find(plan[0] - 1)  # 첫 번째 도시의 루트
for city in plan[1:]:
    if find(city - 1) != root:
        print("NO")
        exit()

print("YES")