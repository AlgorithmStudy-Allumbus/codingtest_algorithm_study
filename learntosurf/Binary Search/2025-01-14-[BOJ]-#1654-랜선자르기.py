import sys 
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

start = 1 
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0 # 랜선의 개수 
    for i in lan:
        lines += i // mid
    if lines >= N: # 랜선의 개수가 많음 (랜선의 길이가 짧음)
        start = mid + 1
    else: # 랜선의 개수가 적음 (랜선의 길이가 김)
        end = mid - 1

print(end)