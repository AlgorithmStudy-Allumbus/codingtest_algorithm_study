def check_password(password):
    num_vowel = sum(1 for c in password if c in 'aeiou')
    num_consonant = len(password) - num_vowel
    return num_vowel >= 1 and num_consonant >= 2

def recursion(start, depth, password):
    if depth == L:
        if check_password(password):
            answers.append(password)
        return

    for i in range(start, len(letters)):
        recursion(i + 1, depth + 1, password + letters[i])

L, C = map(int, input().split())
letters = sorted(input().split())
answers = []

recursion(0, 0, '')

for ans in answers:
    print(ans)
