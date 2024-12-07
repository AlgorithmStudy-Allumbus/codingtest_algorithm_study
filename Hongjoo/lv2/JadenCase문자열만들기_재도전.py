def solution(s):
    answer = ""
    s = s.split(' ') # 1.단어별로 splite 된 list 
    for i in range(len(s)) : #2.각 단어별로 맨 앞글자 대문자,그외 소문자로 변환 
        #capitalize : 첫문자는 대문자,그외는 소문자로 만듦
        s[i] = s[i].capitalize()
    answer = " ".join(s)#3. 분리해둔 단어들을 한개의 str로 합치기
    
    return answer