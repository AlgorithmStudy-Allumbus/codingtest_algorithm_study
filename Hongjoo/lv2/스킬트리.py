
# skillset이 선행조건 충족 여부 확인 함수 
def check_skill(words , skill) :
    set_p = 0 ; 
    for c in words :  
        # 해당 스킬(c) 가 선행스킬 속 존재여부 파악 및 순번 확인
        idx = skill.find(c) 
        if idx < 0 :  # ok
            continue
        elif idx  == set_p :  # ok
            set_p +=1 
            continue
        else : 
            # 선행 스킬 순서 보다 더 이르게 w 스킬이 등장한 경우 
            return False
    return True

def solution(skill, skill_trees):
    answer = 0
    # 반복문올 skill_tree 속 선행스킬 조건에 충족하는 스킬 확인 및 개수 계산
    for skillset in skill_trees : 
        if check_skill(skillset , skill) :
            answer += 1                 
    
    return answer