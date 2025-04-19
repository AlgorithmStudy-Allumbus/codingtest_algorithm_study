import sys
input = sys.stdin.readline

L, C = map(int, input().split())  # L: 암호 길이, C: 문자 종류
chars = sorted(input().split())   # 사전순 정렬
vowels = {'a', 'e', 'i', 'o', 'u'}


def is_valid(word):
    # 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어있는지 확인
    vowel_cnt, consonant_cnt = 0, 0  # 모음 개수, 자음 개수
    for w in word:
        if w in vowels:
            vowel_cnt += 1
        else:
            consonant_cnt += 1

    return vowel_cnt >= 1 and consonant_cnt >= 2


def backtrack(word, start):
    if len(word) == L:  # 종료 조건
        if is_valid(word):
            print(''.join(word))
        return

    for i in range(start, C):
        word.append(chars[i])
        backtrack(word, i+1)
        word.pop()

backtrack([], 0)
