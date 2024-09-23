"""
 (1)평행선 -> 같은 기울기
(2) 두 직선이 일치하는 경우도 
"""

def solution(dots):
    # 모든 직선의 기울기 구하기
    # 1. 점 2개 선택 
    # 2. 기울기 
    answer = 0
    loops= []
    
    for i in range(len(dots)) :
        for j in range(i+1, len(dots)) : 
            x1 , y1 = dots[i]
            x2 , y2 = dots[j]
            print(f"### {x1} ,{y1} , {x2} , {y2}")
            output= (y1-y2)/(x1-x2+0.0001)
            loop = abs(output)
            print(f"##{loop}")
            for l in loops : 
                if loop == l : 
                    return  1 
            loops.append(loop)
    print("$" ,loops)    

    return answer