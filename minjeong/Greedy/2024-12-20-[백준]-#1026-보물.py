import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())  # 배열 길이
A = list(map(int, input().split()))  # 배열 A
B = list(map(int, input().split()))  # 배열 B

# A 오름차순 정렬, B 내림차순 정렬
A.sort()
B.sort(reverse=True)

# 최소값 계산
answer = 0
for i in range(N):
    answer += A[i] * B[i]

# 결과 출력
print(answer)