S = int(input())
n = 0  # 자연수 개수
total = 0  # 누적 합

# 1부터 차례대로 더하기
while total <= S:
    n += 1
    total += n

# 마지막으로 더한 값이 S를 초과했으므로 n-1이 정답
print(n - 1)
