def solution(brown, yellow):
    carpet_size = brown + yellow # 카펫의 전체 크기
    
    for w in range(1,int(carpet_size**0.5)+1): # 약수 범위 설정. 여기서 w는 너비를 의미함
        if carpet_size % w == 0: # 약수라면
            h = carpet_size // w # 전체 크기에서 너비로 나눈 값을 높이로 설정
            
            if (2*w + 2*h - 4 == brown) and ((w-2)*(h-2) == yellow): # 조건에 해당하는지 확인
                return [max(w, h), min(w,h)] 
                