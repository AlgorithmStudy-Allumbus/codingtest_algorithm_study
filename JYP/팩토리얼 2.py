def fac(n):
    if n <= 1: # 종료조건
        ans = 1
    else:
        ans = fac(n-1) * n # 재귀
        
    return ans

print(fac(int(input())))
