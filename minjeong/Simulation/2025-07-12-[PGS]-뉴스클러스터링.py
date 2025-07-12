def solution(str1, str2):
    """
    1. 다중집합 만들기
    - 문자열을 2글자씩 끊기
    - 두 글자가 모두 알파벳일 때에만 저장하기 (`isalpha()` 이용)
    - 대소문자 구분이 없으므로 모두 대문자 또는 소문자 둘 중 하나로 통일하기 (`upper()` or `lower()` 이용)
    2. 다중집합 간의 교집합과 합집합 구하기
        - 다중집합은 중복된 원소를 포함할 수 있다. 따라서 `remove()`를 이용해서 하나씩 비교하며 처리한다.
        - 교집합: A 집합과 B 집합의 공통된 원소를 제거해가면서 교집합을 저장할 리스트(`intersect`)에 저장한다
        - 합집합: A의 차집합(A - B) + B의 차집합(B - A) + 교집합으로 구성한다.
    3. 자카드 유사도 구하기
        - 합집합이 공집합일 경우(=합집합 리스트 길이가 0), 유사도는 1로 처리한다.
        - 그게 아닐 경우, `교집합 / 합집합`
    4. 정답 반환
        - `자카드 유사도 * 65536` 의 정수 부분을 반환한다.
    """
    # 1. 다중집합 만들기
    a = []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            a.append(str1[i:i + 2].upper())

    b = []
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            b.append(str2[i:i + 2].upper())

    # 2.1. 다중합집합 구하기
    union_set = a.copy()
    a_minus_b = a.copy()  # A의 차집합

    for i in b:
        if i not in a_minus_b:  # b에는 있지만 a에 있는 건 b의 차집합이다. 따라서 Union에 추가한다.
            union.append(i)
        else:  # a_minus_b는 a의 차집합으로 b와 중복되는 게 있다면 지워야 한다.
            a_minus_b.remove(i)

    # 2.2. 다중교집합 구하기
    inter_set = []
    for i in b:
        if i in a:
            a.remove(i)
            inter_set.append(i)

    # 3. 자카드 유사도 계산
    if len(union) == 0:  # 합집합이 0이라면
        return 65536

    similarity = len(inter_set) / len(union)

    # 정답 출력
    return int(similarity * 65536)