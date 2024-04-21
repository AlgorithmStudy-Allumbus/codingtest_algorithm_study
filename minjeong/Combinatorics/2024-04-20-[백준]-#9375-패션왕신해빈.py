tc = int(input())  # 테스트 케이스의 수 입력
for _ in range(tc):
    n = int(input())  # 의상의 수 입력
    clothes = {}  # 의상 종류별로 의상을 저장할 사전
    for _ in range(n):
        cloth_name, cloth_type = map(str, input().split())
        if cloth_type in clothes:
            clothes[cloth_type].append(cloth_name)
        else:
            clothes[cloth_type] = [cloth_name]
    
    # 각 의상 종류별로 선택할 수 있는 방법의 수 계산 (아무것도 선택하지 않는 경우 포함)
    combinations = 1
    for key in clothes:
        combinations *= (len(clothes[key]) + 1)
    
    # 알몸 상태 제외 (모든 의상 종류에서 아무것도 선택하지 않는 경우)
    combinations -= 1
    
    print(combinations)  # 가능한 조합의 수 출력
