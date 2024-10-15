import sys

input = sys.stdin.readline

# 좋은 수열인지 검사하는 함수 (유망성 검사 함수)
def is_good(sequence):
    length = len(sequence)
    for i in range(1, length // 2 + 1):
        # 인접한 두 부분 수열이 동일한 경우 False
        if sequence[-i:] == sequence[-2 * i:-i]:
            return False
    return True


def backtracking(sequence, n):
    # 종료 조건: 수열의 길이가 n이면 출력하고 프로그램 종료
    if len(sequence) == n:
        print(sequence)
        exit()

    for num in "123":
        new_sequence = sequence + num       # 새로운 수를 붙여봄
        if is_good(new_sequence):           # 좋은 수열인지 확인
            backtracking(new_sequence, n)   # 재귀 호출로 다음 수 탐색

n = int(input())    # 수열의 길이
backtracking("", n)