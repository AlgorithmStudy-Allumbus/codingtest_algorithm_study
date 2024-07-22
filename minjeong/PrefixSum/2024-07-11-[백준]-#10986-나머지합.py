import sys
sys.setrecursionlimit(10**6) # 최대 재귀한도 깊이
input = sys.stdin.readline

# 초기화
n, m = map(int, input().strip().split()) # n: 수의 개수, m: 조건으로 주어진 합
arr = list(map(int, input().strip().split())) # 수열

prefix_sums = [0] * n
prefix_sums[0] = arr[0]

# 누적합 계산
for i in range(1, n):
    prefix_sums[i] = prefix_sums[i-1] + arr[i]

# 나머지 값 빈도수를 저장할 해시맵
mod_count = {}
mod_count[0] = 1 # 처음부터 M으로 나누어 떨어지는 경우를 위해 초기화
count = 0

# 누적합 배열 순회ㅣ
for p in prefix_sums:
    mod = p % m
    if mod in mod_count: # 동일한 나머지값이 있는 경우
        count += mod_count[mod] # 해당 나머지 갑싀 빈도수만큼 count에 더해줌
        mod_count[mod] += 1 # 해당 나머지 값의 빈도수 +1
    else:
        mod_count[mod] = 1 # 새로운 나머지 값 추가
        
print(count)