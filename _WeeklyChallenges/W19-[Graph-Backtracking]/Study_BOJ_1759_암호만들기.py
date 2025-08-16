"""
BOJ #1759. 암호 만들기 (골드5)
https://www.acmicpc.net/problem/1759
유형: Graph, Backtracking
"""

"""
풀이1: 백트래킹
"""
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


"""
풀이2: 조합
출처: https://velog.io/@dlgosla/%EB%B0%B1%EC%A4%80-BOJ-%EC%95%94%ED%98%B8-%EB%A7%8C%EB%93%A4%EA%B8%B01759-python
"""
from itertools import combinations

L, C = map(int, input().split())

alphabets = input().split()

# 길이가 L인 모든 조합, 증가하는 순서로 배열해야되기 때문에 sort 후 comb
alpha_combs = combinations(sorted(alphabets), L)

answer = []

for alpha_comb in alpha_combs:  # 가능한 조합 중에서
    consonant_count = 0
    vowel_count = 0

    # 자음 모음 개수 세기
    for alpha in alpha_comb:
        if alpha in "aeiou":
            consonant_count += 1
        else:
            vowel_count += 1

    # 모음이 1개 이상, 자음이 2 개 이상이면 출력
    if consonant_count >= 1 and vowel_count >= 2:
        print("".join(alpha_comb))

"""
풀이3: DFS 재귀 방식
출처: https://velog.io/@dlgosla/%EB%B0%B1%EC%A4%80-BOJ-%EC%95%94%ED%98%B8-%EB%A7%8C%EB%93%A4%EA%B8%B01759-python
"""
L, C = map(int, input().split())

alphabets = sorted(input().split())


def dfs(idx, codes):
    if L == idx:
        vowel_count = 0
        consonant_count = 0

        # 자음 모음 개수 세기
        for code in codes:
            if code in "aeiou":
                consonant_count += 1
            else:
                vowel_count += 1

        # 자음 2개 이상, 모음 한개 이상이면 암호가 될 수 있으므로 출력
        if consonant_count >= 1 and vowel_count >= 2:
            print("".join(codes))

    else:
        for i in range(idx, C):
            if codes and alphabets[i] <= codes[-1]:  # 오름차순 아니면 버림
                continue
            dfs(idx + 1, codes + [alphabets[i]])


dfs(0, [])
