"""
https://www.acmicpc.net/problem/1759

4 6
a t c i s w
['a', 'c', 'i', 's', 't', 'w']
- 문자 C 가지로 서로 다른 L개의 문자로 이뤄진 비번
- 비번은 최소 1개의 모음 , 최소 2개의 자음
- 정렬된 문자열 
- goal) 모든 경우의 수 

# 1. 문자 정렬 + 모음 . 자음 나눠두기 
# 2. 중복 x 일반 조합 ? (Backtraking)
# 중복x , 순서 x , (조합)

"""
L , C  = map(int,input().split())
arr = sorted(list(input().split())) #  전체 정렬

# print(f"1 -{arr}")
result = [""] * L 
# print(arr)
# 전체 l 경우에서 c 개 조합
def backtracking(c , l , level , idx) :
    if level == l :
        a = 0 ; b = 0  
        # print(f"result {result}")
        for k in range(l) :
            if result[k] in [ "a" , "e" , "i" ,"o" ,"u"]:
                a +=1
            else :
                b += 1
        if a >= 1 and b >= 2 : 
            print("".join(result))

        return
    for s in range(idx , c) :
        
        result[level] = arr[s]
        backtracking(c,l,level+1, s+1)
        
        

backtracking(C , L , 0,0)