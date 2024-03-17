from collections import Counter

def solution(str1, str2):
    answer = 0
    A = [] # str1 
    B = [] # str2
    
	# str1과 str2 전처리: 2개씩 끊어서 저장하기
    for i in range(len(str1)):
        temp = str1[i:i+2].lower()  # 대소문자 구분 X
        if temp.isalpha() and len(temp) == 2:
            A.append(temp)
            
    for i in range(len(str2)):
        temp = str2[i:i+2].lower()  # 대소문자 구분 X
        if temp.isalpha() and len(temp) == 2:
            B.append(temp)
    
    # Counter 객체로 변환 
    A = Counter(A)
    B = Counter(B)

    # 교집합과 합집합 구하기
    intersection = A & B
    union = A | B
    
    # 합집합의 수가 0인 경우에 대한 예외처리
    if sum(union.values()) == 0:
        answer = 65536
    else:
        answer = int(sum(intersection.values()) / sum(union.values()) * 65536)

    return answer
    