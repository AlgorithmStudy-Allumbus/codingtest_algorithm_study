import sys
from math import ceil
input = sys.stdin.readline

n = int(input()) # 참가자 수
sizes = list(map(int, input().split())) # 티셔츠사이즈별 신청자 수(S, M, L, XL, XXL, XXXL)
t, p = map(int, input().split()) # t: 티셔츠 묶음 수, p: 펜 묶음 수

# t장씩 최소 몇 묶음 주문해야 하는지 계산
min_t_shirts = 0
for s in sizes:
    min_t_shirts += ceil(s / t)
print(min_t_shirts)

# p자루씩 최대 몇 묶음 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문하는지 계산
print(n // p, n % p)
