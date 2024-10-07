from itertools import product

def solution(word):
    answer = 0
    c_list = ['A', 'E', 'I', 'O', 'U']
    dictionary = []

    for i in range(1, len(c_list) + 1):
        for j in product(c_list, repeat=i):
            dictionary.append(''.join(j))
    dictionary.sort()

    return dictionary.index(word) + 1