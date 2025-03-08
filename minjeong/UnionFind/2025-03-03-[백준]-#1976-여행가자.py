import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def union(a, b):
   p_a = find(a)
   p_b = find(b)

   if p_a > p_b:  # a의 대표보다 b의 대표가 더 작은 값을 가지면,
       parent[p_a] = p_b  # a가 속한 집합을 b의 집합에 합치기
   else:
       parent[p_b] = p_a  # 그렇지 않으면 b의 집합을 a의 집합에 합치기

def find(a):
   if a == parent[a]:  # a가 자기 자신의 부모이면 대표 노드
       return a

   parent[a] = find(parent[a])  # 경로 압축을 통해 a의 부모를 대표 노드로 재설정
   return parent[a]

# 도시의 개수 n과 여행 계획에 포함된 도시의 수 m을 입력받기
n = int(input())
m = int(input())

parent = [i for i in range(n)]  # 각 도시는 처음에 자기 자신이 대표 노드.

# n개의 줄에 걸쳐 도시 간 연결 정보를 입력받고, 연결되어 있으면 union 연산 수행
for i in range(n):
   arr = list(map(int, input().split()))
   for j in range(n):
       if arr[j]:  # 1이면 i와 j가 연결되어 있으므로 union 연산 수행
           union(i, j)

# 여행 계획을 입력
plan = list(map(int, input().split()))
result = "YES"
# 여행 계획에 있는 모든 도시가 같은 집합(대표 노드)을 가지는지 확인
for i in range(1, m):
   if parent[plan[i]-1] != parent[plan[0]-1]:
       result = "NO"
       break

print(result)