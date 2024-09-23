'''
LZW
1. Dic = {seq_length = 1  단어들 }

2. in Dic 현재 입력 matching 된 단어중 가장 max length  가진 문자열 찾기  => w 
3.print(W의 index), input 에서 제거 pop
4 입력에서 처리 되지 않은 다음 글자 c  있으면 -> w+c를 사전에 등재 
5.2로 regress 
| condition
1. 대문자만 
2,dic_index : 1 ~ 

'''
dic = [0 , "A" , "B" , "C" , "D" ,"E", "F" , "G" , "H" , "I" , "J" , "K" , "L", "M" , "N" , "O", "P", "Q", "R", "S" , "T" , "U" , "V" , "W", "X" , "Y" , "Z"] 
def compression_check(left_w , dic):
    # 1 . dic에 w 의 여부
    # 2. W 와 total_c  찾기 : 2point matching 된 단어중 가장 max length -
    # answer =[] ; 
    count = 0
    i = 0; j = len(left_w) #  i : start ,j : end 
    while i != j and j >= 0: # c가 없음 -> 끝
        # print("1" ,left_w[i:j]  ,i , j)
        count+=1
        if left_w[i:j]in dic : 
            print("2"  , i, j)          
            w = left_w[i:j] 
            c = left_w[j]
            dic.append(w+c)
            print(w ,c,dic)
            idx = dic.index(w)
            # answer.append(idx)
            print("w_idx" , idx)
            # left_w = "" + c  # 초기화
            i = j #업데이트 
            return idx , j 
            # print("#" , w , c , dic , left_w)
            
        # print("-1")
        j=j-1
        # print(j)

        
def solution(msg):
    answer = []    
    
    
    # 1. inintialize dic
    # dic = [0 , "A" , "B" , "C" , "D" ,"E", "F" , "G" , "H" , "I" , "J" , "K" , "L", "M" , "N" , "O", "P", "Q", "R", "S" , "T" , "U" , "V" , "W", "X" , "Y" , "Z"] # total 26 + "0" = 1 -> 1~ 26 only valid
    #2. 
    a = 0 ; c ="a"
    answer = []
    a , j_c  = compression_check(msg , dic)
    answer.append(a)
    
    while j_c > 0 : 
        a,j_c = compression_check(msg[j_c:] , dic)
        print(a)
    
    # print("####", answer)
    return answer