import sys
input = sys.stdin.readline

def find_number_of_paper(x_start, y_start, n):
    global white_cnt, blue_cnt
    check_sum = 0 # 색종이가 만들어지는지 여부를 확인하기 위한 변수
    for i in range(x_start, x_start + n):
        for j in range(y_start, y_start + n):
            check_sum += colored_paper[i][j]
    if check_sum == 0:       # 하얀 색종이라면
        white_cnt += 1
    elif check_sum == n * n: # 파란 색종이라면
        blue_cnt += 1
    else: # 해당 사항 없으면 다시 분할
        find_number_of_paper(x_start, y_start, n // 2)
        find_number_of_paper(x_start + n // 2, y_start, n // 2)
        find_number_of_paper(x_start, y_start + n // 2, n // 2)
        find_number_of_paper(x_start + n // 2, y_start + n // 2, n // 2)

n = int(input())    # 한 변의 길이
colored_paper = []  # 정사각형칸의 색
for _ in range(n):
    li = list(map(int, input().split()))
    colored_paper.append(li)

white_cnt = 0   # 햐얀색 색종이의 개수
blue_cnt = 0    # 파란색 색종이의 개수

find_number_of_paper(0, 0, n)

print(white_cnt)
print(blue_cnt)