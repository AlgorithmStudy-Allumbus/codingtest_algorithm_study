def solution(s):
    answer = []
    # 1. 문자열 속 모든 "0" 제외하기 & 제외한 0 개수 누적 합
    # 2. 남은 문자열 크기의 값을 이진수 변환 
    #3. 변환된 이진수를 다시 [1]번의 입력으로 넣어 반복(문자열 길이가 1이 될때 까지) 
    
    a = 0 
    rotate = 0 
    while len(s) > 1 :
        cnt = 0
        for n in s : 
            if n == "0" :
                a+=1
                continue
            cnt +=1

        s= str(bin(cnt))[2:]
        rotate += 1
    
    answer = [rotate , a]
    return answer