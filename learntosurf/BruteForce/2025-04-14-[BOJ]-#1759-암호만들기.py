import sys 
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())
chars = input().split()
chars.sort() # 오름차순 정렬 

candidates = list(combinations(chars, L)) # L개 고르는 모든 조합을 생성 

# 조건에 맞는 조합 필터링 
# 조건: 모음 >= 1개, 자음 >= 2개 
vowels = set('aeiou')

for comb in candidates: 
    vowel_count = 0 
    consonant_count = 0 
    
    for ch in comb: 
        if ch in vowels: 
            vowel_count += 1 
        else:
            consonant_count += 1
    
    if vowel_count >= 1 and consonant_count >= 2: 
        print(''.join(comb))