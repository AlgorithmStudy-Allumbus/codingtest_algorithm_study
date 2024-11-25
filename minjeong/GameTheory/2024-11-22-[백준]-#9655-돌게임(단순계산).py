import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())

if n % 2 == 0:
    print("CY")  # 짝수일 때 CY 승리
else:
    print("SK")  # 홀수일 때 SK 승리
