import sys 
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())
chars = input().split()
chars.sort() # 오름차순 정렬 

vowels = set('aeiou')
result = []

# 백트래킹: 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법
# 현재까지 만든 암호의 길이가 L이면 종료 조건 
# 모음/자음 개수를 체크해서 만족할 경우 출력 
# 그렇지 않으면 다음 알파벳을 선택해 재귀 호출 
def backtrack(path, start):
    # 1. 종료 조건: 길이가 L이면 조합 완성 
    if len(path) == L: 
        vowel_count = 0 
        consonant_count = 0 
        
        # 모음/자음 개수 세기 
        for ch in path: 
            if ch in vowels: 
                vowel_count += 1
            else: 
                consonant_count += 1 
        
        # 조건에 맞으면 출력 
        if vowel_count >= 1 and consonant_count >= 2: 
            print(''.join(path))
        return 
    
    # 2. 가능한 모든 문자에 대해 선택
    for i in range(start, C): # C == len(chars)
        # 선택 
        path.append(chars[i])
        # 재귀 호출(다음 문자 선택) - 조합이므로 i+1부터
        backtrack(path, i+1)
        # 선택 취소  
        path.pop()
        
# 탐색 시작 
backtrack([], 0)