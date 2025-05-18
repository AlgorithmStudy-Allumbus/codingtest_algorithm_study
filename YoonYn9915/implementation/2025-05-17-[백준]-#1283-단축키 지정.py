'''

1.하나의 옵션에 대해 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가(공백으로 구분하는 것을 이용) 이미 단축키로 지정되었는지 살펴본다.
만약 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정한다.

2. 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정한다.

3.어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.

4. 위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.

'''

import sys

inp = sys.stdin.readline

N = int(inp())

# 단축키로 지정된 대문자 알파벳들
used_shortcuts = set()

# 결과 저장용 리스트
results = []

for _ in range(N):
    original = inp().strip()
    shortcut_index = -1
    words = original.split()
    index_in_string = 0

    # 1단계: 각 단어의 첫 글자 확인
    for word in words:
        char = word[0].upper()
        if char not in used_shortcuts:
            used_shortcuts.add(char)
            shortcut_index = index_in_string
            break
        index_in_string += len(word) + 1  # 공백 포함해서 다음 인덱스 계산

    # 2단계: 전체 문자열 순회
    if shortcut_index == -1:
        for i, char in enumerate(original):
            if char != ' ' and char.upper() not in used_shortcuts:
                used_shortcuts.add(char.upper())
                shortcut_index = i
                break

    # 단축키 표시
    if shortcut_index != -1:
        marked = (
            original[:shortcut_index]
            + '[' + original[shortcut_index] + ']'
            + original[shortcut_index + 1:]
        )
        results.append(marked)
    else:
        results.append(original)

# 출력
print('\n'.join(results))