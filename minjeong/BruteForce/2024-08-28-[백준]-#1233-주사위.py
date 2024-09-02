import sys
input = sys.stdin.readline

S1, S2, S3 = map(int, input().split())

# 가능한 합의 빈도를 저장할 딕셔너리
sum_counts = {}

for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            temp_sum = i + j + k
            if temp_sum in sum_counts:
                sum_counts[temp_sum] += 1
            else:
                sum_counts[temp_sum] = 1

# 가장 높은 빈도와 그 합을 찾는다.
max_freq = max(sum_counts.values())
# 답이 여러개라면 가장 합이 적은 것을 출력한다.
answer = []
for key, value in sum_counts.items():
    if value == max_freq:
        answer.append(key)
print(min(answer))

'''
S1, S2, S3 = map(int, input().split())
arr = [0 for i in range(S1+S2+S3+1)]
for i in range(S1):
    for j in range(S2):
        for k in range(S3):
            arr[i+j+k+3]+=1
max = max(arr)
for i in range(len(arr)):
    if arr[i] == max:
        print(i)
        break
'''