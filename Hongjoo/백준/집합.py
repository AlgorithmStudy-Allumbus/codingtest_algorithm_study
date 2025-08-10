"""
[BOJ]#11723. 집합 / 실버5 / 비트마스킹
문제 : https://www.acmicpc.net/problem/11723
# PROBLEM
add x / remove x / check x . toggle x / 
all , empty 
"""
import sys
input = sys.stdin.readline
# answer = []
M = int(input())
s = [ 0 for _ in range(21)] # 1<=x <=20 숫자 제한 존재함
for _ in range(M) :
    operations = list(input().split())
    # 1. empty, all 
    if len(operations) <2 : 
        if operations[0] == "all" :
            s = [1 for _ in range(21)]
        elif operations[0] == "empty" :
            s = [0 for _ in range(21)]
    # 2. add, remove , check , toggle
    else :
        ops , x = operations
        if ops == "add" :
            s[int(x)] = s[int(x)] | 1 
        elif ops == "remove" :
            s[int(x)] = s[int(x)] & 0 
        elif ops == "check" :
            print(s[int(x)])
            # answer.append(s[int(x)])
        elif ops == "toggle" : # NAND - 같으면 0 , 다르면 1
            s[int(x)] = s[int(x)]^1
    
# #3. 결과 출력
# for a in answer:
#     print(a)