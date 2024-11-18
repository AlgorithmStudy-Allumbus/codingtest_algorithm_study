from itertools import permutations
import math


# 소수 판별 함수
def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:  # i로 나누어 떨어지면 소수가 아니므로 False 리턴
            return False
    return True  # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴


# 문제 해결 함수
def solution(numbers):
    answer = 0
    numbers_list = list(numbers)
    prime_set = set()

    # 모든 순열 생성
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers_list, i):
            prime_set.add(int(''.join(perm)))

    prime_set -= {0, 1}  # 0 또는 1은 순열 집합에서 제거하기

    # 순열 집합에서 소수인 값을 발견하면 +1
    for num in prime_set:
        if is_prime_num(num):
            answer += 1

    return answer
