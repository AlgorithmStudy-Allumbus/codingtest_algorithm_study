from itertools import permutations

def solution(k, dungeons):
    # k : current_tired 
    #1.순열 -> 입장 순서 모든 경우의 수
    dun_len= len(dungeons)
    order = permutations(dungeons , dun_len)
    answer = 0
    #2.입장 가능 여부 확인 => 최대 던전 수 = answer 반환
    # k < 최소 필요 피로도 , break
    # 최소 필요 피로도 >= 소모 피로도
    for permute in order : 
        hp = k
        count = 0
        for p in permute :

            if hp >= p[0] : 
                hp -=p[1]
                count += 1
        if count >answer :
            answer = count
            
    return answer