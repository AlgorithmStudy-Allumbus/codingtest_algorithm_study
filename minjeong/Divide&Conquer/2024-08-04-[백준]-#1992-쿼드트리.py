import sys
input = sys.stdin.readline

def quad_tree(x_start, y_start, n):
    global answer
    cnt = 0  # 압축이 가능한 지 여부를 확인하기 위한 변수
    for i in range(x_start, x_start + n):
        for j in range(y_start, y_start + n):
            cnt += grid[i][j]

    if cnt == 0:  # 다 더한 값이 0이라면 0으로 압축 가능
        answer += "0"
    elif cnt == n * n:  # 다 더한 값이 1*n*n이라면 1로 압축 가능
        answer += "1"
    else:  # 해당 사항 없으면 분할
        answer += "("  # 가장 먼저 괄호 열고
        quad_tree(x_start, y_start, n // 2)  # 왼쪽 위
        quad_tree(x_start, y_start + n // 2, n // 2)  # 오른쪽 위
        quad_tree(x_start + n // 2, y_start, n // 2)  # 왼쪽 아래
        quad_tree(x_start + n // 2, y_start + n // 2, n // 2)  # 오른쪽 아래
        answer += ")"  # 호출이 모두 끝날 경우 괄호 닫음

n = int(input())    # 영상의 크기
grid = []           # 영상 배열
for _ in range(n):
    li = input().strip()
    li = list(map(int, li))  # 문자열을 int형으로 변환하여 리스트로 저장
    grid.append(li)

answer = ""
quad_tree(0, 0, n)

# 정답 출력
print(answer)