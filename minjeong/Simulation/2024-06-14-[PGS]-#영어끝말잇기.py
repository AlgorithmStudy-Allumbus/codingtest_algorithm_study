def solution(n, words):
    done = [words[0]] # 사용한 단어 저장
    flag = 0
    for i in range(1, len(words)):
        # 중복 단어 체크
        if words[i] in done: 
            person = (i % n) + 1
            turn = ( i // n) + 1
            return [person, turn]
        # 끝말잇기 이어지는지 체크
        if done[i-1][-1] != words[i][0]:
            person = (i % n) + 1
            turn = ( i // n) + 1
            return [person, turn]
    
        # 조건 통과하면 단어 추가
        done.append(words[i])
    
    # 탈락자가 없으면 [0,0] 반환
    return [0,0]


'''
GPT
'''
'''
def solution(n, words):
    used_words = set()  # 이미 사용된 단어를 저장하는 집합
    used_words.add(words[0])  # 첫 번째 단어는 미리 저장
    for i in range(1, len(words)):
        # 중복 단어 사용 여부 체크
        if words[i] in used_words:
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]
        # 끝말잇기 규칙 체크 (이전 단어의 마지막 글자와 현재 단어의 첫 글자 비교)
        if words[i][0] != words[i-1][-1]:
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]
        # 조건을 모두 통과하면 단어를 집합에 추가
        used_words.add(words[i])
    # 탈락자가 없으면 [0, 0] 반환
    return [0, 0]

'''