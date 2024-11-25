n = int(input())

# 승패를 기록할 배열
win = [-1] * (n + 1)

# 초기 값 설정
win[1] = 1  # SK
win[2] = 0  # CY
win[3] = 1  # SK

# 점화식으로 승패 계산
for i in range(4, n + 1):
    if win[i-1] == 1 or win[i-3] == 1:
        win[i] = 0  # CY가 승리
    else:
        win[i] = 1  # SK가 승리

# 결과 출력
if win[n] == 1:
    print("SK")
else:
    print("CY")
