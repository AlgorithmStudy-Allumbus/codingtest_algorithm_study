answer = 0
def solution(n):
    
    def backtracking(path,lv):
        # 재귀 종료
        global answer
        if lv >= len(path):
            if sum(path)==n : 
                answer += 1 
            # print(f"{lv} : {path} >{answer}")
            return 0
        #자식 노드 이동 
        for x in [1,2] :
            if sum(path) + x <= n : 
                path[lv] = x 
                backtracking(path , lv+1)
            # backtracking
            path[lv] = 0 
            
    for m in range(1,n+1) :
        backtracking([0]*m , 0)
    return answer%1234567