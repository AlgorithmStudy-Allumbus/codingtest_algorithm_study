def solution(brown, yellow):
    carpet_size = brown + yellow # 카펫의 전체 크기
    
    for w in range(1,int(carpet_size**0.5)+1): # 약수 범위 설정. 여기서 w는 너비를 의미함
        if carpet_size % w == 0: # 약수라면
            h = carpet_size // w # 전체 크기에서 너비로 나눈 값을 높이로 설정
            
            if (2*w + 2*h - 4 == brown) and ((w-2)*(h-2) == yellow): # 조건에 해당하는지 확인
                return [max(w, h), min(w,h)] 
                
# # 다른 풀이 1            
# def solution(brown, yellow):
#     for i in range(1, int(yellow**(1/2))+1):
#         if yellow % i == 0:
#             if 2*(i + yellow//i) == brown-4:
#                 return [yellow//i+2, i+2]
            
# # 다른 풀이2
# import math
# def solution(brown, yellow):
#     w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
#     h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
#     return [w,h]

# # 다른 풀이 3
# def solution(brown, yellow):
#     nm = brown + yellow
#     for n in range(1, nm+1):
#         if nm%n != 0:
#             continue
#         m = nm//n
#         if (n-2)*(m-2) == yellow:
#             return sorted([n, m], reverse = True)