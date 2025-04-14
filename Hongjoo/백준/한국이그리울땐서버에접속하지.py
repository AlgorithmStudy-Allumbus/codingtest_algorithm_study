"""
https://www.acmicpc.net/problem/9996
"""
N = int(input())
# Q. a*b는 asbasd도 정답인가? 
# 1. 변수 입력 받기
pattern = list(input().split('*'))
cmstr = [[] for k in range(N)]

for i in range(N):
    # cmstr[i] = [x for x in input()]
    cmstr[i] = input()
#2. 

for i in range(N):
    # 패턴 앞, 뒤 매칭하기 
    if cmstr[i][:len(pattern[0])] != pattern[0] or cmstr[i][-len(pattern[-1]):] != pattern[-1]:
        print("NE")
        continue
    # 안 맞음
        
    flag = [False * len(pattern[1:-1])]
    point = len(pattern[0])
    for p in pattern[1:-1] : # 패턴 내부 
        cnt = cmstr[i][point:].find(p) 
        if cnt < 0 :  #없으면 
            print("NE")
            break
        # 있으면 - 그 이전에 있음
        point = cnt    

    print("DA")

     
