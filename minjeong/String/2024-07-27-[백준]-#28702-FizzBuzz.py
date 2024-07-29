import sys
from math import ceil
input = sys.stdin.readline

# FizzBuzz 문자열 배열
fizzbuzz = [0] * 3
for i in range(3):
    fizzbuzz[i] = input().strip()

for s in fizzbuzz:
    if s.isdigit(): # 문자열이 숫자로 이루어져있다면,
        idx = fizzbuzz.index(s) # 해당 문자열의 위치를 저장하여
        answer = int(fizzbuzz[idx]) + (3 - idx) # 정답 값을 구하기

# FizzBuzz 규칙에 따라 정답 출력
if answer % 3 == 0 and answer % 5 == 0:
    print("FizzBuzz")
elif answer % 3 == 0:
    print("Fizz")
elif answer % 5 == 0:
    print("Buzz")
else:
    print(answer)


