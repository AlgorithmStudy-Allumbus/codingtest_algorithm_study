def defend(use_k,n,k,enemy_i):
    if use_k : # use_k true
        return n ,k-1
    else : # no uese_k
        return n-enemy_i, k
    
def solution(n, k, enemy):
    answer = 0
    graph = [[] for _ in range(len(enemy)+1)]
    graph[0] =[[n,k]]
    #매 i 라운드 별로
    for i in range(len(enemy)) :
        # print("길이:",len(graph[i]))
        if len(graph[i]) == 0 : # 길이 0(중간에 끝나는 경우)
            # print(i-1)
            return i-1
        for r in graph[i]:
            input_n = r[0] ; left_k= r[1]
            #1-1  use k /no use k  -> [남은 n, 남은 k]
            for use_k in [0,1]:
                x,y = defend(use_k,input_n,left_k,enemy[i])
                if x>=0 and y>=0 :
                    graph[i+1].append([x,y])
                    # print(f"{i+1}라운드: {[x,y]} =>{graph[i+1]}")
    #모든 라운드 통과
    answer = len(enemy)
    return answer
                                      
                                       
                                