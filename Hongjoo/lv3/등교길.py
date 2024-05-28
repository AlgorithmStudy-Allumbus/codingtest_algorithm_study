def solution(m, n, puddles):
    #DP
    answer = 0
    #1.i=0,1 or j=0,1 -> map[i.j] =1 
    map = [[1]*(m+1) for _ in  range(n+1)]#n+1xm+1
    #print(map)
    # puddles -> map[i,j] =0 으로 세팅
    # for p in puddles :
    #     map[p[0]][p[1]] = 0
    
    for i in range(n+1):
        for j in range(m+1):
            if [i,j] in puddles:
                print("##p=0:",i,j,"skip")
                map[i][j] = 0
                continue
            if i in [0,1] or j in [0,1] :
                print("##p=1:",i,j,"skip")
                continue
            map[i][j] = map[i][j-1] + map[i-1][j]
            #print(i,j,":",map[i][j] ,"=", map[i][j-1] ,"+", map[i-1][j])
    #print(map)
    answer = map[n][m]
    
    #print(map[n][m-1]+map[n-1][m] )
    return answer%1000000007